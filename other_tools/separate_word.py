__author__ = 'sunary'


import pandas as pd
import os
from other_tools.sorted_list import SortedWords


class SeparateWord():
    '''
    separate combine words by character: [s, en, n]
    '''
    separate_words = ['s', 'en', 'n']

    def __init__(self):
        self.current_dir = os.path.dirname(__file__)
        self.sorted_words = SortedWords()
        self.get_dictionary()

    def get_dictionary(self):
        pd_file = pd.read_csv(self.current_dir + '/../resources/en_dict.csv')
        self.sorted_words.set(pd_file['word'])

    def find(self, word):
        if '-' in word:
            self.format_A_B(word)
        elif self.separate_words[1] in word and self.format_AsB(word):
            pass
        else:
            self.format_AB(word)

    def format_A_B(self, word):
        '''
        word has format: A-B

        Args:
            word: input word

        Returns:
            bool: True if input word can separate
        '''
        split_word = word.split('-')
        if self.sorted_words.exist(split_word[1]):
            if self.sorted_words.exist(split_word[0]):
                print split_word[0] + ' ' + split_word[1]
                return True
            elif split_word[0][-1] == 's' and self.sorted_words.exist(split_word[0][:-1]):
                print split_word[0][:-1] + ' ' + split_word[1]
                return True
        return False

    def format_AsB(self, word):
        '''
        word has format: A[character separate]B

        Args:
            word: input word

        Returns:
            bool: True if input word can separate
        '''
        id_separate = 1
        for i in range(1, len(word) - len(self.separate_words[id_separate])):
            if word[i:i + len(self.separate_words[id_separate])] == self.separate_words[id_separate] and self.sorted_words.exist(word[:i]) and self.sorted_words.exist(word[i + len(self.separate_words[id_separate]):]):
                print word[:i] + ' ' + word[i + len(self.separate_words[id_separate]):]
                return True
        return False

    def format_AB(self, word):
        '''
        word has format: AB

        Args:
            word: input word

        Returns:
            bool: True if input word can separate
        '''
        word_position = self.sorted_words.find(word)
        while word[0] == self.sorted_words.words[word_position][0] and word_position > 0:
            word_position -= 1
            if word.startswith(self.sorted_words.words[word_position]) and self.sorted_words.exist(word[len(self.sorted_words.words[word_position]):]):
                print self.sorted_words.words[word_position] + ' ' + word[len(self.sorted_words.words[word_position]):]
                return True
        return False


if __name__ == '__main__':
    check_word_combine = SeparateWord()
    check_word_combine.find('ballshoot')
    check_word_combine.find('mushroom')
    check_word_combine.find('aenbout')
    check_word_combine.find('asss-bout')
