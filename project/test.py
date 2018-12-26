from flask import Flask, render_template, request,redirect
from flaskext.mysql import MySQL
import json
import keygen
#from flask_mail import Mail, Message
from werkzeug import generate_password_hash,check_password_hash
import queries
import svg_path
app = Flask(__name__,static_folder='static',template_folder = 'templates')
from operator import itemgetter
from sentiment_analysis import get_sentiments
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'seproject'
app.config['MYSQL_DATABASE_DB'] = 'IMS_DB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()
from threading import Thread, Condition
import time
import os

queue = []
MAX_NUM = 10
condition = Condition()
command = "curl "
server_addr = "http://localhost:5002/"
email_functions = ["email_welcome","email_post_problem","email_event","email_group","add_user"]
invalid_email = 0
#producer thread for inserting into the queue
class ProducerThread(Thread):
	def __init__(self, req):
	        super(ProducerThread,self).__init__()
	        self.req = req
	def run(self):
		global queue
		condition.acquire()
		if len(queue) == MAX_NUM:
				print("Queue full, producer is waiting")
				condition.wait()
		print("Space in queue, Consumer notified the producer")
		queue.append(self.req)
		print("Produced", self.req)
		condition.notify()
		condition.release()

#consumer thread for seding curl requests
class ConsumerThread(Thread):
	def run(self):
		global queue
		while True:
			condition.acquire()
			if not queue:
				print("Nothing in queue, consumer is waiting")
				condition.wait()
				print ("Producer added something to queue and notified the consumer")
			user_req = queue.pop(0)
			if user_req[0] != 2 : 
				print("Consumed", command+server_addr+email_functions[user_req[0]]+"/"+ user_req[1] + "/" + user_req[2])
				os.system(command+server_addr+email_functions[user_req[0]]+"/"+ user_req[1] + "/" + user_req[2])
			else :
				print("Consumed", command+server_addr+email_functions[user_req[0]]+"/"+ user_req[1] + "/" + user_req[2] + "/" + user_req[3])
				os.system(command+server_addr+email_functions[user_req[0]]+"/"+ user_req[1] + "/" + user_req[2] + "/" + user_req[3])
			condition.notify()
			condition.release()

ConsumerThread().start()

user_session = {"customer_id" : None,  "user_name": None, "hashed_password" : None ,"email_id": None ,"phone_no":None,"company_name" :None }
@app.route("/")
def home() :
	return render_template('home.html')

@app.route('/chat')
def chat():
	return render_template('chat.html')
	
@app.route("/show_login")
def show_login() :
	return render_template('login_san.html',message="")

@app.route("/login_validate", methods=['GET','POST'])
def login_validate() :
	if request.method=="POST" :
		email_id=request.form.get('email')
		password = request.form.get('pass')
		data = queries.extract_user_details(cursor,email_id)
		if check_password_hash(data[0][2],password) :
			user_session["customer_id"] = int(data[0][0])
			user_session["user_name"] = data[0][1]
			user_session["email_id"] = data[0][3]
			user_session["phone_no"] = data[0][4]
			user_session["company_name"] = data[0][5]
			print(user_session)
			return redirect("http://localhost:5001/show_user_profile")
		else :
			return 	render_template('login_san.html',message="Invalid Username/password")		
		
@app.route("/show_signup")
def show_signup() :
	return render_template('Signup.html')

@app.route("/signup_validate",methods=['GET','POST'])
def signup_validate() :
	if request.method=="POST" :
		email_id=request.form.get('email')
		password = request.form.get('password')
		status	= queries.check_unique(cursor,email_id)
		if status == False : 
			return render_template('Signup.html',message = "You already have an account")
		else :
			user_session["user_name"] = request.form.get('user_name')
			user_session["email_id"] = email_id
			user_session["phone_no"] = request.form.get('number')
			user_session["company_name"] = request.form.get('company')
			user_session["customer_id"] = queries.insert_user_details(conn,cursor,user_session["user_name"],password, email_id,user_session["phone_no"],user_session["company_name"])
			my_thread_0 = ProducerThread((0,user_session["user_name"],user_session["email_id"]))
			my_thread_0.start()
			return redirect("http://localhost:5001/show_user_profile")
		
		
	
@app.route("/show_user_profile")
def show_user_profile() :
	if user_session["customer_id"] != None :
		print(user_session["customer_id"])
		group_names = queries.extract_user_groups(cursor,user_session["customer_id"])
		user_stats = queries.extract_user_statistics(cursor,user_session["customer_id"])
		total_stats = []
		for x in user_stats:
				total_stats.append(len(x))
		svg_paths= svg_path.construct_svg_path(user_stats)
		votes_data = queries.get_idea_votes(cursor,user_session["customer_id"])
		#return str(svg_paths)
		return render_template('user_profile.html',groups = group_names, path = svg_paths, name = user_session["user_name"], email= user_session["email_id"], phone_no = user_session["phone_no"], total_graphs = total_stats , user_votes_data = votes_data)
	


@app.route("/show_group_create/<mess>")
def show_group_create(mess) :
	group_names = queries.company_groups(cursor,'PESU')
	if mess != "none" :
		return render_template('groupForm.html', names = group_names, error_message = " ".join(mess.split("-")))
	else :
		return render_template('groupForm.html', names = group_names,  u_name = user_session["user_name"], email= user_session["email_id"])


@app.route("/process_group_form",methods=['GET','POST'])
def process_group_form() :
	if request.method == "POST" :
		group_name = request.form.get('group_name')
		email_ids=request.form.get('emailIDs')
		problem_statement = request.form.get('problem_statement')
		success_group = queries.insert_group_details(conn,cursor,group_name,user_session["company_name"])
		cust_id = user_session["customer_id"]
		if success_group :
			success_email = queries.insert_members(conn,cursor,email_ids,success_group,cust_id) 
			print(success_email)
			if success_email :
				my_thread_3 = ProducerThread((3,str(success_group),group_name))
				my_thread_3.start()
				queries.insert_problem_details(conn,cursor,success_group,problem_statement)
				return redirect("http://localhost:5001/show_user_profile")
			else :
				return redirect("http://localhost:5001/show_group_create/invalid-email-address-but-group-created")
		else :
			return redirect("http://localhost:5001/show_group_create")
		return redirect("http://localhost:5001/show_group_create")

@app.route("/show_calendar/<int:g_id>")
def show_calendar(g_id) :
	list_events = queries.get_events(cursor,g_id)
	print(list_events)
	return render_template('calendar.html',group_id = g_id, events = list_events)

@app.route("/process_events/<int:g_id>",methods=['GET','POST'])
def process_events(g_id) :
	
	if request.method == "POST" :
		event_list = request.form.get('event_name').split(";")
		insert_details = []
		labels = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
		for event in event_list :
			if event != "" :
				details = event.split("title-")
				date_details = details[0].split(" ")
				get_month = labels[date_details[1]]
				get_day = date_details[2]
				get_year = date_details[3]
				full_date = get_year +"-"+ get_month +"-"+ get_day
				insert_details.append((full_date,details[1]))
		g_name = queries.get_group_name(cursor,g_id)
		queries.insert_events(conn,cursor,insert_details,g_id)
		for event in insert_details :
			my_thread_2= ProducerThread((2,str(g_id),g_name,str(event[0])))
			my_thread_2.start()

			
	return redirect("http://localhost:5001/group_profile/"+str(g_id))



@app.route("/group_profile/<int:g_id>")
def group_profile(g_id) : 
	problem_st = queries.get_problem_statements(cursor,g_id,user_session["customer_id"])
	member_names = queries.get_group_members (cursor,g_id)
	if invalid_email == 2 :
		return render_template("manager_dash.html", group_id = g_id, group_name = problem_st[0],members = member_names,  is_manager = problem_st[1],problems = problem_st[2],u_name = user_session["user_name"], email= user_session["email_id"], mess = "successfully added") 
	elif invalid_email == 1 :
		return render_template("manager_dash.html", group_id = g_id, group_name = problem_st[0],members = member_names,  is_manager = problem_st[1],problems = problem_st[2],u_name = user_session["user_name"], email= user_session["email_id"],mess = "Invalid email address") 
	else :
		return render_template("manager_dash.html", group_id = g_id, group_name = problem_st[0],members = member_names,  is_manager = problem_st[1],problems = problem_st[2],u_name = user_session["user_name"], email= user_session["email_id"]) 

@app.route("/process_group_profile/<int:group_id>",methods=['GET','POST'])
def process_group_profile(group_id) : 
	if request.method == "POST" :
		problem_statement = request.form.get('problem_statement')
		if problem_statement != "" : 
			queries.insert_problem_details(conn,cursor,group_id,problem_statement)
			my_thread_1 = ProducerThread((1,str(group_id),queries.get_group_name(cursor,group_id)))
			my_thread_1.start()
			return redirect("http://localhost:5001/group_profile/"+str(group_id))
		email_id = request.form.get('emailID')
		if email_id != "" :
			t = queries.insert_member(conn,cursor,email_id,group_id)
			if(t==1) :
				my_thread_4 = ProducerThread((4,queries.get_group_name(cursor,group_id),email_id))
				my_thread_4.start()
				print("hello")
				invalid_email = 2
				return redirect("http://localhost:5001/group_profile/"+str(group_id))
			else : 
				print("bye")
				invalid_email = 1
				return redirect("http://localhost:5001/group_profile/"+str(group_id))
		return "ok"


@app.route("/problem_statement/<int:g_id>/<int:p_id>")
def problem_statement(g_id,p_id) :
	ideas = queries.get_ideas(cursor,p_id,user_session["customer_id"],g_id)
	member_names = queries.get_group_members (cursor,g_id)
	return render_template('problem_statement.html', group_id = g_id, problem_id = p_id ,members = member_names, ideas_list = ideas[2], group_name = ideas[1], is_manager = ideas[0] ,u_name = user_session["user_name"], email= user_session["email_id"])

@app.route("/process_problem/<int:g_id>/<int:p_id>",methods=['GET','POST'])
def process_problem(g_id,p_id) : 
	if request.method == "POST" : 
		c_id = user_session["customer_id"]
		if(request.form.get('add_idea') != "" ) :
			queries.insert_idea(conn,cursor,p_id,c_id,request.form.get('add_idea'))
		else :  
			change = request.form.get('vote_vector').split('-')
			print(change)
			if change[1] != change[2] :
				if int(change[2]) == 3 :
					queries.delete_vote(conn,cursor,c_id,int(change[0]))
				elif int(change[1]) == 3:
					queries.add_vote(conn,cursor,c_id,int(change[0]),int(change[2]))
				else :  queries.update_vote(conn,cursor,c_id,int(change[0]),int(change[2]))
			
		return redirect("http://localhost:5001/problem_statement/"+str(g_id)+"/"+str(p_id))


@app.route("/idea_desc/<int:idea_id>")
def idea_desc(idea_id) :
	comment_details = queries.get_comments(cursor,idea_id) 
	print(comment_details[1])
	return render_template('idea_desc.html', i_id = idea_id , ideas = comment_details[1] , comments = comment_details[0],u_name = user_session["user_name"], email= user_session["email_id"])

@app.route("/process_comment/<int:idea_id>", methods=['GET','POST'])
def process_comment(idea_id) :
	if request.method == "POST" :
		queries.insert_comment(conn,cursor,str(request.form.get('comment')),cust_id,idea_id)
	return redirect("http://localhost:5001/process_comment/"+str(idea_id))


@app.route("/docs_links/<int:g_id>")
def docs_links(g_id) :
	doc_links = queries.get_doc_links(cursor,g_id)
	return render_template('docs.html',group_id = g_id, docs = doc_links,u_name = user_session["user_name"], email= user_session["email_id"])


@app.route("/process_doc/<int:g_id>", methods=['GET','POST'])
def process_doc(g_id) :
	if request.method == "POST" :
		c_id = user_session["customer_id"]
		queries.insert_doc_links(conn,cursor,g_id,str(request.form.get('doc_name')),str(request.form.get('link')),c_id)
	return redirect("http://localhost:5001/docs_links/"+str(g_id))

@app.route("/idea_dashboard/<int:p_id>")
def idea_dashboard(p_id) :
	idea_attr = queries.get_idea_analytics(cursor,p_id)
	list_idea_index = [] 
	for idea_id in idea_attr.keys() :
		index_val = idea_attr[idea_id][1] - idea_attr[idea_id][2] + idea_attr[idea_id][3] 
		list_idea_index.append((idea_id,idea_attr[idea_id][0], idea_attr[idea_id][1], idea_attr[idea_id][2], idea_attr[idea_id][3], index_val))
	final_ideas = sorted(list_idea_index,key = itemgetter(5),reverse= True)
	no_ideas = len(final_ideas)
	#print(final_ideas)
	group_id = queries.get_group_id(cursor,p_id)
	print("hello",group_id)
	if no_ideas < 4 :
		comments = queries.get_comments_sentiment(cursor,final_ideas)
		ans = get_sentiments(comments)
		return render_template('index.html', ideas_comments = ans, ideas = final_ideas,n_ideas = no_ideas, g_id = group_id)
	else : 
		comments = queries.get_comments_sentiment(cursor,final_ideas[:4])
		ans = get_sentiments(comments)
		return render_template('index.html', ideas_comments = ans, ideas = final_ideas[:4], n_ideas = 4, g_id = group_id)

        
@app.route('/fetch_relevant_info', methods=['GET'])
def get_relevant_docs():
    docs = keygen.getResults(request.args['idea'])
    ranked = keygen.rankDocs(request.args['idea'],docs)
    print(ranked)
    return json.dumps(ranked)

@app.route('/logout', methods=['GET'])
def logout():
	user_session["customer_id"] = None
	user_session["user_name"] = None
	user_session["email_id"] = None
	user_session["phone_no"] = None
	user_session["company_name"] = None
	return 	render_template('login_san.html')



if __name__ == "__main__" :
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(debug=True,port = 5001)
	


