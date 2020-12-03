# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 18:15:11 2020

@author: CH01MHL
"""


from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route("/", defaults={"js": "plain"})
@app.route("/<any(plain, jquery, fetch):js>")
def index(js):
    return render_template("{0}.html".format(js), js=js)


@app.route("/add", methods=["POST"])
def add():
    a = request.form.get("a", 0, type=float)
    b = request.form.get("b", 0, type=float)
    return jsonify(result=a + b)