# -*- coding: utf-8 -*-
__author__ = 'sunary'


from vietnamese import virules


class Accent(object):

    NONE = 0
    GRAVE = 1
    ACUTE = 2
    HOOK = 3
    TIDLE = 4
    DOT = 5


class Mark(object):

    NONE = 0
    HAT = 1
    BREVE = 2 # or HORN
    # HORN = 3
    BAR = 4


class ViChar(object):

    def __init__(self, c, a=Accent.NONE, m=Mark.NONE):
        self.accent = a
        self.mark = m

        if c in virules.LOWER_CONVERTER:
            self.char = virules.LOWER_CONVERTER[c]
            self.is_uppercase = True
        else:
            self.char = c
            self.is_uppercase = False

    def get_char(self):
        return self.char

    def get_vichar(self):
        vichar = self.char
        if self.mark == Mark.HAT:
            if vichar == 'a':
                vichar = u'â'
            elif vichar == 'e':
                vichar = u'ê'
            elif vichar == 'o':
                vichar = u'ô'
        elif self.mark == Mark.BREVE:
            if vichar == u'a':
                vichar = u'ă'
            elif vichar == 'o':
                vichar = u'ơ'
            elif vichar == 'u':
                vichar = u'ư'
        elif self.mark == Mark.BAR:
            if vichar == 'd':
                vichar = u'đ'

        if self.accent != Accent.NONE:
            vichar = virules.ADD_MARK[vichar][self.accent - 1]

        if self.is_uppercase:
            return virules.UPPER_CONVERTER[vichar]
        else:
            return vichar

    def action(self, action_id):
        if action_id in 'aeo':
            if self.mark != Mark.HAT:
                self.mark = Mark.HAT
            else:
                return False
        elif action_id == 'w':
            if self.mark != Mark.BREVE:
                self.mark = Mark.BREVE
            else:
                return False
        elif action_id == 'd':
            if self.mark != Mark.BAR:
                self.mark = Mark.BAR
            else:
                return False

        elif action_id == 'f':
            if self.accent != Accent.GRAVE:
                self.accent = Accent.GRAVE
            else:
                return False
        elif action_id == 's':
            if self.accent != Accent.ACUTE:
                self.accent = Accent.ACUTE
            else:
                return False
        elif action_id == 'r':
            if self.accent != Accent.HOOK:
                self.accent = Accent.HOOK
            else:
                return False
        elif action_id == 'x':
            if self.accent != Accent.TIDLE:
                self.accent = Accent.TIDLE
            else:
                return False
        elif action_id == 'j':
            if self.accent != Accent.DOT:
                self.accent = Accent.DOT
            else:
                return False
        elif action_id == 'z':
            if self.accent != Accent.NONE:
                self.accent = Accent.NONE
            else:
                return False
        else:
            pass
            # raise NotImplementedError('Not support')

        return True

    def __eq__(self, other):
        return self.char == other.char and self.accent == other.accent and self.mark == other.mark


if __name__ == '__main__':
    o_char = ViChar('d')
    # o_char.action('o')
    # o_char.action('w')
    # o_char.action('f')
    o_char.action('d')
    print o_char.get_vichar()