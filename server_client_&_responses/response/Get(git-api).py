"""
request.get and plotly bar graph using git-api(application programming interface)
"""

import requests
# from plotly.graph_objs import Bar
from plotly import offline

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)       # requests.get() is used to get information from the web application.
print(f"Status code: {r.status_code}")
# print(f"Text: {r.text}")
print(r.raw)        # Prints the socket response from server.

'''
To save the content of the get response in a file.
'''
'''
with open('file1', 'wb') as fb:
    for chunk in r.iter_content(chunk_size=128):
        fb.write(chunk)
'''

response_dict = r.json()
print(response_dict.keys())
repo_dicts = response_dict['items']
print(f"Total no. of repo's: {response_dict['total_count']}")
print(f"Number of repo's returned: {len(repo_dicts)}")
repo_dic = repo_dicts[0]
key_list = ['id', 'name', 'owner', 'stargazers_count', 'html_url', 'description']

name, stars = [], []
for repo_dict in repo_dicts:
    print(f"No. of key's in ({repo_dict['id']}){repo_dict['name']} : {len(repo_dict.keys())}\n")
    for key, value in sorted(repo_dict.items()):
        name.append(repo_dict['name'])
        stars.append(repo_dict['stargazers_count'])
        if key in key_list:
            print(f"{key: <29} : {value}")
    print("\n\n")

data = [{
        'type': 'bar',
        'x': name,
        'y': stars
        }]

my_layout = {
            'title': "Most starred python repo's",
            'xaxis': {'title': 'Repository'},
            'yaxis': {'title': 'Stars_count'}
            }

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="../Python repo's.html")
