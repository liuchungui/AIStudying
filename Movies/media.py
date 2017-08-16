#coding=utf-8

class Movie(object):
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """
        Movie类的初始化方法
        :param title:
        :param poster_image_url:
        :param trailer_youtube_url:
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url