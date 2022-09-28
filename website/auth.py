from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)



@auth.route("/signup")
def signup():
    return("<h1> soining up <h1>")

@auth.route("/logout")
def logut():
    return("<h1> loggin out <h1>")