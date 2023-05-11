from flask import render_template, request, redirect

def index():
    return render_template('/recipes/index.html')