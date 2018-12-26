import datetime
from werkzeug import generate_password_hash,check_password_hash

#extracts all details of a user for validation
def extract_user_details(cursor,email_id):
	cursor.execute("select * from Customer where email_id=\""+email_id+"\";")
	data= cursor.fetchall()
	data_list = []
	for row in data :
		row_list = []
		for col in range(len(row)) :
			row_list.append(str(row[col]))
		data_list.append(row_list)
	return data_list

#creates an entry for a user
def insert_user_details(conn,cursor,user_name,password,email_id,phone_no,company) : 
	hashed_password = generate_password_hash(password)
	str_exec = "insert into Customer (customer_id, user_name,hashed_password, email_id, phone_no,company_name) values(NULL,\""+user_name+"\",\""+ str(hashed_password) +"\",\""+ email_id +"\",\""+ phone_no +"\", \""+ company +"\");"
	cursor.execute(str_exec)
	conn.commit()
	cursor.execute("select customer_id from Customer where email_id=\""+email_id+"\";")
	data = cursor.fetchall()
	return str(data[0][0])

#check if the user already has an  account
def check_unique(cursor,email_id) :
	cursor.execute("select email_id from Customer;")
	data= cursor.fetchall()
	
	for row in data :
		for col in range(len(row)) :
			if (col == 0 and email_id == str(row[col])) :
				return False
	
	return True

# get statistics like ideas,posts , likes, dislikes and comments
def extract_user_statistics(cursor,user_id) :
	 
	cursor.execute("select Date_of_post,idea_id from Customer_vote where customer_id=\""+str(user_id)+"\";")
	dates_votes = cursor.fetchall()
	cursor.execute("select Date_of_post,comment_id from comments where customer_id=\""+str(user_id)+"\";")
	dates_comments= cursor.fetchall()
	cursor.execute("select Date_of_post, problem_id from Problem_statement where g_id in (select g_id from Belongs_to where customer_id=\"" + str(user_id) + "\" and role=\"manager\");")
	dates_problems= cursor.fetchall()
	cursor.execute("select Date_of_event,event_id from Events where g_id in (select g_id from Belongs_to where customer_id=\"" + str(user_id) + "\");")
	dates_events= cursor.fetchall()
	return (str_two_dim_list(dates_votes) , str_two_dim_list(dates_comments),str_two_dim_list(dates_problems),str_two_dim_list(dates_events))

# converts a 2d list from unicode to string
def str_two_dim_list(data) :
	data_list = []
	for row in data :
		row_list = []
		for col in range(len(row)) :
			row_list.append(str(row[col]))
		data_list.append(row_list)
	return data_list

# extracts list of groups that a user belongs to , returns group_id,group_name,role
def extract_user_groups(cursor,user_id) :
	cursor.execute("select distinct Groups.g_id,Groups.group_name,Belongs_to.role from Groups,Belongs_to  where Belongs_to.customer_id=" + str(user_id) + " and Groups.g_id = Belongs_to.g_id;")
	data= cursor.fetchall()
	return str_two_dim_list(data)

# gets all details of a user with respect to ideas posted
def get_idea_votes (cursor,user_id):
	cursor.execute("select Date_of_post,idea_id from Ideas where customer_id=\""+str(user_id)+"\";")
	dates_ideas= cursor.fetchall()
	cursor.execute("select Customer_vote.Date_of_post,Customer_vote.Vote,Ideas.idea_id from Customer_vote,Ideas where Ideas.customer_id="+str(user_id) +" and Customer_vote.idea_id = Ideas.idea_id;")
	dates_votes= cursor.fetchall()
	up_votes = [0,0,0,0,0,0,0,0,0,0,0,0]
	down_votes = [0,0,0,0,0,0,0,0,0,0,0,0]
	ideas = [0,0,0,0,0,0,0,0,0,0,0,0]
	for row in range(len(dates_ideas)) :
		date_str = str(dates_ideas[row][0])
		month = date_str.split("-")[1]
		#print(int(month))
		ideas[int(month)-1] = ideas[int(month)-1] + 1
	for row in range(len(dates_votes)) :
		date_str = str(dates_votes[row][0])
		month = date_str.split("-")[1]
		#print(int(month))
		if  str(dates_votes[row][1]) == "Up" :
			up_votes[int(month)-1] = up_votes[int(month)-1] + 1
		if  str(dates_votes[row][1]) == "Down" :
			down_votes[int(month)-1] = up_votes[int(month)-1] + 1
	print(ideas,up_votes,down_votes)
	return (ideas,up_votes,down_votes)

#get all email_ids of a group
def get_group_email_ids (cursor,group_id) :
	cursor.execute("select Customer.email_id from Customer,Belongs_to where Belongs_to.g_id="+group_id+" and Customer.customer_id = Belongs_to.customer_id;")
	data= cursor.fetchall()
	data_list = []
	for row in data :
		data_list.append(str(row[0]))
	return data_list

#gets all groups of a company
def company_groups(cursor,company_name) :
	cursor.execute("select group_name from Groups")
	data= cursor.fetchall()
	data_list = []
	for row in data :
		data_list.append(str(row[0]))
	print(data_list)
	return data_list

#create an entry for a group
def insert_group_details(conn,cursor,group_name,company_name) :
	cursor.execute("insert into Groups (g_id,group_name,company_name) values (NULL,+\"" + group_name + "\", \"" + company_name + "\");")
	conn.commit()
	cursor.execute("select g_id from Groups where group_name =\""+group_name + "\" and company_name=\""+ company_name + "\";")
	data = cursor.fetchall()
	return int(data[0][0])

# inserts email_ids of all members added to group
def insert_members(conn,cursor,email_ids,g_id,cust_id) :
	email_list = email_ids.split(" ")
	cursor.execute("select customer_id,email_id from Customer;" )
	data = cursor.fetchall()
	customer_list = {}
	for row in data :
		customer_list[str(row[1])] = int(row[0])
	print(email_list,customer_list)
	for email in email_list :
		if email!="" and email not in customer_list :
			 return 0
	cursor.execute("insert into Belongs_to (customer_id,g_id,role) values ("+str(cust_id)+"," + str(g_id) + ",'manager');")
	conn.commit()
	for email in email_list :
		if email != "" :
			cursor.execute("insert into Belongs_to (customer_id,g_id,role) values ("+str(customer_list[email])+"," + str(g_id) + ",'developer');")
			conn.commit()
	return 1
				

#insert details of the problem
def insert_problem_details(conn,cursor,g_id,problem_statement) :

	cursor.execute("insert into Problem_statement( problem_id, g_id ,STATEMENT,Date_of_post ) values (NULL, "+str(g_id) + ",\"" + problem_statement + "\",\'" + str(datetime.date.today()) + "\');")
	conn.commit()
# get all events of a group
def get_events(cursor,g_id) :
	
	cursor.execute("select Date_of_event,Name_of_event from Events where g_id="+str(g_id)+";")
	data= cursor.fetchall()
	return str_two_dim_list(data)

# creates entry for all users
def insert_events(conn,cursor,insert_details,g_id) :
	for event in insert_details :
		cursor.execute("insert into Events (event_id,Date_of_event,Name_of_event,g_id) values (Null,'"+event[0]+"','"+ event[1] + "'," + str(g_id) + ");")
		conn.commit()
#gets problem statements of the group
def get_problem_statements(cursor,g_id,c_id) :
	cursor.execute("select Groups.group_name,Belongs_to.role from Groups,Belongs_to where Belongs_to.customer_id="+str(c_id) + " and Belongs_to.g_id = "+str(g_id) + " and Groups.g_id = Belongs_to.g_id ;")
	data= cursor.fetchall()
	if data[0][1] == "manager" :
		is_manager = 1
	else : is_manager = 0  
	cursor.execute("select problem_id,STATEMENT from Problem_statement where g_id="+str(g_id) + ";")
	data1= cursor.fetchall()
	return (str(data[0][0]),is_manager,str_two_dim_list(data1))
#returns list of names of people in a group
def get_group_members (cursor,group_id) :
	cursor.execute("select Customer.user_name from Customer,Belongs_to where Belongs_to.g_id="+str(group_id)+" and Customer.customer_id = Belongs_to.customer_id;")
	data= cursor.fetchall()
	data_list = []
	for row in data :
		data_list.append(str(row[0]))
	return data_list
# adds a member to a group
def insert_member(conn,cursor,email_id,group_id) :
	email_list = [email_id]
	cursor.execute("select customer_id,email_id from Customer;" )
	data = cursor.fetchall()
	customer_list = {}
	for row in data :
		customer_list[str(row[1])] = int(row[0])
	print(email_list,customer_list)
	for email in email_list :
		if email!="" and email not in customer_list :
			 return 0
	for email in email_list :
		if email != "" :
			cursor.execute("insert into Belongs_to (customer_id,g_id,role) values ("+str(customer_list[email])+"," + str(group_id) + ",'developer');")
			conn.commit()
	return 1

# gets all data about ideas for analysis
def get_ideas(cursor,p_id,c_id,g_id) :
	cursor.execute("select Groups.group_name,Belongs_to.role from Groups,Belongs_to where Belongs_to.customer_id="+str(c_id) + " and Belongs_to.g_id = "+str(g_id) + " and Groups.g_id = Belongs_to.g_id ;")
	data= cursor.fetchall()
	cursor.execute("select Ideas.idea_id,Ideas.STATEMENT,Customer.user_name from Ideas,Customer where Ideas.problem_id="+str(p_id) + " and Customer.customer_id = Ideas.customer_id;")
	data1= cursor.fetchall()
	cursor.execute("select idea_id,count(*) from Customer_vote where Vote = 'Up' and idea_id in (select idea_id  from Ideas where problem_id = "+str(p_id)+") group by idea_id;")
	data2= cursor.fetchall()
	cursor.execute("select idea_id,count(*) from Customer_vote where Vote = 'Down' and idea_id in (select idea_id  from Ideas where problem_id = "+ str(p_id)+") group by idea_id;")
	data3= cursor.fetchall()
	data1 = str_two_dim_list (data1)
	data2 = str_two_dim_list (data2)
	data3 = str_two_dim_list (data3)
	dict_ideas = {}
	for row in data1 :
		dict_ideas[row[0]] = [row[1],row[2],'0','0']
	for row in data2 :
		dict_ideas[row[0]][2] = row[1]
	for row in data3 :
		dict_ideas[row[0]][3] = row[1]
	
	if data[0][1] == "manager" :
		is_manager = 1
		for idea in dict_ideas.keys():
			dict_ideas[idea].append('0')  
	else :
		cursor.execute("select customer_id,idea_id from Customer_vote where Vote = 'Up' and idea_id in (select idea_id  from Ideas where problem_id = "+str(p_id)+");")
		data4= cursor.fetchall()
		cursor.execute("select customer_id,idea_id from Customer_vote where Vote = 'Down' and idea_id in (select idea_id  from Ideas where problem_id = " + str(p_id)+");")
		data5= cursor.fetchall()
		dict_up_votes = {}
		data4 = str_two_dim_list (data4)
		data5 = str_two_dim_list (data5)
		print("hi",data4,data5)
		for row in data4 :
			if row[1] not in dict_up_votes.keys():
				dict_up_votes[row[1]] = []
				dict_up_votes[row[1]].append(row[0])
			else : dict_up_votes[row[1]].append(row[0])
		dict_down_votes = {}
		data4 = str_two_dim_list (data4)
		data5 = str_two_dim_list (data5)
		for row in data5 :
			if row[1] not in dict_down_votes.keys():
				dict_down_votes[row[1]] = []
				dict_down_votes[row[1]].append(row[0])
			else : dict_down_votes[row[1]].append(row[0])
		print(dict_up_votes)
		for idea in dict_ideas.keys() :
			if idea in dict_up_votes.keys() and str(c_id) in dict_up_votes[idea]:
				dict_ideas[idea].append('1')
			elif  idea in dict_down_votes.keys() and str(c_id) in dict_down_votes[idea] :
					dict_ideas[idea].append('2')
			else  : dict_ideas[idea].append('3')
		is_manager = 0	
	print(dict_ideas)
	return is_manager,str(data[0][0]),dict_ideas 

def insert_idea(conn,cursor,p_id,c_id,statement) :

	cursor.execute("insert into Ideas (idea_id ,problem_id,STATEMENT,customer_id ,Date_of_post) values (Null,"+str(p_id)+", \'" + statement +"\',"+str(c_id)+",\'" +str(datetime.date.today()) + "\');")
	conn.commit()

def  delete_vote(conn,cursor,c_id,idea_id) : 
	print("hello")
	cursor.execute("delete from Customer_vote where idea_id = "+str(idea_id)+" and customer_id = "+str(c_id) +";")
	conn.commit()

def  update_vote(conn,cursor,c_id,idea_id,vote) : 
	
	if vote == 1 :
		cursor.execute("update Customer_vote set Vote = 'Up' where idea_id = "+str(idea_id)+" and customer_id = "+str(c_id) +";")
	else : cursor.execute("update Customer_vote set Vote = 'Down' where idea_id = "+str(idea_id)+" and customer_id = "+str(c_id) +";")
	conn.commit()
	

def  add_vote(conn,cursor,c_id,idea_id,vote) : 
	
	if vote == 1 :
		cursor.execute("insert into Customer_vote(customer_id,idea_id,Vote,Date_of_post) values (" + str(c_id) + ","+str(idea_id)+ ",\'Up\',\'" + str(datetime.date.today())  + "\'); ")
	else : cursor.execute("insert into Customer_vote(customer_id,idea_id,Vote,Date_of_post) values (" + str(c_id) + ","+str(idea_id)+ ",\'Down\',\'" + str(datetime.date.today())  + "\'); ")
	conn.commit()
	
def get_comments(cursor,idea_id) :
	cursor.execute("select comments.STATEMENT,Customer.user_name from comments,Customer where comments.idea_id="+str(idea_id) + " and Customer.customer_id = comments.customer_id;")
	data = cursor.fetchall()
	cursor.execute("select Ideas.STATEMENT,Customer.user_name from Ideas,Customer where Ideas.idea_id="+str(idea_id) + " and Customer.customer_id = Ideas.customer_id;")
	data1= cursor.fetchall()
	return str_two_dim_list(data),str_two_dim_list(data1)

def insert_comment(conn,cursor,comment,cust_id,idea_id) :
		
	cursor.execute("insert into comments(comment_id,idea_id,STATEMENT,customer_id,Date_of_post ) values (NULL,"+str(idea_id)+",\'" + comment +"\',"+str(cust_id)+",\'"+str(datetime.date.today())+"\');")
	conn.commit()
def get_idea_analytics (cursor,p_id) :
		cursor.execute("select Ideas.idea_id,Ideas.STATEMENT from Ideas,Customer where Ideas.problem_id="+str(p_id) + ";")
		data1= cursor.fetchall()
		cursor.execute("select idea_id,count(*) from Customer_vote where Vote = 'Up' and idea_id in (select idea_id  from Ideas where problem_id = "+str(p_id)+") group by idea_id;")
		data2= cursor.fetchall()
		cursor.execute("select idea_id,count(*) from Customer_vote where Vote = 'Down' and idea_id in (select idea_id  from Ideas where problem_id = "+ str(p_id)+") group by idea_id;")
		data3= cursor.fetchall()
		data1 = str_two_dim_list (data1)
		data2 = str_two_dim_list (data2)
		data3 = str_two_dim_list (data3)
		dict_ideas = {}
		for row in data1 :
			dict_ideas[row[0]] = [row[1],0,0,0]
		for row in data2 :
			dict_ideas[row[0]][1] = int(row[1])
		for row in data3 :
			dict_ideas[row[0]][2] = int(row[1])
		cursor.execute("select idea_id,count(*) from comments where idea_id in (select idea_id  from Ideas where problem_id = "+str(p_id)+") group by idea_id;")
		data4= cursor.fetchall()
		data4 = str_two_dim_list(data4)
		for row in data4 :
			dict_ideas[row[0]][3] = int(row[1])
		return dict_ideas

def get_comments_sentiment(cursor,ideas) :
		all_data = {}
		for idea in ideas :
			cursor.execute("select STATEMENT from comments where idea_id = "+idea[0]+";")
			data = cursor.fetchall()
			idea_data = []
			for row in data :
				idea_data.append(str(row[0]))
			all_data[idea] = idea_data
		return all_data

def get_doc_links(cursor,g_id) :
	cursor.execute("select doc_links.doc_name,doc_links.link,Customer.user_name from doc_links,Customer where doc_links.g_id="+str(g_id) + " and Customer.customer_id = doc_links.customer_id;")
	data = cursor.fetchall()
	return str_two_dim_list(data)

def insert_doc_links(conn,cursor,g_id,doc_name,link,c_id) :
	
	cursor.execute("insert into doc_links(doc_id,g_id,doc_name,link,customer_id,Date_of_post) values(NULL,"+str(g_id)+",\'"+doc_name+ "\',\'"+link+"\',"+str(c_id)+",\'"+str(datetime.date.today())+"\') ; ")
	conn.commit()

def get_group_name(cursor,g_id) :
	cursor.execute("select group_name from Groups where g_id ="+str(g_id)+";")
	data = cursor.fetchall()
	return str(data[0][0])

def get_group_id(cursor,p_id) :
	cursor.execute("select g_id from Problem_statement where problem_id ="+str(p_id)+";")
	data = cursor.fetchall()
	return str(data[0][0])


