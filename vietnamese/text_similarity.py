# -*- coding: utf-8 -*-
__author__ = 'sunary'


import re
from virules import LOWER_CONVERTER


VN_STOP_WORDS_SET = set(['bị', 'bởi', 'cả', 'các', 'cái', 'cần', 'càng', 'chỉ', 'chiếc', 'cho', 'chứ', 'chưa', 'chuyện',
                         'có', 'có thể', 'cứ', 'của', 'cùng', 'cũng', 'đã', 'đang', 'đây', 'để', 'đến_nỗi', 'đều',
                         'điều', 'do', 'đó', 'được', 'dưới', 'gì', 'khi', 'không', 'là', 'lại', 'lên', 'lúc', 'mà',
                         'mỗi', 'một cách', 'này', 'nên', 'nếu', 'ngay', 'nhiều', 'như', 'nhưng', 'những', 'nơi', 'nữa',
                         'phải', 'qua', 'ra', 'rằng', 'rằng', 'rất', 'rất', 'rồi', 'sau', 'sẽ', 'so', 'sự','tại', 'theo',
                         'thì', 'trên', 'trước', 'từ', 'từng', 'và', 'vẫn', 'vào', 'vậy', 'vì', 'việc', 'với', 'vừa'])


def lower(word):
    new_word = ''
    for i in range(len(word)):
        new_word += LOWER_CONVERTER[word[i]] if word[i] in LOWER_CONVERTER else word[i]

    return new_word


def set_of_word(text):
    words_set = set()

    for word in text.split(' '):
        word = re.sub('[\.,!;\(\)"\']+', '', word)
        word = lower(word)

        if word not in VN_STOP_WORDS_SET and word not in words_set:
            words_set.add(word)

    return words_set


def sim_ratio(text1, text2):
    if not isinstance(text1, set):
        words_set1 = set_of_word(text1)
    else:
        words_set1 = text1

    if not isinstance(text2, set):
        words_set2 = set_of_word(text2)
    else:
        words_set2 = text2

    return len(words_set1.intersection(words_set2)) * 1.0/ min(len(words_set1), len(words_set2))


if __name__ == '__main__':
    text1 = u'Của chồng công vợ'
    text2 = u'Vợ người thì đẹp, văn mình thì hay.'
    print(set_of_word(text1))
    print(set_of_word(text2))
    print check_sim(text1, text2)