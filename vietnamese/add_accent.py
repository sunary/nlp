# -*- coding: utf-8 -*-
__author__ = 'sunary'


from vietnamese import virules, vichar, validation


def add_accent(input_text, input_type=1):
    global may_move_accent

    may_move_accent = False
    previous_chars = []
    string_chars = ''
    output_text = []

    input_text += ' '
    for c in input_text:
        if c == ' ':
            may_move_accent = False
            if previous_chars:
                if isinstance(previous_chars, list):
                    previous_chars = vichars_to_chars(previous_chars)

                output_text.append(previous_chars)
                previous_chars = []
                string_chars = ''
        else:
            if isinstance(previous_chars, list):
                string_chars += c
                if input_type == 1:
                    previous_chars = telex_transform(previous_chars, string_chars, c)
                else:
                    previous_chars = vni_transform(previous_chars, string_chars, c)
                if isinstance(previous_chars, list) and not validation.validation(vichars_to_chars(previous_chars)):
                    previous_chars = string_chars
            else:
                previous_chars += c

    return ' '.join(output_text)


def vichars_to_chars(vichars):
    return ''.join(map(lambda x: x.get_vichar(), vichars))


def contain_vichar(previous_chars, vichar):
    for char in previous_chars:
        if char == vichar:
            return True

    return False


def move_accent(previous_chars):
    for i in range(len(previous_chars) - 1):
        if previous_chars[i].accent != vichar.Accent.NONE:
            previous_chars[i + 1].accent = previous_chars[i].accent
            previous_chars[i].accent =  vichar.Accent.NONE
            break


def telex_transform(previous_chars, string_chars, new_char):
    global may_move_accent

    if not previous_chars:
        if new_char in 'w':
            new_char = vichar.ViChar('u')
            new_char.mark = vichar.Mark.BREVE
        elif new_char in 'W':
            new_char = vichar.ViChar('U')
            new_char.mark = vichar.Mark.BREVE
        else:
            new_char = vichar.ViChar(new_char)

        previous_chars.append(new_char)
        return previous_chars

    vowels_may_change = {}
    consonants_may_change = {}

    for i, w in enumerate(previous_chars):
        if w.get_char() in virules.VOWELS:
            vowels_may_change[w.get_char()] = i

    for i, w in enumerate(previous_chars):
        if w.get_char() in 'd':
            consonants_may_change[w.get_char()] = i

    if new_char.lower() in 'w':
        if vowels_may_change:
            if 'u' in vowels_may_change:
                vowels_changed = set()
                for w in previous_chars:
                    if w.get_char() == u'o' or w.get_char() == u'u' and w.get_char() not in vowels_changed:
                        vowels_changed.add(w.get_char())
                        previous_chars = make_action(previous_chars, string_chars, w.get_char(), 'w')
            elif 'a' in vowels_may_change:
                for w in previous_chars:
                    if w.get_char() == u'a':
                        previous_chars = make_action(previous_chars, string_chars, w.get_char(), 'w')
            elif 'o' in vowels_may_change:
                for w in previous_chars:
                    if w.get_char() == u'o':
                        previous_chars = make_action(previous_chars, string_chars, w.get_char(), 'w')
        else:
            if new_char in 'w':
                new_char = vichar.ViChar('u')
                new_char.mark = vichar.Mark.BREVE
            elif new_char in 'W':
                new_char = vichar.ViChar('U')
                new_char.mark = vichar.Mark.BREVE

            previous_chars.append(new_char)
    elif new_char.lower() in 'aeo' and new_char.lower() in vowels_may_change:
        previous_chars = make_action(previous_chars, string_chars, new_char, 'e')

    elif new_char.lower() in consonants_may_change:
        previous_chars = make_action(previous_chars, string_chars, new_char, 'd')

    elif new_char.lower() in 'fsrxjz':
        vowel_need = ''
        if vowels_may_change:
            if string_chars.startswith('gi'):
                if len(string_chars) == 3:
                    vowel_need = previous_chars[1].get_char()
                else:
                    vowel_need = previous_chars[2].get_char()
            elif string_chars.startswith('qu'):
                vowel_need = previous_chars[2].get_char()
            elif contain_vichar(previous_chars, vichar.ViChar('a', m=vichar.Mark.HAT)):
                vowel_need = 'a'
            elif contain_vichar(previous_chars, vichar.ViChar('a', m=vichar.Mark.BREVE)):
                vowel_need = 'a'
            elif contain_vichar(previous_chars, vichar.ViChar('e', m=vichar.Mark.HAT)):
                vowel_need = 'e'
            elif contain_vichar(previous_chars, vichar.ViChar('o', m=vichar.Mark.HAT)):
                vowel_need = 'o'
            elif contain_vichar(previous_chars, vichar.ViChar('o', m=vichar.Mark.BREVE)):
                vowel_need = 'o'
            elif contain_vichar(previous_chars, vichar.ViChar('u', m=vichar.Mark.BREVE)):
                vowel_need = 'u'
            else:
                count = 0
                id_vowel_need = (len(vowels_may_change) + 1)/2
                for w in previous_chars:
                    if w.get_char() in virules.VOWELS:
                        count += 1
                        if count == id_vowel_need:
                            vowel_need = w.get_char()
                            if count == 1 and len(vowels_may_change) == 2:
                                may_move_accent = True
                            break

        if vowel_need:
            previous_chars = make_action(previous_chars, string_chars, vowel_need, new_char.lower())
        else:
            previous_chars.append(vichar.ViChar(new_char))
            return previous_chars
    else:
        if may_move_accent:
            move_accent(previous_chars)
        previous_chars.append(vichar.ViChar(new_char))

    return previous_chars


def vni_transform(previous_chars, string_chars, new_char):
    global may_move_accent

    vowels_may_change = {}
    consonants_may_change = {}

    for i, w in enumerate(previous_chars):
        if w.get_char() in virules.VOWELS:
            vowels_may_change[w.get_char()] = i

    for i, w in enumerate(previous_chars):
        if w.get_char() in 'd':
            consonants_may_change[w.get_char()] = i

    if new_char in '78':
        if vowels_may_change:
            if 'a' in vowels_may_change:
                for w in previous_chars:
                    if w.get_char() == u'a':
                        previous_chars = make_action(previous_chars, string_chars, w.get_char(), 'w')
            elif 'u' in vowels_may_change or 'o' in vowels_may_change:
                for w in previous_chars:
                    if w.get_char() == u'o' or w.get_char() == u'u':
                        previous_chars = make_action(previous_chars, string_chars, w.get_char(), 'w')
            else:
                previous_chars.append(vichar.ViChar(new_char))
    elif new_char in '6' and any(x in vowels_may_change for x in 'aoe'):
        for x in 'eao':
            if x in vowels_may_change:
                previous_chars = make_action(previous_chars, string_chars, x, 'e')
                break

    elif new_char in '9':
        previous_chars = make_action(previous_chars, string_chars, 'd', 'd')

    elif new_char.lower() in '213450':
        vowel_need = ''
        if vowels_may_change:
            if string_chars.startswith('gi'):
                if len(string_chars) == 3:
                    vowel_need = previous_chars[1].get_char()
                else:
                    vowel_need = previous_chars[2].get_char()
            elif string_chars.startswith('qu'):
                vowel_need = previous_chars[2].get_char()
            elif contain_vichar(previous_chars, vichar.ViChar('a', m=vichar.Mark.HAT)):
                vowel_need = 'a'
            elif contain_vichar(previous_chars, vichar.ViChar('a', m=vichar.Mark.BREVE)):
                vowel_need = 'a'
            elif contain_vichar(previous_chars, vichar.ViChar('e', m=vichar.Mark.HAT)):
                vowel_need = 'e'
            elif contain_vichar(previous_chars, vichar.ViChar('o', m=vichar.Mark.HAT)):
                vowel_need = 'o'
            elif contain_vichar(previous_chars, vichar.ViChar('o', m=vichar.Mark.BREVE)):
                vowel_need = 'o'
            elif contain_vichar(previous_chars, vichar.ViChar('u', m=vichar.Mark.BREVE)):
                vowel_need = 'u'
            else:
                count = 0
                id_vowel_need = (len(vowels_may_change) + 1)/2
                for w in previous_chars:
                    if w.get_char() in virules.VOWELS:
                        count += 1
                        if count == id_vowel_need:
                            vowel_need = w.get_char()
                            if count == 1 and len(vowels_may_change) == 2:
                                may_move_accent = True
                            break

        if vowel_need:
            previous_chars = make_action(previous_chars, string_chars, vowel_need, virules.VNI_TELEX_CONVERTER[new_char])
        else:
            previous_chars.append(vichar.ViChar(new_char))
            return previous_chars
    else:
        previous_chars.append(vichar.ViChar(new_char))

    return previous_chars


def make_action(previous_chars, string_chars, char_action, action_id):
    for w in previous_chars:
        if char_action.lower() == w.get_char():
            if not w.action(action_id.lower()) and\
                    (string_chars[-2].lower() == char_action or string_chars[-2].lower() == action_id):
                previous_chars = string_chars[:-1]
            break

    return previous_chars


if __name__ == '__main__':
    # print add_accent('cos chis thif neen')
    # print add_accent('coo chus')
    # print add_accent('dix nhieen laf uw ow dduowcj')
    # print add_accent('vox vawn nhataj')
    # print add_accent('hoawcj laf')
    # print add_accent('ddoocj coo caauf baij')
    # print add_accent('mootjs ddoanjv vawn bisf ssafi nhieeuf looixo nguoiwf hiiiieue')
    # print add_accent('hieeus nuawx hoaf hoas cuuws haauj hoanf cuowps cowf ddiaj loiwj ddaoj thuowr chuyeenj tuys')
    # print add_accent('quas gias gir thuowngr nhows hieenf hoafn hoaxn hoawjc chuyeenj dduowng thoiwf meof')
    # print add_accent('nghieeng chieenj huowngf')
    # print add_accent('DDdos server with haSs')
    # print add_accent('cuuws coooc dddos')
    print add_accent('Thieen, thoiwf', 1)
    # print add_accent('thu73 mo6t5 ca1c d9u3 nga4 nu7a4 truo71c')

    # print add_accent('DDOOCJ COO CAAUF BAIJ W UW')