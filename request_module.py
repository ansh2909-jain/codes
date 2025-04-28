import requests
 
def make_request(method, endpoint, base_url, headers=None, payload={}, auth=None):
    try:
        complete_url = base_url + endpoint
 
        if method == 'GET':
            if headers:
                response = requests.get(complete_url, headers=headers, allow_redirects=True)
            else:
                response = requests.get(complete_url, auth=auth, allow_redirects=True)
        elif method == 'POST':
            if headers:
                response = requests.post(complete_url, headers=headers, data=payload, allow_redirects=True)
            response = requests.post(complete_url, auth=auth, data=payload, allow_redirects=True)
        elif method == 'DELETE':
            if headers:
                response = requests.delete(complete_url, headers=headers, allow_redirects=True)
            response = requests.delete(complete_url, auth=auth, allow_redirects=True)
        else:
            print(f"!!!Wrong HTTP method!!!: {method.upper()}")
            return None, None
 
        print(f"Final URL after redirect: {response.url}")
        print(f"Status code: {response.status_code}")
 
        if response.status_code == 200:
            print("Request successful. Response content:")
            return response.status_code, response.text
        else:
            print(f"Unexpected status code: {response.status_code}")
            return response.status_code, response.text
 
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")