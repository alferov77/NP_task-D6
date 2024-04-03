# В файле news/apps.py

from django.apps import AppConfig

class NewsConfig(AppConfig):
    name = 'news'

    def ready(self):
        import news.signals


