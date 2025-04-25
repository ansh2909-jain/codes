import requests
from requests.auth import HTTPBasicAuth
 
base_url = 'http://127.0.0.1:8000'
username="Anmol"
password="anmol123j"
 
try:
    endpoint = '/'
    complete_url = base_url + endpoint  
    response = requests.get(complete_url, auth= HTTPBasicAuth(username, password), allow_redirects=True)
 
    print(f"Final URL after redirect: {response.url}")
    print(f"Status code: {response.status_code}")
 
    if response.status_code == 200:
        print("Redirect successful. Response content:")
        print(response.text)
    else:
        print(f"Unexpected status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error calling API: {e}")