import requests
import json

def make_authenticated_request(api_url, bearer_token):
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Content-Type': 'application/json',  # Adjust content type if needed
    }
    payload = {
        "id" : 165097785,
        "projectKey": "DEV",
        "name": "Check axial pump1",
        "key": "DEV-T119",
        "objective": "To ensure the axial pump can be enabled",
                  
        "folderId": 14808425,
        "priority": {'id': 4614911, 'self': 'https://api.zephyrscale.smartbear.com/v2/priorities/4614911'},
        "status": {'id': 4614908, 'self': 'https://api.zephyrscale.smartbear.com/v2/statuses/4614908'},
        "project":  {'id': 254590, 'self': 'https://api.zephyrscale.smartbear.com/v2/projects/254590'},
        
        "customFields": {
            "Build Number": 20.0,
            "test type": None,
        },
    }

    try:
        response = requests.put(api_url, headers=headers, json=payload)

        # Check if the request was successful (status code 201)
        if response.status_code == 200:
            print("Request successful. Response:")
            print(response.json())
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Replace 'YOUR_API_URL' with the actual API endpoint you want to access
#api_url = 'https://api.zephyrscale.smartbear.com/v2/testcases'
api_url = 'https://api.zephyrscale.smartbear.com/v2/testcases/DEV-T119'

file_path = 'token.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the API token from the file
    bearer_token = file.read().strip()

make_authenticated_request(api_url, bearer_token)
