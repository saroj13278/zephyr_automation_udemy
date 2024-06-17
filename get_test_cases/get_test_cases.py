import requests
import json

def make_authenticated_request(api_url, bearer_token):
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Content-Type': 'application/json',  # Adjust content type if needed
    }
   

    try:
        response = requests.get(api_url, headers=headers)

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
api_url= 'https://api.zephyrscale.smartbear.com/v2/testcases?startAt=10&maxResults=10'


file_path = 'token.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the API token from the file
    bearer_token = file.read().strip()

make_authenticated_request(api_url, bearer_token)
