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
user2 = g.get_user(username2)
user3 = g.get_user(username3)

def print_repo(repo):
    # repository full name
    print("Full name:", repo.full_name)

    # repository description
    print("Description:", repo.description)

    # the date of when the repo was created
    print("Date created:", repo.created_at)

    # the date of the last git push
    print("Date of last push:", repo.pushed_at)

    # programming language
    print("Language:", repo.language)
    print("-"*50)

    # repository content (files & directories)
    print("Contents:")
    for content in repo.get_contents(""):
        print(content)

# iterate over all public repositories
for repo in user.get_repos():
    print_repo(repo)
    print("="*100)

for repo in user2.get_repos():
    print_repo(repo)
    print("="*100)

for repo in user3.get_repos():
    print_repo(repo)
    print("="*100)