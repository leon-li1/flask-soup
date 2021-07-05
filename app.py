from flask import Flask, render_template, request
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = request.args.get("name")
    return render_template("index.html", name=name) 
 
@app.route("/soup")
def beautiful_soup():
    html_doc = """<html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """
    soup = BeautifulSoup(html_doc, 'html.parser')
    return soup.prettify()
 