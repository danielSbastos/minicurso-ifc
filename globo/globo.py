import os

from newsapi import NewsApiClient


class Globo:

    NEWS_API_KEY = os.getenv("NEWS_API_KEY")

    def __init__(self):
        self.api = NewsApiClient(api_key=self.NEWS_API_KEY)

    def find_news(self, query):
        self.query = query
        return self.api.get_everything(q=self.query, sources="globo", sort_by="relevancy")

    def format_for_messenger(self, news):
        content_to_be_sent = []

        articles = news.get("articles")
        if articles:
            for article in articles[:3]:
                content_to_be_sent.append(
                    "*" + article.get("title") + "*" + '\n' + article.get("url")
                )
        else:
            content_to_be_sent.append("Nenhum notícia encontrada para *" + self.query + "*")

        return "\n\n".join(content_to_be_sent)
