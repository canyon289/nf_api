from github import Github
import ipdb
import pandas as pd
import re

# Get a personal access token from github
from p_token import personal_token

pattern = "Review vote:([\s,a-z, :, +, - ,👍,❤️,👎, 😕 ]*)\n"

# or using an access token
g = Github(personal_token)

repo = g.get_repo("OriolAbril/pymcon_reviews")
# repo = g.get_repo("canyon289/nf_api")
open_issues = repo.get_issues(state='open')



rows = []

for issue in open_issues:

    for comment in issue.get_comments():

        d = {} 
        d["title"] = issue.title
        d["issue_number"] = issue.number

        if comment.user.login not in ("canyon289"):
            d["reviewer"] = comment.user.login
            d["body"] = comment.body 
            vote = re.search(pattern, comment.body)

            if vote is not None:
                d["vote"] = vote.groups()[0].rstrip()
            else:
                d["vote"] = vote
            print(vote)

            rows.append(d)

df = pd.DataFrame(rows)
df.to_excel("Reviews.xlsx")
print("Review Counts")
print(df["title"].value_counts().sort_index())
