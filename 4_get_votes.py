from github import Github
import ipdb
import pandas as pd
import re

# Get a personal access token from github
from p_token import personal_token

numerical_conversion = {
                        # These are two different hearts even though they look the same
                        "❤":2,
                        "❤️":2,
                        ":heart:":-1,
                        "👍":1,
                        ":thumbsup:":-1,
                        "👎":-1,
                        ":thumbsdown:":-1,
                        "😕":-2,
                        ":frowning_face:":-2
                        }


pattern = "Review vote:([\s,a-z, :, +, - ,👍,❤️,👎, 😕, 1-9]*)\n"

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
                d["vote"] = vote.groups()[0].strip()
            else:
                d["vote"] = vote
            print(vote)

            rows.append(d)

long_df = pd.DataFrame(rows)

long_df["NumericalScale"] = long_df["vote"].replace(numerical_conversion)

# Replace emojis with numbers
writer = pd.ExcelWriter('Reviews.xlsx', engine='xlsxwriter')

long_df.to_excel(writer, sheet_name='long')
# df2.to_excel(writer, sheet_name='Sheet2')


writer.save()

print("Review Counts")
print(long_df["title"].value_counts().sort_index())
