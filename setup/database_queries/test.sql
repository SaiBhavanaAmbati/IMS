CREATE DATABASE IF NOT EXISTS IMS_DB ;
USE IMS_DB ;

CREATE TABLE IF NOT EXISTS Customer (
    customer_id INT NOT NULL  AUTO_INCREMENT,
    user_name VARCHAR(60) NOT NULL,
    hashed_password VARCHAR(100) NOT NULL,
    email_id VARCHAR(30) NOT NULL,
    phone_no VARCHAR(15) NOT NULL,
    company_name VARCHAR(30) NOT NULL,
    PRIMARY KEY (customer_id));


CREATE TABLE IF NOT EXISTS Groups (
    g_id INT NOT NULL AUTO_INCREMENT ,
    PRIMARY KEY (g_id),
  group_name VARCHAR(30) NOT NULL,
company_name VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS Belongs_to (
    customer_id INT NOT NULL,
    g_id INT NOT NULL,
    role ENUM('manager','developer') NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id) ON DELETE CASCADE ,
FOREIGN KEY (g_id) REFERENCES Groups(g_id) ON DELETE CASCADE ,
PRIMARY KEY (customer_id,g_id)); 


CREATE TABLE IF NOT EXISTS Problem_statement (
    problem_id INT NOT NULL AUTO_INCREMENT ,
 g_id INT,
FOREIGN KEY (g_id) REFERENCES Groups(g_id) ON DELETE CASCADE,
STATEMENT TEXT,
Date_of_post DATE NOT NULL,
PRIMARY KEY (problem_id)
);
CREATE TABLE IF NOT EXISTS Ideas (
    idea_id INT NOT NULL AUTO_INCREMENT ,
 problem_id INT NOT NULL,
STATEMENT TEXT,
customer_id INT Not null,
Date_of_post DATE NOT NULL,
PRIMARY KEY (idea_id),
FOREIGN KEY (problem_id) REFERENCES Problem_statement(problem_id) ON DELETE CASCADE,
FOREIGN KEY (customer_id) REFERENCES Customer(customer_id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS comments(
    comment_id INT NOT NULL AUTO_INCREMENT ,
 idea_id INT Not null,
STATEMENT TEXT,
customer_id INT not null,
Date_of_post DATE NOT NULL,
PRIMARY KEY (comment_id),
FOREIGN KEY (idea_id) REFERENCES Ideas(idea_id) ON DELETE CASCADE,
FOREIGN KEY (customer_id) REFERENCES Customer(customer_id) ON DELETE cascade
);


CREATE TABLE IF NOT EXISTS Customer_vote (
customer_id INT not null,
 idea_id INT,
Vote ENUM('Up','Down'),
Date_of_post DATE NOT NULL,
PRIMARY KEY (customer_id,idea_id),
FOREIGN KEY (customer_id) REFERENCES Customer(customer_id) ON DELETE cascade ,
FOREIGN KEY (idea_id) REFERENCES Ideas(idea_id) ON DELETE CASCADE);


CREATE TABLE IF NOT EXISTS Events (
event_id INT NOT NULL AUTO_INCREMENT ,
Date_of_event DATE NOT NULL,
Name_of_event VARCHAR(20),
g_id INT not null,
FOREIGN KEY (g_id) REFERENCES Groups(g_id) ON DELETE CASCADE ,
PRIMARY KEY(event_id)
);

