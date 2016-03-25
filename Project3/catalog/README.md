## Intro
This is an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## How to run it?
To run the application, simply use 
```
python apllication.py
```
It will run on 127.0.0.1:8000. If you wish to change IP or ports, please go to the application.py file and change it at the bottom part. There are some dependencies you might want to install:
- flask
- sqlalchemy
- oauth2client
- requests

## API End Point
There are currently two API end points, 
- /catalog.json
- /api/newItem

## Issues for flask version
Depending on the version of Flask you have, you may or may not be able to store a credentials object in the login_session the same way that Lorenzo does. You may get the following error:
```
OAuth2Credentials object is not JSON serializable
```
To fix this problem, update your versions of Flask by using the following commands:
```
pip install werkzeug==0.8.3
pip install flask==0.9
pip install Flask-Login==0.1.3
```
