import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from requests.auth import HTTPBasicAuth

# Sending a GET request to the URL
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Convert the JSON response to a Python list (or dictionary)
    posts = response.json()
    
    # Print the first 5 posts as an example
    for post in posts[:5]:
        print(f"Title: {post['title']}\nBody: {post['body']}\n")
else:
    print(f"Failed to fetch data: {response.status_code}")

# URL to post data (jsonplaceholder allows creating posts)
url = 'https://jsonplaceholder.typicode.com/posts'

# Data to send (usually comes in the form of a dictionary)
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Sending a POST request
response = requests.post(url, json=data)  # Use 'json' to send as JSON payload

# Checking if the request was successful
if response.status_code == 201:  # 201 is the status code for successful creation
    print("Post created successfully!")
    print(response.json())  # Print the response JSON (created post)
else:
    print(f"Failed to create post: {response.status_code}")
try:
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    response.raise_for_status()  # Check if the request was successful (status code 200)
    json_data = response.json()  # Automatically parses JSON
    print("Response from the first GET request:")
    print(json_data[:2])  # Print the first 2 posts for brevity
except requests.exceptions.RequestException as e:
    print(f"An error occurred during the first GET request: {e}")

headers = {'User-Agent': 'my-app'}
try:
    response = requests.get('https://jsonplaceholder.typicode.com/posts', headers=headers)
    response.raise_for_status()  # Raises an exception for 4xx/5xx responses
    print("\nResponse from the second GET request (with headers):")
    print(response.text[:200])  # Print first 200 characters of the response for brevity
except requests.exceptions.RequestException as e:
    print(f"An error occurred during the second GET request: {e}")

try:
    response = requests.get('https://jsonplaceholder.typicode.com/posts', timeout=5)  # 5-second timeout
    response.raise_for_status()  # Check if the request was successful
    print("\nResponse from the third GET request (with timeout):")
    print(response.text[:200])  # Print first 200 characters of the response for brevity
except requests.exceptions.Timeout:
    print("The request timed out during the third GET request.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred during the third GET request: {e}")

session = requests.Session()
retries = Retry(total=3, backoff_factor=0.5)
session.mount('http://', HTTPAdapter(max_retries=retries))

response = session.get('https://jsonplaceholder.typicode.com/posts')
print(response.text)

response = requests.get('https://httpbin.org/basic-auth/user/pass', auth=HTTPBasicAuth('user', 'pass'))
print(response.status_code)  # Should return 200 for successful authentication