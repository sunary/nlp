__author__ = 'sunary'


import os
from os import listdir
from os.path import isfile, join
import pandas as pd
import re
from other_tools.sorted_list import SortedWords
from other_tools.preprocessor import Preprocessor
from other_tools.quick_sort import QuickSort


class StatisticTokenize():

    def __init__(self):
        self.current_dir = os.path.dirname(__file__)
        self.sorted_list = SortedWords()
        self.preprocessor = Preprocessor()

    def create_model(self):
        fo = open(self.current_dir + '/../resources/vi_dict.txt', 'r')
        lines_file = fo.read().split('\n')

        self.tag_model = {'word': [],
                          'role': [],
                          'rate': []}
        for line in lines_file:
            if len(line) == 2:
                self.tag_model['role'][-1] = self.tag_model['role'][-1] + '-' + line[-1]
            else:
                self.tag_model['word'].append(line[:-2])
                self.tag_model['role'].append(line[-1])
                self.tag_model['rate'].append(1)

    def read_model(self):
        pd_file = pd.read_csv(self.current_dir + '/../resources/tag_model.csv')
        self.tag_model = {'word': [],
                          'role': [],
                          'rate': []}
        for i in range(len(pd_file['word'])):
            self.tag_model['word'].append(pd_file['word'][i])
            self.tag_model['role'].append(pd_file['role'][i])
            self.tag_model['rate'].append(pd_file['rate'][i])

    def sort_model(self):
        quick_sort = QuickSort()
        self.tag_model = quick_sort.get_dataframe(self.tag_model, ['word', 'role', 'rate'])
        self.sorted_list.set(self.tag_model['word'])

    def read_text_train(self):
        fo = open(self.current_dir + '/../resources/VNESEcorpus.txt', 'r')
        self.text_train = fo.read()
        self.text_train = self.text_train.split('\n')
        self.text_train = self.preprocessor.remove_mark_docs(self.text_train)

    def statistic(self):
        for sentence in self.text_train:
            self.statistic_doc(sentence)

    def statistic_doc(self, text):
        text = text.split(' ')
        for len_word in range(1, 4):
            for i in range(len(text) - len_word + 1):
                word = ' '.join(text[i:i + len_word])
                position = self.sorted_list.find(word)

                if self.sorted_list.words[position] == word:
                    self.tag_model['rate'][position] += 1

    def save_model(self):
        self.tag_model = pd.DataFrame.from_dict(self.tag_model)
        self.tag_model.to_csv(self.current_dir + '/../resources/tag_model.csv', index=False)

if __name__ == '__main__':
    statistic_tokenize = StatisticTokenize()
    statistic_tokenize.read_model()
    statistic_tokenize.sort_model()
    # statistic_tokenize.read_text_train()
    # statistic_tokenize.statistic()
    statistic_tokenize.save_model()