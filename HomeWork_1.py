import requests
import json

user = 'Sergei729'
url = f'https://api.github.com/users/{user}/repos'

response = requests.get(url).json()

with open('repos_names.json', 'w') as file:
    json.dump(response, file)

for repo_name in response:
    print(repo_name['name'])
