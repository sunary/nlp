__author__ = 'sunary'


import os
from other_tools.preprocessor import Preprocessor
from other_tools.sorted_list import SortedWords


class NaiveBayesClassify():
    '''
    classified texts using Naive Bayes
    '''
    def __init__(self):
        self.current_dir = os.path.dirname(__file__)
        self.sorted_words = SortedWords()
        self.preprocessor = Preprocessor()

    def set_doc_c1(self):
        fo = open(self.current_dir + '/../resources/pos_text.txt', 'r')
        self.text_c1 = fo.read()
        self.text_c1 = self.text_c1.split('\n')
        self.text_c1 = self.preprocessor.remove_mark_docs(self.text_c1)
        fo.close()

    def set_doc_c2(self):
        fo = open(self.current_dir + '/../resources/neg_text.txt', 'r')
        self.text_c2 = fo.read()
        self.text_c2 = self.text_c2.split('\n')
        self.text_c2 = self.preprocessor.remove_mark_docs(self.text_c2)

    def set_doc_classify(self):
        fo = open(self.current_dir + '/../resources/classify_text.txt', 'r')
        self.text_classify = fo.read()
        self.text_classify = self.text_classify.split('\n')
        self.text_classify = self.preprocessor.remove_mark_docs(self.text_classify)
        fo.close()

    def probability_cal(self):
        self.p_c1 = len(self.text_c1)*1.0/(len(self.text_c1) + len(self.text_c2))
        self.p_c2 = 1 - self.p_c1

        self.word = []
        self.tf_c1 = []
        self.tf_c2 = []

        #add to list
        for sentence in self.text_c1:
            s_words = sentence.split(' ')
            for w in s_words:
                self.sorted_words.add(word=w)

        for sentence in self.text_c2:
            s_words = sentence.split(' ')
            for w in s_words:
                self.sorted_words.add(word=w)

        #cal tf
        self.tf_c1 = [0 for i in range(len(self.sorted_words.words))]
        for sentence in self.text_c1:
            s_words = sentence.split(' ')
            for w in s_words:
                self.tf_c1[self.sorted_words.find(w)] += 1

        self.tf_c2 = [0 for i in range(len(self.sorted_words.words))]
        for sentence in self.text_c2:
            s_words = sentence.split(' ')
            for w in s_words:
                self.tf_c2[self.sorted_words.find(w)] += 1

    def train(self):
        sum_tf_c1 = 0
        sum_tf_c2 = 0
        for i in range(len(self.word)):
            sum_tf_c1 += self.tf_c1[i]
            sum_tf_c2 += self.tf_c2[i]

        self.probability_c1 = []
        self.probability_c2 = []
        for i in range(len(self.sorted_words.words)):
            self.probability_c1.append((self.tf_c1[i] + 1.0)/(len(self.sorted_words.words) + sum_tf_c1))
            self.probability_c2.append((self.tf_c2[i] + 1.0)/(len(self.sorted_words.words) + sum_tf_c2))

    def get_rate_probability_c1(self, word):
        position = self.sorted_words.find(word)
        if word == self.sorted_words.words[position]:
            return self.probability_c1[position]/self.probability_c2[position]
        else:
            return 1

    def test(self):
        for sentence in self.text_classify:
            self.test_doc(sentence)

    def test_doc(self, text):
        rate_px_c1 = 1

        s_words = text.split(' ')
        for w in s_words:
            rate_px_c1 *= self.get_rate_probability_c1(w)

        if rate_px_c1*self.p_c1 >= self.p_c2:
            print text + ': belong c1'
        else:
            print text + ': belong c2'

if __name__ == '__main__':
    naive_bayes_classify = NaiveBayesClassify()
    naive_bayes_classify.set_doc_c1()
    naive_bayes_classify.set_doc_c2()
    naive_bayes_classify.set_doc_classify()
    naive_bayes_classify.probability_cal()
    naive_bayes_classify.train()
    naive_bayes_classify.test()
