from github import Github
import ipdb
import pandas as pd
import re

# Get a personal access token from github
from p_token import personal_token


# or using an access token
g = Github(personal_token)

repo = g.get_repo("numfocus/DISCOVER-Cookbook")
open_issues = repo.get_issues(state='open')



for issue in open_issues:
    # import ipdb
    # ipdb.set_trace()

    print(f"This is issue: {issue.title}")
    print(f"This is issue body: {issue.body}")
    for comment in issue.get_comments():
           print(f"This is the comment body {comment.body}")
           print("\n")
