from django.http import response
from django.shortcuts import render, HttpResponse
import json
import requests
import base64
from github import Github
from pprint import pprint
import json

# Github username
username = "Kev00715"
username2 = "OE7DIO"
username3 = "xTzarol"
username4 = "edinkhauser"
username5 = "edinkhauser"
username6 = "Manuel-Faehndrich"

# pygithub object
g = Github("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")

# get that user by username
user = g.get_user(username)
user2 = g.get_user(username2)
user3 = g.get_user(username3)
user4 = g.get_user(username4)
user5 = g.get_user(username5)
user6 = g.get_user(username6)

def data_user(user):
    return f'-----Project Information for {user}-----'

def get_repos(user):
    output = ""
    for repo in user.get_repos():
        # repository full name
        output = "\n".join((output, f"Full name: {repo.full_name}"))
        
        # repository owner
        output = "\n".join((output, f"Owner: {repo.owner.name}"))

        # repository description
        output = "\n".join((output, f"Description: {repo.description}"))

        # the date of when the repo was created
        output = "\n".join((output, f"Date created: {repo.created_at}"))

        # the date of the last git push
        output = "\n".join((output, f"Date of last push: {repo.pushed_at}"))

        # programming language
        output = "\n".join((output, f"Language: {repo.language}"))

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

def index(request):
    project = requests.get('https://api.github.com/repos/Kev00715/GubitzerMiljakGithub')
    content = project.text
    return HttpResponse(content)

def home(request):
    return render(request, 'GithubReview/base.html')

def description(request):
    var = get_repos(user)
    var2 = get_repos(user2)
    var3 = get_repos(user3)
    var4 = get_repos(user4)
    var5 = get_repos(user5)
    var6 = get_repos(user6)
    name_project = data_user(username)
    name_project2 = data_user(username2)
    name_project3 = data_user(username3)
    name_project4 = data_user(username4)
    name_project5 = data_user(username5)
    name_project6 = data_user(username6)

    return render(request, 'GithubReview/description.html', {"github_kevin" : var, "name_project" : name_project, "github_stefan" : var2, "name_project2" : name_project2, "github_leo" : var3, "name_project3" : name_project3,
     "github_elias" : var4, "name_project4" : name_project4, "github_alexander" : var5, "name_project5" : name_project5, "github_michael" : var6, "name_project6" : name_project6})

'''
  - Links in Config-Datei machen (eigene Datei json Datei, die verknüpft werden soll)
  - user data ausgeben (wieviel pushs, namen - Projekt informationen als "drop-down" (wenn klicken, runterklappen))
  - Github Token
  - iframe für Infos
'''
 
def get_links():
    input_file = open('links.json')
    json_array = json.load(input_file)
    links_list = []
 
    for item in json_array:
        store_details = {"links":None}
        store_details['links'] = item['links']
        links_list.append(store_details)
 
    print(links_list)