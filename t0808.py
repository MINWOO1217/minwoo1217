#모듈예제
# import requests
# url ="http://jspstudy.co.kr"
# movie = requests.get(url)
# print(movie.text)


#98p
# import sys
# sys.path.append("c:/doit")
# #import mymode


# #101p
# import requests
# from bs4 import BeautifulSoup

# url = "http://finance.naver.com/"
# # 클릭해서 나오는 실시간 속보 부분만 가져오기
# response = requests.get(url)

# soup = BeautifulSoup(response.content, "html.parser")
# # 안되면 터미널에서 파이썬 경로가서 ㄱㄱ
# #main_section = soup.find("div",{"class":"news_area"})
# main_section = soup.find("div",{"class":"section"})

# top_news_ul = main_section.find("ul")
# top_news = top_news_ul.find_all("span")

# for article in top_news:
#     print(article.get_text())





import requests
from bs4 import BeautifulSoup


# 클릭해서 나오는 실시간 속보 부분만 가져오기
url = "https://www.q-net.or.kr/man001.do?&gSite=Q&gId="
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
# main_section = soup.find("p",{"class":"infoText"})
# abc = main_section.find("p")
top_news = soup.find_all(attrs={"class": "infoText" })
print(top_news)


#top_ul = main_section.find_all("ul")
#print(main_section)

# top2 = top_ul.find("li")
# top3 = top2.find("ul")
# top4 = top3.find_all("li")

# for article in top4:
#     print(article.get_text())

