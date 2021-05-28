from django.shortcuts import render, HttpResponse
import json
import requests
import base64
from github import Github
from pprint import pprint

# Create your views here.
def frontpage(request):
    return render(request, 'GithubReview/base.html')

def description(request):
    return render(request, 'GithubReview/description.html')

