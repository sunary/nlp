__author__ = 'sunary'


import re


class RegularExpression():

    def __init__(self):
        pass

    def regex_info(self):
        print re.match('.*?([\d\w_\.]+\@[\d\w_\.]+).*', 'dasd sadsad@kadh.com').group(1)

        REGEX_TEL = '.*?((\+\d*\s)?(\(\+?\d+\)\s?)?\d+[\d\s\-]*\d{2,}).*'
        print re.match(REGEX_TEL, '+1 (416) 868-1079, ext. 225').group(1)
        print re.match(REGEX_TEL, '(+416) 868-1079, ext. 225').group(1)
        print re.match(REGEX_TEL, '(416) 868-1079, ext. 225').group(1)
        print re.match(REGEX_TEL, '+1(416)868-1079, ext. 225').group(1)
        print re.match(REGEX_TEL, '+(416)868-1079, ext. 225').group(1)

        print re.match('<b>(.*)</b>', 'fsdfsd<b>fsdf</b>').group()

    def check_findall(self):
        print re.findall('<[^<]*?>|\)|\(|\s', '<fs>fdsdad sad sf<gf)d<rter>g>')

    def check_use_function(self):
        def my_replace(match):
            match = match.group()
            return match + str(match.index('e'))

        string = 'The quick @red fox jumps over the @lame brown dog.'
        print re.sub(r'@\w+', my_replace, string)

if __name__ == "__main__":
    regular_expression = RegularExpression()
    # regular_expression.regex_info()
    regular_expression.check_use_function()