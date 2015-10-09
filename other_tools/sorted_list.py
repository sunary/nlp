__author__ = 'sunary'


class SortedWords():

    def __init__(self):
        self.words = []

    def set(self, sorted_list):
        self.words = sorted_list

    def add(self, word=None, list_word=None):
        '''
        add word or list of words to sorted list

        Args:
            word: the word need to add
            list_word: the list of words need to add
        '''
        if not self.words:
            if word:
                self.words.append(word)
                return
            else:
                self.words.append(list_word[0])
                del list_word[0]

        if word:
            position = self.find(word)
            if word != self.words[position]:
                self.words[position + 1:position + 1] = [word]
        else:
            for w in list_word[0:]:
                position = self.find(w)
                if w != self.words[position]:
                    self.words[position + 1:position + 1] = [w]

    def find(self, word):
        '''
        position of word in sorted list

        Args:
            word: input word

        Returns:
            position of input word
        '''
        if not word:
            return 0

        left_position = 0
        right_position = len(self.words) - 1

        mid_position= (left_position + right_position)/2
        mid_value = self.words[mid_position]
        while left_position <= right_position:
            if word < mid_value:
                right_position = mid_position - 1
            else:
                left_position = mid_position + 1

            mid_position = (left_position + right_position)/2
            mid_value = self.words[mid_position]

        return left_position - 1

    def exist(self, word='', position_word=0):
        if word:
            position = self.find(word)
        else:
            position = position_word
        return word == self.words[position]


if __name__ == '__main__':
    sorted_words = SortedWords()
    sorted_words.add(list_word = ['w', 'c', 'd', 'ff', 'b', 'c', 'ff'])
    print sorted_words.find('c')
    print sorted_words.words