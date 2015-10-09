__author__ = 'sunary'


import pandas as pd


class SpellingCorrect():

    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.get_dictionary()

    def get_dictionary(self):
        pd_file = pd.read_csv('dict.csv')
        self.list_words = pd_file['word']

    def get_position(self, word):
        if not word:
            return 1

        left_position = 0
        right_position = len(self.list_words) - 1

        mid_position= (left_position + right_position)/2
        mid_word = self.list_words[mid_position]
        while left_position <= right_position:
            if word < mid_word:
                right_position = mid_position - 1
            else:
                left_position = mid_position + 1

            mid_position = (left_position + right_position)/2
            mid_word = self.list_words[mid_position]

        return left_position

    def check_exist_dict(self, word):
        return self.list_words[self.get_position(word) - 1] == word

    def get_correct_words(self, word):
        ability_words = self.ability_words(word)
        correct_words = set()

        for word in ability_words:
            if self.check_exist_dict(word):
                correct_words.add(word)

        return correct_words

    def ability_words(self, word):
       splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
       deletes    = [a + b[1:] for a, b in splits if b]
       transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
       replaces   = [a + c + b[1:] for a, b in splits for c in self.alphabet if b]
       inserts    = [a + c + b for a, b in splits for c in self.alphabet]
       return set(deletes + transposes + replaces + inserts)


if __name__ == '__main__':
    spelling_correct = SpellingCorrect()
    print spelling_correct.get_correct_words('speling')
    print spelling_correct.get_correct_words('embaras')
    print spelling_correct.get_correct_words('colate')
    print spelling_correct.get_correct_words('reciet')
