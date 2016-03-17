from flask import (Flask, render_template)
from pymongo import MongoClient

class Article:
    def __init__(self, _title, _content, _image):
        self.title = _title
        self.content = _content
        self.image = _image


app = Flask(__name__)

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

client = MongoClient()
db =  client.demo
collection = db.my_collection
posts = db.posts

a_list=[]
for post in posts.find({"category":"duong pho"}):
    a_list.append(Article(post["title"], post["content"], post ["image"]))

b_list=[]
for post in posts.find({"category":"truyen thong"}):
    b_list.append(Article(post["title"], post["content"], post ["image"]))

c_list=[]
for post in posts.find({"category":"bon phuong"}):
    c_list.append(Article(post["title"], post["content"], post ["image"]))


@app.route("/")
def index():
    return render_template("list.html", a_list=a_list)

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/duong_pho")
def duong_pho():
    return render_template("list.html", a_list=a_list)

@app.route("/truyen_thong")
def truyen_thong():
    return render_template("list.html", a_list=b_list)

@app.route("/bon_phuong")
def bon_phuong():
    return render_template("list.html", a_list = c_list)

@app.route('/article/<int:article_idx>')
def get_article_from_idx(article_idx ):
    #return str.format("you just query article {0}", article_idx)
    return render_template("file_post.html", Article = a_list[article_idx])

if __name__ == '__main__':
    app.run()

