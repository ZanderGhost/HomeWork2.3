# -*- coding: UTF-8 -*-

import codecs
import json
import chardet



def read_file (file_name):
	with open(file_name, 'rb') as f:
		data = f.read()
		result = chardet.detect(data)
	with codecs.open(file_name, encoding=result['encoding']) as news:
		dict_news = json.load(news)
		return dict_news

read_file('newsafr.json')
			
def get_news_list ():
	dict_news = read_file()
	rss_list = dict_news['rss']['channel']['item']
	news_list = []
	for dict_news in rss_list:
		news_list.append(dict_news['description']['__cdata'])
	list_word = ''.join(news_list).split(' ')
	return list_word

def select_word():
	list_word = get_news_list()
	list_select_word = []
	for word in list_word:
		if len(word) >= 6:
			list_select_word.append(word)
	return list_select_word

def get_count_word():
	list_word = select_word()
	dict_word = {}
	for item in list_word:
		if item not in dict_word.keys():
			dict_word[item] = 1
		else:
			dict_word[item] += 1
	return dict_word

def sort_dict():
	dict_word_sort = get_count_word()
	list_word_sort = []
	l = lambda i: i[1]
	list_word_sort = sorted(dict_word_sort.items(), key=l, reverse=True )
	return list_word_sort




	

