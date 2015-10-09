__author__ = 'sunary'


import os

class LevenshteinDistance():
    '''
    Levenshteind distance of two words
    eg: 'a' - 'ab' is 1 (add 'b' from 'a')
        'ab' - 'ba' is 1 (switch 'a' and 'b' from 'ab')
        'ac' - 'ab' is 1 (replace 'c' from 'ac' by 'b')
        'ab' - 'cd' is 2 (replace 'a' from 'ab' by 'c', replace 'b' from 'cb' by 'd')
    '''
    
    def __init__(self):
        self.current_dir = os.path.dirname(__file__)
        
    def distance(self, str1, str2):
        lev = [[] for _ in range(len(str1) + 1)]
        for i in range(len(str1) + 1):
            lev[i] = [0]*(len(str2) + 1)

        for i in range(1, len(str1) + 1):
            lev[i][0] = i
        for j in range(1, len(str2) + 1):
            lev[0][j] = j

        for i in range(0, len(str1)):
            for j in range(0, len(str2)):
                if str1[i] == str2[j]:
                    lev[i + 1][j + 1] = lev[i][j]
                else:
                    lev[i + 1][j + 1] = min(lev[i][j + 1], lev[i + 1][j], lev[i][j]) + 1

        return 1 - lev[len(str1)][len(str2)]*1.0/max(len(str1), len(str2))


if __name__ == '__main__':
    levenshtein_distance = LevenshteinDistance()
    print levenshtein_distance.distance('tuonghan', 'vovannhat')