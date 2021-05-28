from django.shortcuts import render, HttpResponse
import json
import requests
import base64
from github import Github
from pprint import pprint

# Github username
username = "Kev00715"
# pygithub object
g = Github()
# get that user by username
user = g.get_user(username)



def get_repos(user):
    output = ""
    for repo in user.get_repos():
        # repository full name
        output = "\n".join((output, f"Full name: {repo.full_name}"))

        # repository description
        output = "\n".join((output, f"Description: {repo.description}"))

        # the date of when the repo was created
        output = "\n".join((output, f"Date created: {repo.created_at}"))

        # the date of the last git push
        output = "\n".join((output, f"Date of last push: {repo.pushed_at}"))

        # programming language
        output = "\n".join((output, f"Language: {repo.language}"))
        
        # number of forks
        output = "\n".join((output, f"Number of forks: {repo.forks}"))
        
        # number of stars
        output = "\n".join((output, f"Number of stars: {repo.stargazers_count}"))

        output_lf = ["\n", output]
        #minuses = ["-" for i in range(50)]
        #output_lf.extend(minuses)
        #output = "".join(output_lf)

        output = "\n".join((output, "Contents:"))
        for content in repo.get_contents(""):
            output = "\n".join((output, str(content)))
        
        try:
            # repo license
            output = "\n".join((output, f"License: {base64.b64decode(repo.get_license().content.encode()).decode()}"))
        except Exception:
            pass
        
        return output

print(get_repos(user))