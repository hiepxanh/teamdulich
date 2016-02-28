import urllib3
from bs4 import BeautifulSoup
import re

def download_webpage(url, file_name = "data.html"):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    file = open(file_name,'wb')
    file.write(r.data)
    file.close()

#---------------------------------------Toidi.net

def find_category(bs, category):
    found_elements = bs.find_all('a', rel = "category tag", string = "Ẩm Thực")
    if len(found_elements) > 0:
        return found_elements
    return None

def get_link_from_category_element(cat_el):
    top_parent = cat_el.parent.parent.parent
    a_book_mark = top_parent.find('a', rel="bookmark")
    return a_book_mark['href']

def get_post_title (bs):
    post_title = bs.find('h1', {"class" : "post-title"})
    #return post_title.string
    return post_title.string

def get_content(bs):
    whole_post = bs.find_all('div', {"class" : "entry-inner"})
    post_content = ""
    if len(whole_post)>0:
        element = whole_post[0]
        for child in element.children:
            if child.string != "Bài viết hay liên quan":
                post_content += str(child).replace('\n','')
            else:
                break
    return post_content

def get_image(bs): # chi lay cai anh thu 2
    i = 0
    for link in bs.find_all('img'):
        #print (link.get('src'))
        if i == 1:
            #print (link.get('src'))
            return link.get('src')
        else:
            None
        i += 1

if __name__ == '__main__':
    url = "http://toidi.net/tag/quan-an-ngon/"
    file_name = "toidi_amthuc.html"
    #download_webpage(url, file_name = "toidi_amthuc.html")
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
        first_img = get_image (toidi_article)
        post_dict = {
            "title" : title,
            "content" : post_content,
            "image" : first_img,
            "category": "duong pho"
        }
        post_contents.append(post_dict)
        i= i + 1
    for post_content in post_contents:
        print(post_content)


# -----------------------------------------------------------Blogdulich
def find_box_post_title(bs,post):
    found_elements_2=bs.find_all('h2', {"class" :"post-box-title" })
    if len(found_elements_2)>0:
        return found_elements_2
        return None
def get_link_from_box_post_title(cat_el_2):
    child = cat_el_2.find('a')
    return child.get('href')

def get_post_title_2 (bs):
    post_title_2 = bs.find('title')
    return post_title_2.string

def get_content_2(bs):
    post_content_2=[]
    if len(whole_post_2)>0:
        element = whole_post_2[0]
        for child in element.children:
            if child.string != None:
                post_content_2.append(child)
            return(post_content_2)

#if __name__ == '__main__':
#     url = "http://blogdulich.vn/am-thuc"
#     file_name = "blogdulich-amthuc.html"
#     download_webpage(url, file_name="blogdulich-amthuc.html")
#     open_file = open(file_name, "rb")
#     decoded_content = open_file.read().decode("utf-8")
#     soup_2 = BeautifulSoup (decoded_content, "html.parser")
#     ret_cat_els_2 = find_box_post_title (soup_2, "Ẩm thực")
#     i=0
#     if __name__ == '__main__':
#     while i<len(ret_cat_els_2):
#         article_link_2= get_link_from_box_post_title(ret_cat_els_2[i])
#         file_name = "blogdulich_article_1.html"
#         download_webpage(article_link_2,file_name = "blogdulich_article_1.html")
#         open_article_file_2 = open(file_name,"rb")
#         decoded_article_content_2 = open_article_file_2.read().decode("utf-8")
#         blogdulich_article = BeautifulSoup (decoded_article_content_2, "html.parser")
#         print(get_post_title_2(blogdulich_article))
#         get_content_2(blogdulich_article)
#         i=i+1
















