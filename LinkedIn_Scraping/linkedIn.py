import requests
import os
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedInProfileURL: str, mock: bool):
    if mock:
        linkedin_profile_url = os.getenv('LINKEDIN_PROFILE_GIST_URL')
        response = requests.get(linkedin_profile_url)

    else:
        api_key = os.getenv('PROXY_CURL_API_KEY')
        headers = {'Authorization': 'Bearer ' + api_key}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        params = {
            # 'facebook_profile_url': 'https://www.facebook.com/31AKP',
            'linkedin_profile_url': linkedInProfileURL,
            'extra': 'include',
            'github_profile_id': 'include',
            'facebook_profile_id': 'include',
            'personal_contact_number': 'include',
            'personal_email': 'include',
            'inferred_salary': 'include',
            'skills': 'include',
            'use_cache': 'if-present',
            'fallback_to_cache': 'on-error',
        }
        response = requests.get(api_endpoint, params=params, headers=headers)

    data = response.json()
    finalDict = {}
    for k, v in data.items():
        if v not in ([], "", "", None):
            finalDict[k] = v
    return finalDict

if __name__ == "__main__":
    response = scrape_linkedin_profile('https://www.linkedin.com/in/arkapatra31/', True)
    #print(response)