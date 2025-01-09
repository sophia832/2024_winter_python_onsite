import pandas as pd
from openai_chatgpt import complete_chat


news = pd.read_csv("news.csv")

# print(news.head())

# solution 1
# news = news.to_dict(orient='records')
# for new in news[:5]:
#    print(new['title'])

# solution 2


def summarize_google_news(csv_file="news.csv"):
    news = pd.read_csv(csv_file)
    groups = news.groupby('topic_id')
    summarizations = list()
    for gid, group in groups:
        # print(list(group['title']), '\n')

        temp = list(group['title'])
        message = "\n". join(temp)
        print(message)
        summarization = complete_chat(message)
        print("summarization = ", summarization, '\n')
        summarizations.append(summarization)
    return summarizations


if __name__ == '__main__':
    summarize_google_news()
