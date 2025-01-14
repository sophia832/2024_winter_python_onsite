import requests
from bs4 import BeautifulSoup
import pandas as pd

# step 1 : request webpage html
url = "https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRFptTXpJU0JYcG9MVlJYS0FBUAE?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant"
response = requests.get(url)
# print(response)
# print(len(response.text))

# step 2 : Convert text into soup
soup = BeautifulSoup(response.text, 'html.parser')

# step 3 : Find element
topic_elements = soup.find_all("div", class_="W8yrY")
print("Total # of topics: ", len(topic_elements))

list_of_news = list()
for topic_id, topic_element in enumerate(topic_elements):
    # 新聞標題
    news_titles = topic_element.find_all('a', class_="gPFEn")
    # 新聞媒體
    medias = topic_element.find_all('div', class_='vr1PYe')
    # 發布時間
    public_times = topic_element.find_all('time', class_='hvbAAd')

    for media, news_title, public_time in zip(medias, news_titles, public_times):
        # print(media.text)
        # print(news_title.text)  # 新聞標題
        # print(public_time['datetime'])
        # print()
        list_of_news.append(
            {
                'topic_id': topic_id,
                'media_name': media.text,
                'title': news_title.text,
                'url': 'https://news.google.com' + news_title['href'][1:],
                'public_time': public_time['datetime']
            }
        )


print("Total # of news: ", len(list_of_news))

df = pd.DataFrame(list_of_news)
df.to_csv("news.csv")
