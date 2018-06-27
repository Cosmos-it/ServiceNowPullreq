## Running on Python3, pip3 installation

Required items to run successful:
This can be found inside app.py

from flask import Flask, request, render_template
from flask import Flask, session, redirect, url_for, escape
import requests
import json

they don't exist,

use:
sudo pip3 install Flask
sudo pip3 install requests

everything else should be find.



To run the application 
This needs to be filled out first inside app.py under a comment section called 'CORE SERVICE'

username = '' # Add user name here
password = '' # Add password here
baselink = 'https://api.github.com/'
repoUrl = 'users/UserNameGooesHere/repos'

1. Make sure you have Python3 and Flask installed
2. Install using Pip3
3. To run the project,
    1. export FlASK_APP=app.py
    2. flask run (ignore any error you might see)
    3. then navigate to the link suggested: http://127.0.0.1:5000/

