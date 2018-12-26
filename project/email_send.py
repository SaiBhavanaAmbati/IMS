from flask import Flask, render_template
from flask_mail import Mail, Message
from flaskext.mysql import MySQL
from queries import get_group_email_ids 
app =Flask(__name__)
mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'idea.management.system4@gmail.com'
app.config['MAIL_PASSWORD'] = 'seproject'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'seproject'
app.config['MYSQL_DATABASE_DB'] = 'IMS_DB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()


@app.route("/email_welcome/<user_name>/<email_id>")
def email_welcome(user_name,email_id):
	msg1 = Message('Welcome to IMS', sender = 'idea.management.system4@gmail.com', recipients = [email_id])
	msg1.html=(render_template('welcome.html',sending_mail=True,name= user_name))
	mail.send(msg1)
	return "sent"

@app.route("/email_post_problem/<g_id>/<g_name>")
def email_post_problem(g_id,g_name):
	list_emails = get_group_email_ids(cursor,g_id)
	msg1 = Message('IMS PROBLEM STATEMENT', sender = 'idea.management.system4@gmail.com', recipients = list_emails)
	msg1.html=(render_template('post_problem.html',group_name=g_name,sending_mail=True))
	mail.send(msg1)
	print(list_emails)
	return "sent" + ' '.join(list_emails)
@app.route("/email_event/<g_id>/<g_name>/<e_date>")
def email_event(g_id,g_name,e_date):
	list_emails = get_group_email_ids(cursor,g_id)
	msg1 = Message('IMS EVENT INVITE', sender = 'idea.management.system4@gmail.com', recipients = list_emails)
	msg1.html=(render_template('event_create.html',sending_mail=True,group_name=g_name,date=e_date))
	print(list_emails)
	mail.send(msg1)
	return "sent" + ' '.join(list_emails)
@app.route("/email_group/<g_id>/<g_name>")
def email_group(g_id,g_name):
	list_emails = get_group_email_ids(cursor,g_id)
	msg1 = Message('IMS GROUP INVITE', sender = 'idea.management.system4@gmail.com', recipients = list_emails)
	msg1.html=(render_template('group_create.html',group_name=g_name,sending_mail=True))
	mail.send(msg1)
	return "sent" + ' '.join(list_emails)

@app.route("/add_user/<g_name>/<email_id>")
def add_user(g_id,g_name,email_id):
	msg1 = Message('IMS GROUP INVITE', sender = 'idea.management.system4@gmail.com', recipients = [email_id])
	msg1.html=(render_template('group_create.html',group_name=g_name,sending_mail=True))
	mail.send(msg1)
	return "sent" + email_id

if __name__ == '__main__':
   app.run(debug = True,port=5002)



