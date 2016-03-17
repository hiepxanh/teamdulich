from pymongo import MongoClient
from main import *
from bs4 import BeautifulSoup

client = MongoClient()
db =  client.demo
collection = db.my_collection
posts = db.posts

if __name__ == '__main__':
    url = "http://toidi.net/tag/quan-an-ngon/"
    file_name = "toidi_amthuc.html"
    download_webpage(url, file_name = "toidi_amthuc.html")
    open_file = open(file_name, "rb")
    identify= "post-4116"
    decoded_content = open_file.read().decode("utf-8")
    soup = BeautifulSoup (decoded_content, "html.parser")
    ret_cat_els = find_category (soup, "Ẩm Thực")

    i = 0
    post_contents = []
    while i < len(ret_cat_els):
        article_link = get_link_from_category_element(ret_cat_els[i]) #ret_cat_els[0] là doan code vơi tag "Am thuc" ma lay phan tu dau tien
        file_name="toidi_article_1.html"
        download_webpage(article_link, file_name="toidi_article_1.html")

        open_article_file = open(file_name,"rb")
        decoded_article_content = open_article_file.read().decode("utf-8")
        toidi_article = BeautifulSoup (decoded_article_content, "html.parser")
        title = get_post_title(toidi_article)
        post_content = get_content(toidi_article)
        first_img = get_image(toidi_article)
        post_dict = {
            "title" : title,
            "content" : post_content,
            "image" : first_img,
            "category": "duong pho"
        }
        post_contents.append(post_dict)
        i= i + 1
    # for post_content in post_contents:
    #     print(post_content)

#dic = {
#     "name": "fuma",
#    "likes": "100"
#}
#insert document
#posts.insert(dic)

#read

#for post in posts.find():
#    print (post)
posts.insert_many(post_contents)
for bai_viet in posts.find({"category":"duong pho"}):
    print(bai_viet['category'])
#next: can 1 template, trong template co <h1> {{post.title}}</h1>
#sau do render_template ("post.html", post = p.title) p la 1 class hoac object
#


###-----------------------------------HIEP GA CRAW AM THUC BON PHUONG -----------------------------------

if __name__ == '__main__':
    url = "http://toidi.net/tag/am-thuc-chau-a/"
    file_name = "toidi_amthuc_bonphuong.html"
    download_webpage(url, file_name = "toidi_amthuc_bonphuong.html")
    open_file = open(file_name, "rb")
    identify= "post-4316"
    decoded_content = open_file.read().decode("utf-8")
    soup = BeautifulSoup (decoded_content, "html.parser")
    ret_cat_els = find_category (soup, "Ẩm Thực")

    i = 0
    post_contents = []
    while i < len(ret_cat_els):
        article_link = get_link_from_category_element(ret_cat_els[i]) #ret_cat_els[0] là doan code vơi tag "Am thuc" ma lay phan tu dau tien
        file_name="toidi_article_1_bonphuong.html"
        download_webpage(article_link, file_name="toidi_article_1_bonphuong.html")

        open_article_file = open(file_name,"rb")
        decoded_article_content = open_article_file.read().decode("utf-8")
        toidi_article = BeautifulSoup (decoded_article_content, "html.parser")
        title = get_post_title(toidi_article)
        post_content = get_content(toidi_article)
        first_img = get_image(toidi_article)
        post_dict = {
            "title" : title,
            "content" : post_content,
            "image" : first_img,
            "category": "bon phuong"
        }
        post_contents.append(post_dict)
        i= i + 1

posts.insert_many(post_contents)
for bai_viet in posts.find({"category":"bon phuong"}):
    print(bai_viet['category'])


#---------------------------- Fuma coming -------------------------------

# -----------------------------------------------------------Blogdulich

if __name__ == '__main__':
    url = "http://toidi.net/am-thuc-2/page/3/"
    file_name = "toidi_amthuc_truyenthong.html"
    download_webpage(url, file_name = "toidi_amthuc_truyenthong.html")
    open_file = open(file_name, "rb")
    identify= "post-2963"
    decoded_content = open_file.read().decode("utf-8")
    soup = BeautifulSoup (decoded_content, "html.parser")
    ret_cat_els = find_category (soup, "Ẩm Thực")

    i = 0
    post_contents = []
    while i < len(ret_cat_els):
        article_link = get_link_from_category_element(ret_cat_els[i]) #ret_cat_els[0] là doan code vơi tag "Am thuc" ma lay phan tu dau tien
        file_name="toidi_article_1_truyenthong.html"
        download_webpage(article_link, file_name="toidi_article_1_truyenthong.html")

        open_article_file = open(file_name,"rb")
        decoded_article_content = open_article_file.read().decode("utf-8")
        toidi_article = BeautifulSoup (decoded_article_content, "html.parser")
        title = get_post_title(toidi_article)
        post_content = get_content(toidi_article)
        first_img = get_image(toidi_article)
        post_dict = {
            "title" : title,
            "content" : post_content,
            "image" : first_img,
            "category": "truyen thong"
        }
        post_contents.append(post_dict)
        i= i + 1

posts.insert_many(post_contents)
for bai_viet in posts.find({"category":"truyen thong"}):
    print(bai_viet['category'])















