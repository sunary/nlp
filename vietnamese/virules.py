# -*- coding: utf-8 -*-
__author__ = 'sunary'


LOWER_CONVERTER = {
    u'A': u'a', u'À': u'à', u'Á': u'á', u'Ả': u'ả', u'Ã': u'ã', u'Ạ': u'ạ',
    u'Ă': u'ă', u'Ằ': u'ằ', u'Ắ': u'ắ', u'Ẳ': u'ẳ', u'Ẵ': u'ẵ', u'Ặ': u'ặ',
    u'Â': u'â', u'Ầ': u'ầ', u'Ấ': u'ấ', u'Ẩ': u'ẩ', u'Ẫ': u'ẫ', u'Ậ': u'ậ',
    u'B': u'b',
    u'C': u'c',
    u'D': u'd', u'Đ': u'đ',
    u'E': u'e', u'È': u'è', u'É': u'é', u'Ẻ': u'ẻ', u'Ẽ': u'ẽ', u'Ẹ': u'ẹ',
    u'Ê': u'ê', u'Ề': u'ề', u'Ế': u'ế', u'Ể': u'ể', u'Ễ': u'ễ', u'Ệ': u'ệ',
    u'F': u'f',
    u'G': u'g',
    u'H': u'h',
    u'I': u'i', u'Ì': u'ì', u'Í': u'í', u'Ỉ': u'ỉ', u'Ĩ': u'ĩ', u'Ị': u'ị',
    u'J': u'j',
    u'K': u'k',
    u'L': u'l',
    u'M': u'm',
    u'N': u'n',
    u'O': u'o', u'Ò': u'ò', u'Ó': u'ó', u'Ỏ': u'ỏ', u'Õ': u'õ', u'Ọ': u'ọ',
    u'Ô': u'ô', u'Ồ': u'ồ', u'Ố': u'ố', u'Ổ': u'ổ', u'Ỗ': u'ỗ', u'Ộ': u'ộ',
    u'Ơ': u'ơ', u'Ờ': u'ờ', u'Ớ': u'ớ', u'Ở': u'ở', u'Ỡ': u'ỡ', u'Ợ': u'ợ',
    u'P': u'p',
    u'Q': u'q',
    u'R': u'r',
    u'S': u's',
    u'T': u't',
    u'V': u'v',
    u'U': u'u', u'Ù': u'ù', u'Ú': u'ú', u'Ủ': u'ủ', u'Ũ': u'ũ', u'Ụ': u'ụ',
    u'Ư': u'ư', u'Ừ': u'ừ', u'Ứ': u'ứ', u'Ử': u'ử', u'Ữ': u'ữ', u'Ự': u'ự',
    u'W': u'w',
    u'X': u'x',
    u'Y': u'y', u'Ỳ': u'ỳ', u'Ý': u'ý', u'Ỹ': u'ỹ', u'Ỷ': u'ỷ', u'Ỵ': u'ỵ',
    u'Z': u'z',
}

UPPER_CONVERTER = {}
for k, v in LOWER_CONVERTER.iteritems():
    UPPER_CONVERTER[v] = k


VNI_TELEX_CONVERTER = {u'2': u'f', u'1': u's', u'3': u'r', u'4': u'x', u'5': u'j', u'0': u'z',
                       u'6': u'aeo', u'7': u'w', u'8': 'w', u'9': 'd'}

TRANSFORM = {u'a': u'âă',
            u'd': u'đ',
            u'e': u'ê',
            u'o': u'ôơ',
            u'u': u'ư'}

ADD_MARK = {u'a': u'àáảãạ',
            u'ă': u'ằắẳẵặ',
            u'â': u'ầấẩẫậ',
            u'e': u'èéẻẽẹ',
            u'ê': u'ềếểễệ',
            u'i': u'ìíỉĩị',
            u'o': u'òóỏõọ',
            u'ô': u'ồốổỗộ',
            u'ơ': u'ờớởỡợ',
            u'u': u'ùúủũụ',
            u'ư': u'ừứửữự',
            u'y': u'ỳýỷỹỵ'
            }

VOWELS = [u'e', u'a', u'o', u'u', u'i', u'y']

NOT_VOWELS = [u'b', u'c', u'd', 'f', 'g', u'h', u'j', u'k', u'l',
            u'm', u'n', u'p', u'q', u'r', u's', u't', u'v', u'w', u'x', u'z',
            u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9']

CONSONANTS = [u'ngh',
            u'ch', u'gh', u'gi', u'kh', u'ng', u'nh', u'ph', u'qu', u'th', u'tr',
            u'b', u'c', u'd', u'g', u'h', u'k', u'l', u'm', u'n', u'p', u'q', u'r', u's', u't', u'v', u'x', u'đ']

TERMINAL_CONSONANTS = [u'ch', u'ng', u'nh', u'c', u'm', u'n', u'p', u't']