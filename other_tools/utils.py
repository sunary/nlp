__author__ = 'sunary'


import re
import string


STOP_WORDS_SET = set(['a', 'an', 'and', 'are', 'as', 'at', 'be', 'but', 'by', 'for', 'if', 'in', 'into', 'is', 'it', 'no', 'not', 'of',
                      'on', 'or', 'such', 'that', 'the', 'their', 'then', 'there', 'these', 'they', 'this', 'to', 'was', 'will', 'with', '&'])

def normalize(text, keep_chars=''):
    '''
    Examples:
        >>> normalize('#Google-Vietnam', keep_chars='-')
        'google-vietnam'
    '''
    accept_chars = string.lowercase + string.digits + keep_chars
    text_normalized = ''

    for t in text.lower():
        if t in accept_chars:
            text_normalized += t

    return text_normalized

def split_text(text, split_char=' -', min_rate=1.5, split_all=False, split_uppercase=True):
    '''
    Examples:
        >>> split_text('AbcDefGhI')
        ['Abc', 'Def', 'Gh', 'I']
        >>> split_text('APP:NYI')
        ['APP:NYI']
        >>> split_text('a-b c', split_all=True)
        ['a', 'b', 'c']
    '''
    if split_all:
        splited_text = []
        last_i = 0
        for i in range(1, len(text)):
            if text[i] in split_char:
                splited_text.append(text[last_i: i])
                last_i = i + 1
        if last_i:
            splited_text.append(text[last_i:])
            return splited_text
    else:
        for sp in split_char:
            if sp in text:
                return text.split(sp)

    if not split_uppercase:
        return [text]

    alphabeta_uppercase = string.uppercase
    splited_text = []
    last_position = 0
    for i in range(1, len(text)):
        if text[i] in alphabeta_uppercase:
            splited_text.append(text[last_position:i])
            last_position = i

    splited_text.append(text[last_position:len(text)])

    avg_len = len(text)*1.0/len(splited_text)
    if avg_len >= min_rate:
        return splited_text

    return [text]

def check_abbreviate(long_text, short_text):
    '''
    Examples:
        >>> check_abbreviate('DanangUniversityTech', 'DUT')
        True
        >>> check_abbreviate('Danang University Tech', 'dut')
        True
        >>> check_abbreviate('HanoiVietnam', 'HN-VN')
        False
    '''
    long_text = split_text(long_text)
    short_text = split_text(short_text)
    short_text = list(short_text[0]) if len(short_text) == 1 else short_text

    if len(long_text) == len(short_text):
        for i in range(len(long_text)):
            if not normalize(long_text[i]).startswith(normalize(short_text[i])):
                return False

        return True
    return False

def root_url(url):
    '''
    Examples:
        >>> root_url('https://www.abc.xyz/google')
        'abc.xyz'
        >>> root_url('http://twitter.com/v2nhat')
        'twitter.com'
        >>> root_url('http://amazon.co.uk/')
        'amazon.co.uk'
        >>> root_url('https://en.wikipedia.com')
        'wikipedia.com'
    '''
    match = re.match('https?://([a-z0-9\.\-_]+)', url, re.IGNORECASE)
    if not match:
        match = re.match('([a-z0-9\.\-_]+)', url, re.IGNORECASE)
    if match and '.' in match.group(1):
        match = match.group(1).split('.')
        match = map(lambda x: normalize(x, '_-'), match)
        match = match[1:] if match[0] == 'www' else match

        if len(match) == 2:
            return '.'.join(match)
        if len(match) > 2:
            if len(match[-1]) <= 3 and len(match[-2]) <= 3:
                return '.'.join(match[-3:])
            else:
                return '.'.join(match[-2:])
    return url

def username_from_url(url, prefix=None):
    '''
    Examples:
        >>> username_from_url('http://twitter.com/v2nhat')
        'v2nhat'
        >>> username_from_url('http://v2nhat.tumblr.com/')
        'v2nhat'
    '''
    if prefix is None:
        match = re.match('https?://([a-z0-9\.\-_]+)', url, re.IGNORECASE)
        if match:
            match = match.group(1).split('.')
            match = match[1:] if match[0] == 'www' else match
            if len(match) > 2:
                return match[0]

        match = re.match('https?://[a-z0-9\.\-_]+/([a-z0-9\.\-_]+)', url, re.IGNORECASE)
        if match:
            return match.group(1)
    else:
        if prefix:
            match = re.match('https?://([a-z0-9\.\-_]+)', url)
            if match:
                match = match.group(1).split('.')
                match = match[1:] if match[0] == 'www' else match
                return match[0]
        else:
            match = re.match('https?://[a-z0-9\.\-_]+/([a-z0-9\.\-_]+)', url, re.IGNORECASE)
            if match:
                return match.group(1)
    return ''

def get_parameter(pattern, str_input):
    '''
    Examples:
        >>> get_parameter('select %s from %s', 'select user_id from twitter')
        ['user_id', 'twitter']
    '''
    replace_special_characters = {' ': '\s'}
    for key, value in replace_special_characters.iteritems():
        pattern = pattern.replace(key, value)

    prefix_left_slash_characters = '.:-+*?^$&!@#~()[]{}|'
    for ch in prefix_left_slash_characters:
        pattern = pattern.replace(ch, '\\' + ch)

    fixed_words = pattern.split('%s')
    values_in_input = []
    for i in range(len(fixed_words) - 1):
        regex_pattern = '^' + '.+?'.join(fixed_words[0:i + 1]) + '(.+?)' + '.+?'.join(fixed_words[i + 1:]) + '$'
        values_in_input.append(re.match(regex_pattern, str_input).group(1))

    return values_in_input

def vary(list_words, max_combine=None):
    '''
    Examples:
        >>> vary(['a', 'b', 'c'])
        set([('a', 'b', 'c'), ('abc',), ('ab', 'c'), ('a', 'bc')])
    '''
    group_list_words = set([tuple(list_words)])
    if max_combine is None:
        max_combine = len(list_words) - 1
    else:
        max_combine = min(len(list_words), max_combine) - 1

    last_group = group_list_words
    for i in range(max_combine):
        temp_group = last_group
        last_group = set()
        for gr in temp_group:
            last_group |= set(filter(lambda x: x not in group_list_words and x not in last_group, group2words(gr)))

        group_list_words |= last_group

    return group_list_words

def group2words(list_words):
    '''
    Examples:
        >>> group2words(['a', 'b', 'c'])
        [('ab', 'c'), ('a', 'bc')]
    '''
    if type(list_words) is tuple:
        list_words = list(list_words)
    return map(lambda x: tuple(list_words[0 : x] + [''.join(list_words[x : x + 2])] + list_words[x + 2:]), xrange(len(list_words) - 1))

def find_by_index(list_words, find_next=5, cannot_first_last=set()):
    '''
    Examples:
        >>> find_by_index(['1h', 'hardware', '2d', 'mobile', 'ab', 'beverage', 'bf', 'cryptography'])
        [['1h', 'hardware'], ['2d', 'mobile'], ['ab', 'beverage'], ['bf', 'cryptography']]
    '''
    indexed_word = []

    word_previous = list_words[0]
    id_previous = 0

    for i in range(1, len(list_words)):
        if i > id_previous + 1 and list_words[i] >= word_previous and\
                all([list_words[i + j] >= list_words[i] or (list_words[i + j] < word_previous if word_previous else True) for j in range(1, min(find_next, len(list_words) - i))]) and\
                normalize(list_words[i]) not in cannot_first_last and normalize(list_words[i-1]) not in cannot_first_last and len(list_words[i-1]) < 6:
            indexed_word.append(list_words[id_previous:i])
            word_previous = list_words[i]
            id_previous = i
    indexed_word.append(list_words[id_previous:])

    return indexed_word

def get_pdf_content(path, num_pages=None):
    import pyPdf

    content = ''
    pdf_file = file(path, 'rb')
    pdf = pyPdf.PdfFileReader(pdf_file)

    i = 0
    while True:
        try:
            content += pdf.getPage(i).extractText() + '\n'
            i += 1
            if num_pages and i >= num_pages:
                break
        except:
            break
    return content


if __name__ == '__main__':
    import doctest
    doctest.testmod()