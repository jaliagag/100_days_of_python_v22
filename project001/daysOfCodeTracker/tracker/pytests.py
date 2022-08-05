#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
from github import Github
from pprint import pprint

# Create an API request 
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
#response = requests.get(url)
##print("Status code: ", response.status_code)
## In a variable, save the API response.
#response_dict = response.json()
## Evaluate the results.
##print(response_dict.keys())
## Find out more about the repositories.
#repos_dicts = response_dict['items']
#print("Repositories found:", len(repos_dicts))
## Examine the first repository.
#repo_dict = repos_dicts[0]
#print("\nThe following is some information regarding the first repository:")
#print('Name:', repo_dict['name'])  #print the project's name
#print('Owner:', repo_dict['owner']['login'])  #use the key owner and the the key login to get the dictionary describing the owner and the owner’s login name respectively.
#print('Stars:', repo_dict['stargazers_count'])  #print how many stars the project has earned
#print('Repository:', repo_dict['html_url'])  #print URL for the project’s GitHub repoitory
#print('Created:', repo_dict['created_at'])  #print when it was created
#print('Updated:', repo_dict['updated_at'])  #show when it was last updated
#print('Description:', repo_dict['description']) #print the repository’s Description

token = os.getenv('GITHUB_TOKEN')
g = Github(token)
repo = g.get_repo("jaliagag/100_days_of_python_v22")
branches = ['master', 'dev']
for i in branches:
    branch = repo.get_branch(branch=i)
    commit = repo.get_commit(sha=sha)
    print(commit)

