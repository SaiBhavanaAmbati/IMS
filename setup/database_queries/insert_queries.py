from flask import Flask, render_template
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash,check_password_hash
app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'seproject'
app.config['MYSQL_DATABASE_DB'] = 'IMS_DB1'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()


if __name__ == "__main__" :
	
	password = "admin123"
	hashed_password = generate_password_hash(password)
	cursor.execute("insert into Customer (customer_id, user_name,hashed_password, email_id, phone_no,company_name) values(NULL,\"Sanjay \",\""+ str(hashed_password) +"\",\"sanjay.yoshimitsu@gmail.com\",\"7829373542\", \"PESU\");")
	conn.commit()
	cursor.execute("insert into Customer (customer_id, user_name,hashed_password, email_id, phone_no,company_name) values(NULL,\"Shruthi S \",\""+ str(hashed_password) +"\",\"shruthi.shankar2512@gmail.com\",\"9686511872\", \"PESU\");")
	conn.commit()
	cursor.execute("insert into Customer (customer_id, user_name,hashed_password, email_id, phone_no,company_name) values(NULL,\"Sai Shashank \",\""+ str(hashed_password) +"\",\"sai.sasank.yadati@gmail.com\",\"8861219216\", \"PESU\");")
	conn.commit()
	cursor.execute("insert into Customer (customer_id, user_name,hashed_password, email_id, phone_no,company_name) values(NULL,\"RM Sourabh\",\""+ str(hashed_password) +"\",\"sourabhraja97@gmail.com\",\"9880125575\", \"PESU\");")
	conn.commit()
	cursor.execute("insert into Customer (customer_id, user_name,hashed_password, email_id, phone_no,company_name) values(NULL,\"Sandeep S\",\""+ str(hashed_password) +"\",\"sandeepsandy.pes@gmail.com\",\"9886943287\", \"PESU\");")
	conn.commit()
	cursor.execute("insert into Customer (customer_id, user_name,hashed_password, email_id, phone_no,company_name) values(NULL,\"Sanat B\",\""+ str(hashed_password) +"\",\"sanathbhimsen26@gmail.com\",\"9740091229\", \"PESU\");")
	conn.commit()
	cursor.execute("insert into Customer (customer_id, user_name,hashed_password, email_id, phone_no,company_name) values(NULL,\"Raghavendra H\",\""+ str(hashed_password) +"\",\"raghavendrahegde17@gmail.com\",\"9481159571\", \"PESU\");")
	conn.commit()
	cursor.execute("insert into Customer (customer_id, user_name,hashed_password, email_id, phone_no,company_name) values(NULL,\"Rekha R\",\""+ str(hashed_password) +"\",\"rekharenu2715@gmail.com\",\"9036360647\", \"PESU\");")
	conn.commit()
	cursor.execute("insert into Customer (customer_id, user_name,hashed_password, email_id, phone_no,company_name) values(NULL,\"Sameer S\",\""+ str(hashed_password) +"\",\"sam13kv@gmail.com\",\"9886943287\", \"PESU\");")
	conn.commit()
	cursor.execute("insert into Customer (customer_id, user_name,hashed_password, email_id, phone_no,company_name) values(NULL,\"Sanjuktha G\",\""+ str(hashed_password) +"\",\"sanjukthaps@gmail.com\",\"9964054600\", \"PESU\");")
	conn.commit()
	cursor.execute("insert into Customer (customer_id, user_name,hashed_password, email_id, phone_no,company_name) values(NULL,\"Sai Bhavana\",\""+ str(hashed_password) +"\",\"sai.bhavana.ambati@gmail.com\",\"9890243965\", \"PESU\");")
	conn.commit()


	

