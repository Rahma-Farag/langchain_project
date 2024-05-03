import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url, mock=False):
    """scrape information from linkedin profiles.
    Manually scrape the information from the linkedin profile"""
    if mock:
        response = requests.get(linkedin_profile_url)
        
    else:
        headers = {'Authorization': 'Bearer ' + os.environ.get('proxy_API_KEY')}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        params = {
            'url': linkedin_profile_url
        }
        response = requests.get(api_endpoint,
                                params=params,
                                headers=headers,
                                timeout=10)
    data = response.json()
    data = {k:v for k,v in data.items() if v not in ([], "","", None) and k not in ['people_also_viewed', 'certifications']}
    
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
            
    return data

if __name__ =='__main__':

    print(scrape_linkedin_profile(
        linkedin_profile_url= 'https://gist.githubusercontent.com/Rahma-Farag/2a933b5d3d08b366cce809c7d516be6b/raw/447399dab0b3bbc0c82c3404fe889079c9df9fdd/rahma-farag.json', 
        mock= True
    ))
    # print(
    #     scrape_linkedin_profile(
    #         linkedin_profile_url=r'https://www.linkedin.com/in/rahma-farag/'
    #     )
    # )
