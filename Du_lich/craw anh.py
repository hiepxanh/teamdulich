__author__ = 'hiepx'
from bs4 import BeautifulSoup
import urllib3

def download_webpage(url, file_name = "data.html"):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    file = open(file_name,'wb')
    file.write(r.data)
    file.close()

url = "http://toidi.net/am-thuc-2/mon-ngon-sai-gon.html"
file_name = "thughiem.html"
#download_webpage(url, file_name)
open_file = open(file_name, "rb")

decoded_content = open_file.read().decode("utf-8")
soup = BeautifulSoup (decoded_content, "html.parser")

import re
#print (type(soup.find_all('img')))
def get_image(hiep):
    i = 0
    for link in soup.find_all('img'):
        #print (link.get('src'))
        if i == 1: # chi lay cai anh thu 2
            #print (link.get('src'))
            return link.get('src')
        else:
            None
        i += 1

print (get_image(soup))

# def get_image(soup):
#     found_image = soup.find_all('img')
#     i = 0
#     element = found_image[0]
#     for link in element:
#         if i == 1:
#             a= link.get('src')
#             return a
#         else:
#             return None
#         i += 1
#
# print (get_image(soup))
