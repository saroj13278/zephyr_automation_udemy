import requests
import json

def make_authenticated_request(api_url, bearer_token):
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Content-Type': 'application/json',  # Adjust content type if needed
    }
    payload = {
  "issueId": 10047
    }


    try:
        response = requests.post(api_url, headers=headers, json=payload)

        # Check if the request was successful (status code 201)
        if response.status_code == 201:
            print("Request successful. Response:")
            print(response.json())
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Replace 'YOUR_API_URL' with the actual API endpoint you want to access
api_url = 'https://api.zephyrscale.smartbear.com/v2/testcases/DEV-T117/links/issues'

file_path = 'token.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the API token from the file
    bearer_token = file.read().strip()

make_authenticated_request(api_url, bearer_token)
