from threading import Thread, Condition
import time
import os

queue = []
MAX_NUM = 10
condition = Condition()
command = "curl "
server_addr = "http://localhost:5002/"
email_functions = ["email_welcome","email_post_problem","email_event","email_group"]
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

my_thread_0 = ProducerThread((0,"bhavana","sai.bhavana.ambati@gmail.com"))

my_thread_0.start()

my_thread_1 = ProducerThread((1,"1","USP_FUSE"))

my_thread_1.start()

my_thread_2= ProducerThread((2,"1","USP_FUSE","2018-09-09"))

my_thread_2.start()

my_thread_3 = ProducerThread((3,"1","USP_FUSE"))

my_thread_3.start()

ConsumerThread().start()
