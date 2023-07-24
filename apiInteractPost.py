#Bater no endpoint cadastrando os dados de um json
import requests
import base64
import json

def request(url, username, password, json_body):
    try:
        # Encode the username and password in base64
        auth_header = f"Basic {base64.b64encode(f'{username}:{password}'.encode()).decode()}"

        headers = {
            "Authorization": auth_header,
            "Content-Type": "application/json"
        }

        # Convert the JSON body to a string
        json_body_str = json.dumps(json_body)

        # Make the POST request
        response = requests.post(url, headers=headers, data=json_body_str)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            print("foi")
            return response.json()  # Assuming the response is in JSON format
        else:
            response.raise_for_status()  # Raise an exception if the request was not successful

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def apiInteractPost():
    #Insert in our three tables, hires, departments and jobs.
    hiredAPI()
    departmentsAPI()
    jobsAPI()
   
    

def hiredAPI():
    url = "http://localhost:8000/hired_employees/"  # Replace with the actual URL
    username = "brenocarlo"  # Replace with your username
    password = "breno123"  # Replace with your password
    json_body = {
        "id": "50",
        "name": "Hired Teste",
        "datetime": "2023-07-23",
        "department_id": "111",
        "job_id": "312"
    } 

    response_data = request(url, username, password, json_body)
    if response_data:
        return print("Response:", response_data)

def departmentsAPI():
    url = "http://localhost:8000/departments/"  # Replace with the actual URL
    username = "brenocarlo"  # Replace with your username
    password = "breno123"  # Replace with your password
    json_body = {
        "id": "92",
        "department": "Departmetns"
    } 

    response_data = request(url, username, password, json_body)
    if response_data:
        return print("Response:", response_data)

def jobsAPI():
    url = "http://localhost:8000/jobs/"  # Replace with the actual URL
    username = "brenocarlo"  # Replace with your username
    password = "breno123"  # Replace with your password
    json_body = {
        "id": "53",
        "job": "Job API Teste"
    } 

    response_data = request(url, username, password, json_body)
    if response_data:
        return print("Response:", response_data)