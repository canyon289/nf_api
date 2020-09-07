"""
Post an issues

https://docs.github.com/en/rest/reference/issues#create-an-issue
"""
import requests
import json

from p_token import personal_token

username = "canyon289"
owner = username

repo = "nf_api"

data = {"title": "Issue Title",
        "body": "Issue body"}


gh_session = requests.Session()
gh_session.auth = (username, personal_token)

endpoint = f"https://api.github.com/repos/{owner}/{repo}/issues"

response = gh_session.post(endpoint, json.dumps(data))

print(response.status_code)
print(response.json())
