__author__ = 'sunary'


import unicodedata
import random


def get_list():
    of = open('../resources/vi_accentwords.txt')
    words = of.read().split('\n')
    of.close()

    set_words = set()
    for word in words:
        word = word.split(' ')
        for w in word:
            set_words.add(remove_accent(w))

    words = list(set_words)
    words.sort()

    of = open('../resources/vi_listwords.txt', 'w')
    for w in words:
        of.write(w + '\n')

    of.close()


def remove_accent(text):
    text = unicode(text, "utf-8")
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').lower()


def dict_search():
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    len_dict = len(words)
    index_words = [-1] * 2
    index_words[0] = 0

    while index_words[0] < len_dict:
        current_index = last_index(index_words)
        text_search = ''
        for i in range(current_index + 1):
            text_search += words[index_words[i]] + ' '

        print text_search
        if search_more(text_search[:-1]) and current_index + 1 < len(index_words):
            index_words[current_index + 1] = 0
        else:
            index_words[current_index] += 1
            while index_words[current_index] >= len_dict:
                if current_index > 0:
                    index_words[current_index:] = [-1] * (len(index_words) - current_index)
                    index_words[current_index - 1] += 1
                    current_index -= 1
                else:
                    return


def dict_search2():
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    len_dict = len(words)

    for i in range(len_dict):
        for j in range(len_dict):
            text_search = words[i] + ' ' + words[j]
            print text_search


def dict_search3():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    len_dict = len(words)

    for i in range(len_dict):
        text_search = words[i]
        print text_search
        if search_more(text_search):
            for c in alphabet:
                text_search = words[i] + ' ' + c
                print text_search


def last_index(idx):
    for i in reversed(range(len(idx))):
        if idx[i] != -1:
            return i


def search_more(text):
    return random.randrange(0, 5) > 3


if __name__ == '__main__':
    dict_search3()