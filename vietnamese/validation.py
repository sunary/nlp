# -*- coding: utf-8 -*-
__author__ = 'sunary'


from vietnamese import virules


def validation(word):
    word = ''.join(filter(lambda x: x in virules.LOWER_CONVERTER and x in virules.UPPER_CONVERTER, word))
    word = ''.join([virules.LOWER_CONVERTER[w] if w in virules.LOWER_CONVERTER else w for w in word])
    word_separate = separate(word)

    def wrong_consonant():
        return set(virules.NOT_VOWELS).intersection(set(word_separate[1]))

    def wrong_vowels():
        return len(word_separate[1]) > 3

    return not (wrong_consonant() or wrong_vowels())


def separate(input_text):
    word_separate = [''] * 3

    for cons in virules.CONSONANTS:
        if input_text.startswith(cons):
            word_separate[0] = cons
            input_text = input_text[len(cons):]
            break

    for cons in virules.TERMINAL_CONSONANTS:
        if input_text.endswith(cons):
            word_separate[2] = cons
            input_text = input_text[:-len(cons)]
            break

    word_separate[1] = input_text

    return word_separate


if __name__ == '__main__':
    # print separate(u'nghiêng')
    # print separate(u'nhanh')
    # print separate(u'thà')
    # print separate(u'ắt')
    # print separate(u'được')
    # print separate(u'lơăn')
    print separate(u'bị')
    print validation(u'bị')