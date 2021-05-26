from django.shortcuts import render, HttpResponse
import json
import requests

# Create your views here.
def frontpage(request):
    return render(request, 'GithubReview/base.html')

def index(request):
    project = requests.get('https://api.github.com/repos/Kev00715/GubitzerMiljakGithub')
    content = project.text
    return HttpResponse(content)

def description(request):
    return render(request, 'GithubReview/description.html')

