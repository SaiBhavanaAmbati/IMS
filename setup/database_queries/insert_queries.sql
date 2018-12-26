USE IMS_DB1;
insert into Groups (g_id,group_name,company_name) values (NULL,'USP_FUSE', 'PESU');
insert into Groups (g_id,group_name,company_name) values (NULL,'JAVASCRIPT_COMPILER', 'PESU');
insert into Groups (g_id,group_name,company_name) values (NULL,'UNIX_TERMINAL', 'PESU');
insert into Groups (g_id,group_name,company_name) values (NULL,'ML_ASL_DETECTION', 'PESU');
insert into Groups (g_id,group_name,company_name) values (NULL,'GREEN_INDEX', 'PESU');
insert into Groups (g_id,group_name,company_name) values (NULL,'SE_IMS', 'PESU');
insert into Groups (g_id,group_name,company_name) values (NULL,'CLOUD_HBASE', 'PESU');
insert into Groups (g_id,group_name,company_name) values (NULL,'RESTAURANT_MS', 'PESU');
insert into Groups (g_id,group_name,company_name) values (NULL,'NFA_TO_DFA', 'PESU');
insert into Groups (g_id,group_name,company_name) values (NULL,'NL_TO_LINUX', 'PESU');

insert into Belongs_to (customer_id,g_id,role) values (1,1,'manager');
insert into Belongs_to (customer_id,g_id,role) values (2,1,'developer');
insert into Belongs_to (customer_id,g_id,role) values (3,1,'developer');
insert into Belongs_to (customer_id,g_id,role) values (4,1,'developer');
insert into Belongs_to (customer_id,g_id,role) values (5,1,'developer');
insert into Belongs_to (customer_id,g_id,role) values (6,2,'manager');
insert into Belongs_to (customer_id,g_id,role) values (7,2,'developer');
insert into Belongs_to (customer_id,g_id,role) values (8,2,'developer');
insert into Belongs_to (customer_id,g_id,role) values (9,2,'developer');
insert into Belongs_to (customer_id,g_id,role) values (10,2,'developer');


insert into Belongs_to (customer_id,g_id,role) values (1,3,'manager');
insert into Belongs_to (customer_id,g_id,role) values (2,3,'developer');
insert into Belongs_to (customer_id,g_id,role) values (3,3,'developer');
insert into Belongs_to (customer_id,g_id,role) values (4,3,'developer');
insert into Belongs_to (customer_id,g_id,role) values (5,3,'developer');
insert into Belongs_to (customer_id,g_id,role) values (6,4,'manager');
insert into Belongs_to (customer_id,g_id,role) values (7,4,'developer');
insert into Belongs_to (customer_id,g_id,role) values (8,4,'developer');
insert into Belongs_to (customer_id,g_id,role) values (9,4,'developer');
insert into Belongs_to (customer_id,g_id,role) values (10,4,'developer');
insert into Belongs_to (customer_id,g_id,role) values (1,5,'developer');
insert into Belongs_to (customer_id,g_id,role) values (2,5,'manager');
insert into Belongs_to (customer_id,g_id,role) values (3,5,'developer');
insert into Belongs_to (customer_id,g_id,role) values (4,5,'developer');
insert into Belongs_to (customer_id,g_id,role) values (5,5,'developer');
insert into Belongs_to (customer_id,g_id,role) values (6,6,'developer');
insert into Belongs_to (customer_id,g_id,role) values (7,6,'manager');
insert into Belongs_to (customer_id,g_id,role) values (8,6,'developer');
insert into Belongs_to (customer_id,g_id,role) values (9,6,'developer');
insert into Belongs_to (customer_id,g_id,role) values (10,6,'developer');
insert into Belongs_to (customer_id,g_id,role) values (1,7,'developer');
insert into Belongs_to (customer_id,g_id,role) values (2,7,'manager');
insert into Belongs_to (customer_id,g_id,role) values (3,7,'developer');
insert into Belongs_to (customer_id,g_id,role) values (4,7,'developer');
insert into Belongs_to (customer_id,g_id,role) values (5,7,'developer');
insert into Belongs_to (customer_id,g_id,role) values (6,8,'developer');
insert into Belongs_to (customer_id,g_id,role) values (7,8,'manager');
insert into Belongs_to (customer_id,g_id,role) values (8,8,'developer');
insert into Belongs_to (customer_id,g_id,role) values (9,8,'developer');
insert into Belongs_to (customer_id,g_id,role) values (10,8,'developer');

insert into Belongs_to (customer_id,g_id,role) values (1,2,'developer');
insert into Belongs_to (customer_id,g_id,role) values (2,2,'developer');
insert into Belongs_to (customer_id,g_id,role) values (3,2,'developer');
insert into Belongs_to (customer_id,g_id,role) values (4,2,'developer');
insert into Belongs_to (customer_id,g_id,role) values (5,2,'developer');
insert into Belongs_to (customer_id,g_id,role) values (6,1,'developer');
insert into Belongs_to (customer_id,g_id,role) values (7,1,'developer');
insert into Belongs_to (customer_id,g_id,role) values (8,1,'developer');
insert into Belongs_to (customer_id,g_id,role) values (9,1,'developer');
insert into Belongs_to (customer_id,g_id,role) values (10,1,'developer');

insert into Belongs_to (customer_id,g_id,role) values (1,3,'Manager');
insert into Belongs_to (customer_id,g_id,role) values (2,3,'developer');
insert into Belongs_to (customer_id,g_id,role) values (3,3,'developer');
insert into Belongs_to (customer_id,g_id,role) values (4,3,'developer');
insert into Belongs_to (customer_id,g_id,role) values (5,3,'developer');
insert into Belongs_to (customer_id,g_id,role) values (6,3,'developer');
insert into Belongs_to (customer_id,g_id,role) values (7,3,'developer');
insert into Belongs_to (customer_id,g_id,role) values (8,3,'developer');
insert into Belongs_to (customer_id,g_id,role) values (9,3,'developer');
insert into Belongs_to (customer_id,g_id,role) values (10,3,'developer');

insert into Belongs_to (customer_id,g_id,role) values (1,4,'Manager');
insert into Belongs_to (customer_id,g_id,role) values (2,4,'developer');
insert into Belongs_to (customer_id,g_id,role) values (3,4,'developer');
insert into Belongs_to (customer_id,g_id,role) values (4,4,'developer');
insert into Belongs_to (customer_id,g_id,role) values (5,4,'developer');
insert into Belongs_to (customer_id,g_id,role) values (6,4,'developer');
insert into Belongs_to (customer_id,g_id,role) values (7,4,'developer');
insert into Belongs_to (customer_id,g_id,role) values (8,4,'developer');
insert into Belongs_to (customer_id,g_id,role) values (9,4,'developer');
insert into Belongs_to (customer_id,g_id,role) values (10,4,'developer');

insert into Belongs_to (customer_id,g_id,role) values (1,5,'Manager');
insert into Belongs_to (customer_id,g_id,role) values (2,5,'developer');
insert into Belongs_to (customer_id,g_id,role) values (3,5,'developer');
insert into Belongs_to (customer_id,g_id,role) values (4,5,'developer');
insert into Belongs_to (customer_id,g_id,role) values (5,5,'developer');
insert into Belongs_to (customer_id,g_id,role) values (6,5,'developer');
insert into Belongs_to (customer_id,g_id,role) values (7,5,'developer');
insert into Belongs_to (customer_id,g_id,role) values (8,5,'developer');
insert into Belongs_to (customer_id,g_id,role) values (9,5,'developer');
insert into Belongs_to (customer_id,g_id,role) values (10,5,'developer');

insert into Belongs_to (customer_id,g_id,role) values (1,6,'developer');
insert into Belongs_to (customer_id,g_id,role) values (2,6,'Manager');
insert into Belongs_to (customer_id,g_id,role) values (3,6,'developer');
insert into Belongs_to (customer_id,g_id,role) values (4,6,'developer');
insert into Belongs_to (customer_id,g_id,role) values (5,6,'developer');
insert into Belongs_to (customer_id,g_id,role) values (6,6,'developer');
insert into Belongs_to (customer_id,g_id,role) values (7,6,'developer');
insert into Belongs_to (customer_id,g_id,role) values (8,6,'developer');
insert into Belongs_to (customer_id,g_id,role) values (9,6,'developer');
insert into Belongs_to (customer_id,g_id,role) values (10,6,'developer');

insert into Belongs_to (customer_id,g_id,role) values (1,7,'developer');
insert into Belongs_to (customer_id,g_id,role) values (2,7,'Manager');
insert into Belongs_to (customer_id,g_id,role) values (3,7,'developer');
insert into Belongs_to (customer_id,g_id,role) values (4,7,'developer');
insert into Belongs_to (customer_id,g_id,role) values (5,7,'developer');
insert into Belongs_to (customer_id,g_id,role) values (6,7,'developer');
insert into Belongs_to (customer_id,g_id,role) values (7,7,'developer');
insert into Belongs_to (customer_id,g_id,role) values (8,7,'developer');
insert into Belongs_to (customer_id,g_id,role) values (9,7,'developer');
insert into Belongs_to (customer_id,g_id,role) values (10,7,'developer');

insert into Belongs_to (customer_id,g_id,role) values (1,8,'developer');
insert into Belongs_to (customer_id,g_id,role) values (2,8,'Manager');
insert into Belongs_to (customer_id,g_id,role) values (3,8,'developer');
insert into Belongs_to (customer_id,g_id,role) values (4,8,'developer');
insert into Belongs_to (customer_id,g_id,role) values (5,8,'developer');
insert into Belongs_to (customer_id,g_id,role) values (6,8,'developer');
insert into Belongs_to (customer_id,g_id,role) values (7,8,'developer');
insert into Belongs_to (customer_id,g_id,role) values (8,8,'developer');
insert into Belongs_to (customer_id,g_id,role) values (9,8,'developer');
insert into Belongs_to (customer_id,g_id,role) values (10,8,'developer');


insert into Problem_statement( problem_id, g_id ,STATEMENT,Date_of_post ) values (NULL, 1, 'Implementing directory structure, read,write, mkdir and rmdir using FUSE','2018-01-07');
insert into Problem_statement( problem_id, g_id ,STATEMENT,Date_of_post ) values (NULL, 1, 'Implementing Block structure in FUSE','2018-02-09');
insert into Problem_statement( problem_id, g_id ,STATEMENT,Date_of_post ) values (NULL, 1, 'Implementing Persistence in FUSE','2018-03-05');
insert into Problem_statement( problem_id, g_id ,STATEMENT,Date_of_post ) values (NULL, 4,'Choosing classification model ','2018-03-10');
insert into Problem_statement( problem_id, g_id ,STATEMENT,Date_of_post ) values (NULL, 4,'Developing Front-End for the input','2018-04-10');
insert into Problem_statement( problem_id, g_id ,STATEMENT,Date_of_post ) values (NULL, 3,'Implementing simple commands','2018-03-10');
insert into Problem_statement( problem_id, g_id ,STATEMENT,Date_of_post ) values (NULL, 3,'Implementing complex piping commands','2018-01-10');
insert into Problem_statement( problem_id, g_id ,STATEMENT,Date_of_post ) values (NULL, 3,'Implementing complex piping commands' , '2018-02-12');
insert into Problem_statement( problem_id, g_id ,STATEMENT,Date_of_post ) values (NULL, 3,'Implementing new customized piping commands' , '2018-03-14');

insert into Events (event_id,Date_of_event,Name_of_event,g_id) values (Null,'2018-03-12','feasibility study',4);
insert into Events (event_id,Date_of_event,Name_of_event,g_id) values (Null,'2018-03-15','requirements study',4);
insert into Events (event_id,Date_of_event,Name_of_event,g_id) values (Null,'2018-03-18','project plan',4);
insert into Events (event_id,Date_of_event,Name_of_event,g_id) values (Null,'2018-03-21','design',4);  
insert into Events (event_id,Date_of_event,Name_of_event,g_id) values (Null,'2018-04-01','implementation',4);    
insert into Events (event_id,Date_of_event,Name_of_event,g_id) values (Null,'2018-04-09','test and deploy',4);
insert into Events (event_id,Date_of_event,Name_of_event,g_id) values (Null,'2018-01-12','feasibility study',3);
insert into Events (event_id,Date_of_event,Name_of_event,g_id) values (Null,'2018-01-15','requirements study',3);
insert into Events (event_id,Date_of_event,Name_of_event,g_id) values (Null,'2018-01-18','project plan',3);
insert into Events (event_id,Date_of_event,Name_of_event,g_id) values (Null,'2018-01-21','design',3);  
insert into Events (event_id,Date_of_event,Name_of_event,g_id) values (Null,'2018-02-01','implementation',3);    
insert into Events (event_id,Date_of_event,Name_of_event,g_id) values (Null,'2018-02-09','test and deploy',3);
insert into Events (event_id,Date_of_event,Name_of_event,g_id) values (Null,'2018-01-12','feasibility study',1);
insert into Events (event_id,Date_of_event,Name_of_event,g_id) values (Null,'2018-01-15','requirements study',1);
insert into Events (event_id,Date_of_event,Name_of_event,g_id) values (Null,'2018-01-18','project plan',1);
insert into Events (event_id,Date_of_event,Name_of_event,g_id) values (Null,'2018-01-21','design',1);  
insert into Events (event_id,Date_of_event,Name_of_event,g_id) values (Null,'2018-02-01','implementation',1);    
insert into Events (event_id,Date_of_event,Name_of_event,g_id) values (Null,'2018-02-09','test and deploy',1);


insert into Ideas (idea_id ,problem_id,STATEMENT,customer_id ,Date_of_post) values (Null, 1, 'The directory structure should be implemented as an array to make the design and operations simple, and make persistence easier',4,'2018-01-10');
insert into Ideas (idea_id ,problem_id,STATEMENT,customer_id ,Date_of_post) values (Null, 1, 'The directory structure should be implemented as a B-tree to increase optimization of searching for files',6,'2018-01-10');
insert into Ideas (idea_id ,problem_id,STATEMENT,customer_id ,Date_of_post) values (Null, 2, 'The block structure should be implemented as an array, the inode of the file stores the index of the first block, each block stores the index of the next block of the file and the last block stores the index as -1',4,'2018-02-10');
insert into Ideas (idea_id ,problem_id,STATEMENT,customer_id ,Date_of_post) values (Null, 2, 'The block structure should be implemented as a linked list, the inode of the file stores the address of the head of the linked list',6,'2018-02-10');
insert into Ideas (idea_id ,problem_id,STATEMENT,customer_id ,Date_of_post) values (Null, 2, 'The block structure should be implemented as an array, the inode of the file stores an array of all indexes of blocks',7,'2018-02-10');
insert into Ideas (idea_id ,problem_id,STATEMENT,customer_id ,Date_of_post) values (Null, 4, 'We should use CNN with few layers to implement the model because it is a very powerful neural network',10,'2018-03-10');
insert into Ideas (idea_id ,problem_id,STATEMENT,customer_id ,Date_of_post) values (Null, 4, 'We should use SVM after PCA because it is a very powerful and optimized model',11,'2018-03-10');
insert into Ideas (idea_id ,problem_id,STATEMENT,customer_id ,Date_of_post) values (Null, 4, 'We should use Ada boosting after PCA because it boosts performance of weak classifiers and thus is very powerful',12,'2018-03-10');

insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (1,1,'Up','2018-01-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (1,2,'Down','2018-01-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (1,3,'Up','2018-02-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (1,4,'Down','2018-02-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (1,5,'Up','2018-02-10');

insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (2,1,'Up','2018-01-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (2,2,'Down','2018-01-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (2,3,'Up','2018-02-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (2,4,'Up','2018-02-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (2,5,'Down','2018-02-10');

insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (3,1,'Up','2018-01-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (3,2,'Down','2018-01-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (3,3,'Up','2018-02-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (3,4,'Up','2018-02-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (3,5,'Down','2018-02-10');

insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (4,1,'Down','2018-01-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (4,2,'Up','2018-01-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (4,3,'Down','2018-02-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (4,4,'Up','2018-02-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (4,5,'Down','2018-02-10');





insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (5,1,'Down','2018-01-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (5,2,'Up','2018-01-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (5,3,'Up','2018-02-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (5,4,'Down','2018-02-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (5,5,'Up','2018-02-10');

insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (6,1,'Up','2018-01-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (6,2,'Down','2018-01-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (6,3,'Up','2018-02-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (6,4,'Down','2018-02-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (6,5,'Up','2018-02-10');

insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (7,1,'Down','2018-01-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (7,2,'Up','2018-01-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (7,3,'Up','2018-02-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (7,4,'Up','2018-02-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (7,5,'Down','2018-02-10');

insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (8,1,'Up','2018-01-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (8,2,'Down','2018-01-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (8,3,'Down','2018-02-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (8,4,'Up','2018-02-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (8,5,'Up','2018-02-10');


insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (9,1,'Up','2018-01-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (9,2,'Down','2018-01-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (9,3,'Up','2018-02-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (9,4,'Down','2018-02-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (9,5,'Up','2018-02-10');

insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (10,1,'Down','2018-01-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (10,2,'Up','2018-01-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (10,3,'Down','2018-02-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (10,4,'Up','2018-02-10');
insert into Customer_vote (customer_id,idea_id,Vote,Date_of_post) values (10,5,'Down','2018-02-10');


