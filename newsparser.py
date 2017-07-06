# -*- coding: UTF-8 -*-

import codecs
import json
import chardet
import re


def read_file(file_name):
    with open(file_name, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        data = data.decode(encoding=result['encoding'])
        dict_news = json.loads(data)
        assert isinstance(dict_news, object)
        return dict_news


def get_news_list(dict_news):
    rss_list = dict_news['rss']['channel']['item']
    news_list = []
    for dict_n in rss_list:
        if '__cdata' in dict_n['description']:
            news_list.append(dict_n['description']['__cdata'])
        else:
            news_list.append(dict_n['description'])
    string_world = re.sub(r'</?a.*?>', '', ' '.join(news_list))
    list_word = re.findall(r'[^,.\/ ]\w+', string_world)
    return list_word


def select_word(list_word):
    return [x for x in list_word if len(x) > 6]


def get_count_word(list_word):
    dict_word = {}
    for item in list_word:
        if item not in dict_word.keys():
            dict_word[item] = 1
        else:
            dict_word[item] += 1
    return dict_word


def sort_dict(dict_word_sort):
    l = lambda i: i[1]
    return sorted(dict_word_sort.items(), key=l, reverse=True)


def main():
    list_files = ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json']
    all_word_list = []
    for file_name in list_files:
        dict_news = read_file(file_name)
        list_word = get_news_list(dict_news)
        list_select_word = select_word(list_word)
        all_word_list.extend(list_select_word)
    dict_word = get_count_word(all_word_list)
    list_sort = sort_dict(dict_word)
    for item in list_sort[:10]:
        print('"{}" - упоминается {} раз'.format(item[0], item[1]))


main()
