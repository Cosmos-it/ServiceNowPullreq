from flask import Flask, request, render_template
from flask import Flask, session, redirect, url_for, escape
import requests
import json


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    repos_name = []
    if request.method == 'POST': 
        repo_name = request.form['data']
        return redirect(url_for('.repos_end_point', repo_name=repo_name))    
    for pulls in returnData():
        repos_name.append(pulls[u'name'])
    return render_template("index.html", data=repos_name)
 

@app.route('/api/repos/<repo_name>', methods = ['GET', 'POST'])
def repos_end_point(repo_name):       
    repo_name = repo_name
    repo_data = GetPullRequests(str(repo_name))
    print(repo_name)
    return render_template('details.html', data=repo_data)

@app.route('/user/')
@app.route('/user/<username>')
def hello(username=None):
    return render_template('index.html', username=username)


##-------------------------------- CORE SERVICES ----------------------------------------------

username = '' # Add user name here
password = '' # Add password here
baselink = 'https://api.github.com/'
repoUrl = 'users/UserNameGooesHere/repos'
pulls = 'ttps://api.github.com/repos/:owner/:repo/pulls?state=all'

collecionsName = [] # stores list of data for search and comparison.
collecionsTemp = [] # for testing
collectionObject = {} 

#### Things to do.
## 1. Show the list of repositories
## 2. Show the number of open Pull requests
## 3. Select repo by name and navigate that repository GitHub
## 4. The list should be sorted based on the number of pull requests.

def Auth():
    response = requests.get(baselink + 'users/' + username + '/repos', auth=(username,password))
    return response

def returnData():
    return Auth().json()

# Git pull regusts for individual repos
# Compare by name
def GetPullRequests(repo_name):
    data = {}
    for pulls in returnData():
        if repo_name == pulls[u'name']:
            # print(pulls)
            data['repo_name'] = repo_name
            data['pulls_url'] = pulls[u'pulls_url'].replace('{', '').replace('}', '').replace('number','').rstrip('/') + '?state=all'
            
            data['repo_link'] = pulls[u'svn_url']
            return data
        
    return False

    
    

