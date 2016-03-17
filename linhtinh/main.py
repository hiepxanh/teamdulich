import urllib3
from bs4 import BeautifulSoup
import re

def download_webpage(url, file_name = "data.html"):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    file = open(file_name,'wb')
    file.write(r.data)
    file.close()

def find_category(bs, category):
    found_elements = bs.find_all('a', rel = "category tag", string = "Ẩm Thực")
    if len(found_elements) > 0:
        return found_elements
    return None

def get_link_from_category_element(cat_el):
    top_parent = cat_el.parent.parent.parent
    a_book_mark = top_parent.find('a', rel="bookmark")
    return a_book_mark['href']

def extract_value (bs, identify):
    #search_for = re.compile(identify)
    found_elements = bs.find_all('a', rel = "category tag", string = "Ẩm Thực")
    print(found_elements[0])
    found_values = []
    #element = found_elements[0]
    #print(found_elements)
       # for child in element.children:

              #  if i==0:
                  #  found_values.append(child.string.strip())

                  #  found_values.append(child.string)

   # return found_values

if __name__ == '__main__':

    url = "http://toidi.net/tag/quan-an-ngon/"
    file_name = "toidi_amthuc.html"
    download_webpage(url, file_name = "toidi_amthuc.html")
    open_file = open(file_name, "rb")
    identify= "post-4116"
    decoded_content = open_file.read().decode("utf-8")
    soup = BeautifulSoup (decoded_content, "html.parser")
    ret_cat_els = find_category (soup, "Ẩm Thực")

if __name__ == '__main__':
    article_link=get_link_from_category_element(ret_cat_els[0])
    file_name="toidi_article_1.html"
    download_webpage(article_link, file_name="toidi_article_1.html")
    open_article_file = open(file_name,"rb")
    decoded_article_content = open_article_file.read().decode("utf-8")
    toidi_article = BeautifulSoup (decoded_article_content, "html.parser")

def get_post_title (bs, post_title):
    bs.find




