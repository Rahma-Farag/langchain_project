import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = 'YOUR_API_KEY'
headers = {'Authorization': 'Bearer ' + os.environ['proxy_API_KEY']}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
params = {
    'url': 'https://www.linkedin.com/in/rahma-farag/'
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=headers)

print(response.json())
print("***********")
print(response._content)