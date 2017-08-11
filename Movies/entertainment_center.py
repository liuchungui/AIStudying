#coding=utf8

import json
import media
import fresh_tomatoes

def movies_data():
	# 读取movies.json数据，输出数组
	with open('movies.json', 'r') as f:
		data = json.load(f)
	return data

media_array = []
movies = movies_data()

# 通过数据创建media对象
for movie in movies:
	media_array.append(media.Movie(movie["title"].encode('UTF-8'), movie["poster_image_url"].encode('UTF-8'), movie["trailer_youtube_url"].encode('UTF-8')))

fresh_tomatoes.open_movies_page(media_array)
