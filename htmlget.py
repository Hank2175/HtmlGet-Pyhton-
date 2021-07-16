import requests
from bs4 import BeautifulSoup
import os

r = requests.get("http://www.sun-jet.com.tw/images/db/") #將此頁面的HTML GET下來
_Html_title = "http://www.sun-jet.com.tw"
soup = BeautifulSoup(r.text, "html.parser") #將網頁資料以html.parser
# print(soup.prettify())

if not os.path.exists("images"):
    os.mkdir("images")  # 建立資料夾

for _Aitem in soup.find_all("a"):
    _Img = _Aitem.get("href")
    img = requests.get(_Html_title + _Img)
    _File_Name = _Img[11:]

    if _File_Name.endswith(".png") or _File_Name.endswith(".jpg"):
        print(_File_Name)
        with open("images/" + _File_Name, "wb") as file:
            file.write(img.content)

# http://www.sun-jet.com.tw/images/db/SJ37_10704.jpg