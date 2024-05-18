# Tango  
  
## What is Tango  
  
Tango is a lightweight framework for building chatbots with Django, specifically for integrating them with RAG Chain architectures or to talk directly with Large Language Models. The goal is to be able to provide a basic foundation for building chatbots outside the more managed bot framework or managed web app-based offerings.  
  
## How to Set Up  
  
### Requirements  
  
- Python 3.7+  
- Databricks Account  
- Databricks Personal Access Token  
  
1. Create an `.env` file with the following structure and values filled out:  
```
DATABRICKS_TOKEN=enter_token_value_here
DATABRICKS_URL=https://<databricks_deployment_name>.cloud.databricks.com/serving-endpoints
DJANGO_SECRET=make_up_a_secret_value
```  
2. Install the necessary libraries `pip3 install -r requirements.txt`  
3. Instantiate the models for Django:  
    - `python3 manage.py makemigrations`
    - `python3 manage.py migrate`  
4. Run the Django server:  
    - `python3 manage.py runserver`  
5. Navigate to `http://127.0.0.1:8000/chat/`  