from django.http import response
from django.shortcuts import render, HttpResponse
import json
import requests
import base64
import os.path
from github import Github
from pprint import pprint
import json

# pygithub object
g = Github()

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
        #output = "\n".join((output, f"Number of forks: {repo.forks}"))
        
        # number of stars
        #output = "\n".join((output, f"Number of stars: {repo.stargazers_count}"))

        output_lf = ["\n", output]
        #minuses = ["-" for i in range(50)]
        #output_lf.extend(minuses)
        #output = "".join(output_lf)

        output = "\n".join((output, "Contents:"))
        for content in repo.get_contents(""):
            output = "\n".join((output, str(content)))
        
        # try:
        #     # repo license
        #     output = "\n".join((output, f"License: {base64.b64decode(repo.get_license().content.encode()).decode()}"))
        # except Exception:
        #     pass
        
        return output

def projectlist_htmlwrapper(urls, users):
    output = ""

    for url, user in zip(urls, users):
        formatted_link = f"<a href=\"{url}\" target=\"_blank\">{user}</a>"
        output = "\n".join((output, formatted_link))
    
    return output

def repoview_htmwrapper(users):
    output = ""

    for user in users:
        github_user = g.get_user(user)
        output = "\n".join((output, data_user(user), get_repos(github_user)))
    
    return output

# Create your views here.
def frontpage(request):
    return home(request)

def index(request):
    project = requests.get('https://api.github.com/repos/Kev00715/GubitzerMiljakGithub')
    content = project.text
    return HttpResponse(content)

def home(request):
    with open(os.path.join(os.path.dirname(__file__), "links.json"), "r") as file:
        json_links = json.load(file)[0]
    
    links = json_links["links"]
    users = json_links["user"]

    menu = projectlist_htmlwrapper(links, users)

    return render(request, 'GithubReview/base.html', {"links" : menu})

def description(request):
    with open(os.path.join(os.path.dirname(__file__), "links.json"), "r") as file:
        json_links = json.load(file)[0]
    
    links = json_links["links"]
    users = json_links["user"]
    github_users = json_links["github_users"]

    menu = projectlist_htmlwrapper(links, users)
    repos = repoview_htmwrapper(github_users)
    


    return render(request, 'GithubReview/description.html', {"links" : menu, "project_information" : repos})

'''
  - Links in Config-Datei machen (eigene Datei json Datei, die verknüpft werden soll)
  - user data ausgeben (wieviel pushs, namen - Projekt informationen als "drop-down" (wenn klicken, runterklappen))
  - Github Token
  - iframe für Infos
'''