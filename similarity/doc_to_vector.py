__author__ = 'sunary'


from other_tools.sorted_list import SortedWords
from other_tools.preprocessor import Preprocessor
import os
import math


import pandas as pd


class DocToVector():

    def __init__(self):
        self.current_dir = os.path.dirname(__file__)
        self.sorted_words = SortedWords()
        self.get_dictionary()
        self.preprocess = Preprocessor()

    def get_dictionary(self):
        pd_file = pd.read_csv(self.current_dir + '/../resources/word_frequency.csv')
        self.sorted_words.set(pd_file['word'])

    def add_to_dict_counter(self, docs):
        docs = self.preprocess.split_space(docs)

    def tf_idf(self, frequency_sentence, frequency_docs, num_words):
        return (1 + math.log(frequency_sentence))*math.log(frequency_docs*1.0/num_words)


if __name__ == '__main__':
    doc2vec = DocToVector()
    doc2vec.add_to_dict_counter('')
    print doc2vec.tf_idf()