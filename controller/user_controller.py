from app import app
from model.user_model import user_model
import json
from flask import request
obj = user_model()

@app.route("/user/signup")
def signup():
    return obj.user_signup_model()
@app.route("/user/signin")
def signin():
    return "this is signin operation"
@app.route("/users/all")
def fetchAllUsers():
    return obj.user_fetch_model()

@app.route("/users/add" , methods=["POST"])
def addUser_model():
    userData = request.form
    return obj.user_add_model(userData)

@app.route("/youtube" , methods=["POST"])
def download_youtube():
    url = request.form 
    obj.download_youtube_video_model(url)
    return {"data from user": url}
