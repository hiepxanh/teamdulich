from flask import (Flask, render_template)
from pymongo import MongoClient

class Article:
    def __init__(self, _title, _content, _id):
        self.title = _title
        self.content = _content
        self.id = _id

app = Flask(__name__)

client = MongoClient()
db =  client.demo
collection = db.my_collection
posts = db.posts

a_list=[]
for post in posts.find():
    a_list.append(Article(post["title"], post["content"], post["_id"]))


@app.route('/article/<int:article_idx>')
def get_article_from_idx(article_idx):
    #return str.format("you just query article {0}", article_idx)
    return render_template("file_post.html", Article = a_list[article_idx])



@app.route('/list')
def get_article_title():
    return render_template("article 2.html", a_list=a_list)


if __name__ == '__main__':
    app.run()

