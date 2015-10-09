__author__ = 'sunary'


import re


class Preprocessor():

    def __init__(self):
        pass

    def remove_mark_docs(self, doc):
        for i in range(len(doc)):
            doc[i] = self.remove_mark(doc[i])
        return doc

    def remove_mark(self, doc):
        marks = ['.', ',', ';', ':', '!', '@', '$', '*']
        for m in marks:
            doc = doc.replace(m, '')
        return doc.lower()

    def detect_name_phase(self, doc):

        return doc

    def split_mark_sentence(self, doc):
        docs = doc.split('\n')

        mark_end = ['.', '!', '?']
        for mark in mark_end:
            sentences = docs
            docs = []
            for s in sentences:
                docs += s.split(mark)

        mark_link = [',', ':', ';']
        for mark in mark_link:
            sentences = docs
            docs = []
            for s in sentences:
                docs += s.split(mark)

        return docs

    def split_space(self, doc):
        split_mark_sentence = self.split_mark_sentence(doc)
        docs = []
        for doc in split_mark_sentence:
            split_space = doc.split(' ')
            for word in split_space:
                if word:
                    docs.append(word)

        return docs
    
    def vary(self, list_words, max_combine = None):
        '''
        Examples:
            >>> vary(['a', 'b', 'c'])
            [['a', 'b', 'c'], ['ab', 'c'], ['a', 'bc'], ['abc']]
        '''
        group_list_words = [list_words]
        if max_combine is None:
            max_combine = len(list_words)
        else:
            max_combine = min(len(list_words), max_combine)

        last_group = group_list_words
        for i in range(max_combine - 1):
            temp_group = last_group
            last_group = []
            for gr in temp_group:
                get_group = self.group2words(gr)
                for gr in get_group:
                    if gr not in group_list_words and gr not in last_group:
                        last_group .append(gr)

            group_list_words += last_group

        return group_list_words

    def group2words(self, list_words):
        '''
        Examples:
            >>> group2words(['a', 'b', 'c'])
            [['ab', 'c'], ['a', 'bc']]
        '''
        group_words = []
        for i in range(0, len(list_words) - 1):
            group_words.append(list_words[0:i] + [''.join(list_words[i:i+2])] + list_words[i+2:])

        return group_words
    
    def get_parameter(self, pattern, str_input):
        '''
        Examples:
            >>> get_parameter('select %s from %s', 'select user_id from twitter')
            ['user_id', 'twitter']
        '''
        replace_special_characters = {' ': '\s'}
        append_left_slash_characters = '.:-+*?^$&!@#~()[]{}|'
        for key, value in replace_special_characters.iteritems():
            pattern = pattern.replace(key, value)
        for ch in append_left_slash_characters:
            pattern = pattern.replace(ch, '\\' + ch)

        fixed_words = pattern.split('%s')
        values_in_input = []
        for i in range(len(fixed_words) - 1):
            regex_pattern = '^' + '.+?'.join(fixed_words[0:i + 1]) + '(.+?)' + '.+?'.join(fixed_words[i + 1:]) + '$'
            values_in_input.append(re.match(regex_pattern, str_input).group(1))

        return values_in_input

if __name__ == '__main__':
    preprocessor = Preprocessor()
    print preprocessor.split_space('adsd. dasd,adsd; sas\' !asdsd. adasd')
