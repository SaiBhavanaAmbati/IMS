def get_sentiments(l_comments):
    import matplotlib.pyplot as plt
    import pandas as pd
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    import matplotlib.pyplot
    from nltk.tokenize import sent_tokenize

    #Retrieve all the most liked/most talked about ideas from the database and place it into a dictionary
    #selected_ideas = retrieve_top_ideas()
    scores={}
    from io import open
    analyzer = SentimentIntensityAnalyzer()

    #for one idea:
    for idea,comments in l_comments.items():
        pos_count = 0
        neg_count = 0
        neut_count = 0
        #retrieve the comment list
        comment_list = comments

        no_of_comments = len(comment_list)

        #comment = "This idea, although may have some merits, might not work in this scenario. It needs a lot more careful thought and planning. There are a lot of loopholes. Maybe if all o them are fixed, it could work."

        for comment in comment_list:
            comment_sentences = sent_tokenize(comment)
            pos_score = 0
            neg_score = 0 
            #neut_score = 0
            for line in comment_sentences:
                score = analyzer.polarity_scores(line)
                #print(line)
                #print(score)
                pos_score += score['pos']
                neg_score += score['neg']
                #neut_score += score['neu']
                length = len(comment_sentences)
            pos = pos_score/length
            neg = neg_score/length
            #neut = neut_score/length
            #print("Pos: ",pos)
            #print("Neg: ",neg)
            #print("Neut: ",neut)
            sentiment = max(pos,neg)
            #print(sentiment)
            if max(pos,neg)==pos:
                pos_count+=1
            elif max(pos,neg)==neg:
                neg_count+=1
            #else:
                #neut_count+=1

        #print(pos_count,neg_count,neut_count)
	if no_of_comments==0:
		pos_percent=0
		neg_percent=0
	else:
        	pos_percent = float(pos_count)/float(no_of_comments)
        	neg_percent = float(neg_count)/float(no_of_comments)
        #neut_percent = neut_count/no_of_comments
        #print(pos_percent,neg_percent)
        scores['idea'+str(idea[0])]=[pos_percent,neg_percent]


    #print(scores)
    #The format of the scores returned: dictionary - {idea1:[pos_score,neg_score], idea2:[pos_score,neg_score]..}
    return scores
"""
#Loading the NRC-emotion-lexicon
'''
nrc_lex = pd.read_csv( "NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt",sep='\t', names=['word','emotion','association'])
#nrc_lex.head()
print ("\n NRC Emotion lexicon loaded...")
col=['anger','fear','anticipation','trust','surprise','joy','sadness','disgust']
emotions=pd.DataFrame(columns=col)
'''
print("Run Before")

'''
#For each review, using the frequency distribution of it's tokens, store the list of the 8 emotion attribute values
#in list and the list of emotion words of that review in emotion_words
emotion_list=[]
emotion_words=[]
ctr=1
for i in df['Tokens']:
    global ctr
    print(ctr)
    anger = 0
    fear = 0
    anticipation = 0
    trust = 0
    surprise = 0
    sadness = 0
    joy = 0
    disgust = 0
    list1=[]
    emotion_word=[]
    freq_dist=nltk.FreqDist(i)
    for w1,w2 in freq_dist.items():
        if nrc_lex['word'].str.contains(w1).any():
            #print ("Found",w1)
            #print w1,w2
            #Change here ..every line is getting printed
            #print (nrc_lex.loc[nrc_lex['word'] == w1])
            anger_list = nrc_lex[nrc_lex['word']==w1][nrc_lex['emotion']=='anger'].index.tolist()
            if len(anger_list) == 1:
                anger += w2*int(nrc_lex.iloc[int(anger_list[0])]['association'])
            fear_list = nrc_lex[nrc_lex['word']==w1][nrc_lex['emotion']=='fear'].index.tolist()
            if len(fear_list) == 1:
                fear += w2*int(nrc_lex.iloc[int(fear_list[0])]['association'])
            anticipation_list = nrc_lex[nrc_lex['word']==w1][nrc_lex['emotion']=='anticipation'].index.tolist()
            if len(anticipation_list) == 1:
                anticipation += w2*int(nrc_lex.iloc[int(anticipation_list[0])]['association'])
            trust_list = nrc_lex[nrc_lex['word']==w1][nrc_lex['emotion']=='trust'].index.tolist()
            if len(trust_list) == 1:
                trust += w2*int(nrc_lex.iloc[int(trust_list[0])]['association'])
            surprise_list = nrc_lex[nrc_lex['word']==w1][nrc_lex['emotion']=='surprise'].index.tolist()
            if len(surprise_list) == 1:
                surprise += w2*int(nrc_lex.iloc[int(surprise_list[0])]['association'])
            sadness_list = nrc_lex[nrc_lex['word']==w1][nrc_lex['emotion']=='sadness'].index.tolist()
            if len(sadness_list) == 1:
                sadness += w2*int(nrc_lex.iloc[int(sadness_list[0])]['association'])
            joy_list = nrc_lex[nrc_lex['word']==w1][nrc_lex['emotion']=='joy'].index.tolist()
            if len(joy_list) == 1:
                joy += w2*int(nrc_lex.iloc[int(joy_list[0])]['association'])
            disgust_list = nrc_lex[nrc_lex['word']==w1][nrc_lex['emotion']=='disgust'].index.tolist()
            if len(disgust_list) == 1:
                disgust += w2*int(nrc_lex.iloc[int(disgust_list[0])]['association'])
            #print ("emotion word: ", w1)
            if w1 not in emotion_word:
                emotion_word.append(w1)
    list1=[anger,fear,anticipation,trust,surprise,joy,sadness,disgust]
    emotion_list.append(list1)
    emotion_words.append(emotion_word)
    ctr+=1
'''

# Building the model 
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
import numpy
from numpy import array

model = Sequential()
model.add(Dense(8, input_dim=8, kernel_initializer='normal', activation='relu'))
model.add(Dense(3, kernel_initializer='normal', activation='relu'))
model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
#model.add(Dense(1, kernel_initializer='normal', activation='softmax'))
# Compile model
epochs = 500
learning_rate = 3
decay_rate = learning_rate / epochs
sgd = SGD(lr=learning_rate, momentum=0.2, decay=decay_rate, nesterov=False)
model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])
#print(categories)
print(emotion_list)
emotion_list = array(emotion_list)
categories = array(categories)
# Fit the model. We manually provide the train and test partition
history=model.fit(emotion_list,categories,validation_split=0.25,epochs=150, batch_size=8, verbose=2)
print(history.history.keys())

# Plotting the model accuracies and model loss
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

"""
