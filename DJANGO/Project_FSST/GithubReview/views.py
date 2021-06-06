from django.http import response
from django.shortcuts import render, HttpResponse
import json
import requests
import base64
from github import Github
from pprint import pprint

# Github username
username = "Kev00715"
username2 = "xTzarol"
username3 = "OE7DIO"

# pygithub object
g = Github()
# get that user by username
user = g.get_user(username)
user2 = g.get_user(username3)
user3 = g.get_user(username2)

def data_user(user):
    return f'-----Project Information for {user}-----'

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


# Create your views here.
def frontpage(request):
    return render(request, 'GithubReview/base.html')

def description(request):
    var = get_repos(user)
    var2 = get_repos(user2)
    var3 = get_repos(user3)
    name_project = data_user(username)
    name_project2 = data_user(username3)
    name_project3 = data_user(username2)

    return render(request, 'GithubReview/description.html', {"github_kevin" : var, "name_project" : name_project, "github_paul" : var2, "name_project2" : name_project2, "github_leo" : var3, "name_project3" : name_project3})