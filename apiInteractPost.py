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
    url = "http://localhost:8000/alunos/"  # Replace with the actual URL
    username = "brenocarlo"  # Replace with your username
    password = "breno123"  # Replace with your password
    json_body = {
        "nome": "Breno",
        "rg": "444444444",
        "cpf": "14151554354",
        "data_nascimento": "2023-07-23"
    } 

    response_data = request(url, username, password, json_body)
    if response_data:
        return print("Response:", response_data)

