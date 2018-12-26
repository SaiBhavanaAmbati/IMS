import re
import pickle
import requests
import numpy as np
import pandas as pd
from nltk import pos_tag
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from gensim.models import word2vec
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from nltk.tag import StanfordPOSTagger


st = StanfordPOSTagger('english-bidirectional-distsim.tagger', path_to_jar='./stanford-postagger.jar')

# Stop words to be removed
stopfile = open("stop_words.txt","r")
stops = stopfile.read().split('\n')

# Word tokens to be removed from sentences, refer to NLTK tokenizer tags
unwantedtags = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'JJS', 'JJR', 'TO', 'RB', 'DT', 'WRB', 'CC','IN']
wantedtags = ['NN','NNS']

# load the google word2vec model
# Download model to use
filename = 'GoogleNews-vectors-negative300.bin'
gmodel = KeyedVectors.load_word2vec_format(filename, binary=True, limit=500000)

num_features = 300

'''
Convert `raw_answer` to a list of words:
'''
def sentence_to_wordlist(raw_answer):
    '''
    The answer is converted to a list of meaningful words
    '''
    # Removing all numbers
    letters_only = re.sub("[^a-zA-Z]", " ", raw_answer)

    # Converting all letters to lowercase
    words = letters_only.lower().strip().split()

    # Remove stopwords
    #meaningful_words = [w for w in words if not w in stops]
    meaningful_words = [w for w in words]

    return meaningful_words

'''
Function to create word vectors
'''
def makeFeatureVectors(words, model, num_features):
    '''
    Create a word vectors of the words passed using the Word2Vec Model
    '''
    # Initial word vector to a zero vector
    featureVec = np.zeros((num_features,),dtype="float32")

    # Initialize Number of Words to 0
    nwords = 0

    # Index2word is a list that contains the names of the words in 
    # the model's vocabulary. Convert it to a set to improve speed
    index2word_set = set(model.wv.index2word)

    for word in words:
        if word in index2word_set:
            # Count the number of words
            nwords = nwords + 1
            # Create a vector by adding all word vectors it contains
            featureVec = np.add(featureVec,model[word])

    # Divide feature vector by 0 to get average word vector
    featureVec = np.divide(featureVec,nwords)

    return featureVec

'''
Function to create word vectors from a set of answers
'''
def getAvgFeatureVecs(answers, model, num_features):
    '''
    Given a set of answers, calculate the average feature 
    vector and return a 2D numpy array for each one 
    '''
    # Initialize a counter
    counter = 0

    # Allocate a 2D numpy array, for speed
    answerFeatureVecs = np.zeros((len(answers),num_features),dtype="float32")

    # Loop through the answers in an answer set
    for answer in answers:

       # Get average feature vector for each answer in answer set
       answerFeatureVecs[counter] = makeFeatureVectors(answer, model, num_features)

       # Increment the counter
       counter = counter + 1

    return answerFeatureVecs

'''
Function to calculate similarity between two given sentences
'''
def calcSimilarity(sentence1, sentence2, model, num_features):
    featureVecs = getAvgFeatureVecs([sentence1.lower().split(),sentence2.lower().split()], model, num_features)
    similarity = np.dot(featureVecs[0],featureVecs[1])/(np.linalg.norm(featureVecs[0])* np.linalg.norm(featureVecs[1]))
    return similarity

def getIssueCode(sentence, model,num_features):
    v1 = getAvgFeatureVecs([sentence.lower().split()], model, num_features)
    pickle_in = open("symptomglovevectors.pickle","rb")
    symptomfeaturevectors = pickle.load(pickle_in)

    maxsimilarity = np.float(0)
    similarindex = 0
    for index in range(len(symptomfeaturevectors)):
        v2 = symptomfeaturevectors[index]
        similarity  = (np.dot(v1,v2)/(np.linalg.norm(v1)* np.linalg.norm(v2)))[0]
        #print(symptomlist[index],similarity)
        if similarity > maxsimilarity:
            #print(type(similarity),type(maxsimilarity))
            maxsimilarity = similarity
            similarindex = index

    return ' '.join(symptomlist[similarindex])

#Function to remove words belonging to a set of tags from a sentence
def removeTags(sentence, tags):
    tokens = pos_tag(sentence.split())
    remainingWords = [t[0] for t in tokens if t[1] not in tags]
    remainingWords = [w for w in remainingWords if not w.lower() == 'issue']
    return ' '.join(remainingWords)


#Using sentence shortening 
def shortenSentence(sentence):
   
    #Regex to remove any sets of characters that have non alphabet symbols
    sentence = re.sub('([A-Za-z]*[^A-Za-z\s][A-Za-z]*)+\s|\s([A-Za-z]*[^A-Za-z\s]+[A-Za-z]*)+', '', sentence)

    #Removal of stop-words
    words = sentence.split()
    stringwords = [w for w in words if w.lower() not in stops]
    sentence = ' '.join(stringwords)
    
    tokens = pos_tag(sentence.split())


    shortstring = ' '.join([item[0] for item in tokens])

    return shortstring


def assigncode(description):
    # Shorten the sentence
    assignedcode = shortenSentence(description)

    # If the shortened form is one or no words then assign a code from the set of standard issue codes provided
    if(len(assignedcode.split()) < 2):
        assignedcode = getIssueCode(description, gmodel, vector_dimensions)

    # Remove unwanted words
    print(pos_tag(assignedcode.split()))
    assignedcode = removeTags(assignedcode,unwantedtags)
    print("Given description: ", description, "\nAssigned Code : ", assignedcode)

    return assignedcode
    
def getResults(sentence):
    keywords = set(removeTags(sentence,unwantedtags).split())
    query = '%20'.join(keywords)
    url = 'https://scholar.google.com/scholar?q=' + query + '&ie=UTF-8&oe=UTF-8&hl=en&btnG=Search'
    content = requests.get(url).text
    page = BeautifulSoup(content, 'lxml')
    docs = []
    for entry in page.find_all("h3", attrs={"class": "gs_rt"}):
	try:
        	docs.append({'link':entry.a['href'], 'title':entry.a.text})
	except:
		continue
    return docs

def rankDocs(base,docs,model=gmodel,num_features=num_features):
    results = []
    for doc in docs:
        sim = calcSimilarity(base,doc['title'],model,num_features)
        results.append([doc,sim])
    results.sort(key=lambda x: x[1])
    results.reverse()
    results = results[:5]
#    print([res[0] for res in results])
    return [res[0] for res in results]
    

#sentence = 'Image captioning using recurrent neural networks'
#docs = getResults(sentence)
#rankDocs(sentence,docs,gmodel,num_features)
