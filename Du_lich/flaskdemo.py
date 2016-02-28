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
for post in posts.find():
    a_list.append(Article(post["title"], post["content"], post ["image"]))

@app.route('/article/<int:article_idx>')
def get_article_from_idx(article_idx ):
    #return str.format("you just query article {0}", article_idx)
    return render_template("file_post.html", Article = a_list[article_idx])




@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/nohome")
# def home():
#     return render_template("tes.html")

@app.route("/list")
def new():
    return render_template("list.html", a_list=a_list)

if __name__ == '__main__':
    app.run()

