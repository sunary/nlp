# -*- coding: utf-8 -*-
__author__ = 'sunary'

import os
import math
from statistic_tokenize import StatisticTokenize

class TestTokenize(StatisticTokenize):
    def __init__(self):
        self.current_dir = os.path.dirname(__file__)

    def read_model(self):
        StatisticTokenize.read_model(self)

    def read_data_test(self):
        self.doc = u'hôm qua nằm mơ thấy em đi bộ một mình'

    def tokenize(self):
        print self.arrange(self.doc.split(' '))

    def arrange(self, remain):
        if not remain:
            return [1, []]

        max_arrange = [-1, []]
        for i in range(1, 4):
            if len(remain) >= i:
                word = ' '.join(remain[0: i])
                position = self.sorted_list.find(word)
                print word + ' ' + self.sorted_list.words[position]
                if self.sorted_list.words[position] == word:
                    rate_word = i*math.pow(self.tag_model['rate'][position]/50.0, i)
                    value_arrange = self.arrange(remain[i:])
                    if max_arrange[0] <= rate_word*value_arrange[0]:
                        max_arrange[0] = rate_word*value_arrange[0]
                        max_arrange[1] = [i] + value_arrange[1]

        if max_arrange[0] == -1:
            value_arrange = self.arrange(remain[1:])
            max_arrange[0] = value_arrange[0]
            max_arrange[1] = [1] + value_arrange[1]
        return max_arrange

if __name__ == '__main__':
    test_tokenize = TestTokenize()
    test_tokenize.read_model()
    test_tokenize.read_data_test()
    test_tokenize.tokenize()