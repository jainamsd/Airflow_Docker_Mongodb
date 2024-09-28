# Automation Project with MongoDB, Airflow, and Email Notification System

## Overview

This project provides an automation solution using MongoDB for configuration management, SMTP for email notifications, and Apache Airflow for orchestrating tasks. The project includes multiple Python modules to handle MongoDB operations, sending emails, and integrating these tasks into Airflow DAGs for automated execution.

---

## Project Structure

The project is divided into multiple components:

- **cloudmongo.py**: Handles MongoDB connection and queries.
- **emailhelper.py**: Sends email notifications using SMTP.
- **mongodbhelper.py**: A helper file that interacts with MongoDB, such as retrieving or inserting documents.
- **automationemailhelper.py**: Contains an Airflow DAG for sending emails.
- **bashoperatordemo.py**: Demonstrates Airflow’s BashOperator to run bash commands.
- **pyemaildag.py**: Contains another Airflow DAG that sends emails using Python.
- **pythonoperatordemo.py**: A Python DAG example that uses PythonOperator.
- **tutorial.py**: Follows a basic Airflow tutorial with templated tasks and dependencies.

---

## Dependencies

- **Python**: Ensure you have Python 3.x installed.
- **Pip packages**:
  - `pymongo`: For MongoDB operations
  - `smtplib`: For email notifications
  - `apache-airflow`: For task orchestration

---

## Getting Started

### Step 1: MongoDB Configuration

MongoDB is used to store configuration data. To connect to the MongoDB Atlas cluster, ensure you update the `DATABASE` and `PASSWORD` placeholders in the `pymongo.MongoClient` connection string found in `cloudmongo.py` and `mongodbhelper.py`.

```python
url = pymongo.MongoClient("mongodb+srv://<DATABASE>:<PASSWORD>@cluster0.mongodb.net/")
```
MongoDB is used to store configuration data. To connect to the MongoDB Atlas cluster, ensure you update the DATABASE and PASSWORD placeholders in the pymongo.MongoClient connection string found in cloudmongo.py and mongodbhelper.py.

```python
url = pymongo.MongoClient("mongodb+srv://<DATABASE>:<PASSWORD>@cluster0.mongodb.net/")
```
### Step 2: SMTP Email Configuration
To send emails, the emailhelper.py uses SMTP via Gmail. The get_single_document method fetches the username and password from the MongoDB collection.

Ensure you have an email configuration document in your MongoDB like the following:

```json

{
  "name": "email_config",
  "username": "your-email@gmail.com",
  "password": "your-email-password"
}
```
### Step 3: Airflow Setup
This project uses Airflow DAGs to automate sending emails and running bash commands. To run the DAGs:

Install Airflow by following the official installation guide.
After installation, place the DAG files (automationemailhelper.py, bashoperatordemo.py, etc.) in the Airflow DAGs directory (~/airflow/dags/).
Start the Airflow web server and scheduler:
```bash
airflow webserver --port 8080
airflow scheduler
```
### Step 4: Running the DAGs
After setting up Airflow, navigate to the Airflow UI (http://localhost:8080) and trigger the DAGs. Example DAGs provided in the project:

Automation Email Helper DAG (automationemailhelper.py): Sends emails automatically using the send_email Python callable.
Bash Operator Demo DAG (bashoperatordemo.py): Runs a bash command to print the current date.
Python Operator Demo DAG (pythonoperatordemo.py): Executes Python functions.
PyEmail DAG (pyemaildag.py): Another example to send emails using the Airflow Python operator.
Code Explanation
### cloudmongo.py
This script handles the MongoDB connection and retrieves data from the config collection.

```python

db = url["automation_config"]
collection = db["config"]
execute_query = collection.find({})
print("convert value----->" + str(list(execute_query)))
```
### emailhelper.py
The email helper sends email notifications using the Gmail SMTP server. It fetches the email credentials from MongoDB and sends an email to the recipient.

```python
config_data = get_single_document("config", {"name": "email_config"}, {"username": 1, "password": 1, "_id": 0})
x.login(config_data['username'], config_data['password'])
x.sendmail("sender", "receiver", message)
```
### mongodbhelper.py
This helper file contains utility functions for connecting to MongoDB, inserting documents, retrieving a single document, and updating documents.

get_connection(): Establishes a connection to MongoDB.
insert_single_document(): Inserts a single document into the specified collection.
get_single_document(): Retrieves a document based on a query.
update_single_document(): Updates a document.
Airflow DAGs
automationemailhelper.py:

Defines a DAG that sends emails using the send_email Python function.
```python

send_email = PythonOperator(
    task_id="send_email",
    python_callable=send
)
```

### bashoperatordemo.py:

Runs a Bash command to print the current date using Airflow's BashOperator.
```python

start_dag = BashOperator(
    task_id='start_dag',
    bash_command="date"
)
```
### pyemaildag.py:

Similar to automationemailhelper.py, this DAG sends emails using Airflow.
pythonoperatordemo.py:

Uses PythonOperator to call a Python function (call()) that returns a greeting.
tutorial.py:

A basic Airflow tutorial DAG that demonstrates dependencies between tasks and templated commands.
Usage
MongoDB Operations:

Ensure MongoDB Atlas credentials are correctly configured.
Add or update email configuration data in the config collection.
Email Notifications:

Set up Gmail SMTP and store email credentials in MongoDB.
Trigger the Airflow DAGs from the UI to send automated emails.

This README.md provides a detailed guide for setting up and running the project, explaining each component and how they work together.
