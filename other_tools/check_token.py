__author__ = 'sunary'


class CheckToken():
    
    def __init__(self):
        self.checker_token = []
        self.black_token = []

    def set_checker(self, checker):
        self.checker_token = checker

    def add_token(self, token):
        '''
        add token to the sorted list of token

        Args:
            token: the token need to be added
        '''
        if self.black_token:
            position = self._find(token)
            if token != self.black_token[position]:
                self.black_token[position + 1:position + 1] = [token]
        else:
            self.black_token.append(token)
        pass

    def _find(self, token):
        if not token:
            return 0

        left_position = 0
        right_position = len(self.black_token) - 1

        mid_position= (left_position + right_position)/2
        mid_value = self.black_token[mid_position]
        while left_position <= right_position:
            if token < mid_value:
                right_position = mid_position - 1
            else:
                left_position = mid_position + 1

            mid_position = (left_position + right_position)/2
            mid_value = self.black_token[mid_position]

        return left_position - 1

    def check_token(self):
        '''
        check any token in the sorted list of tokens is in the list

        Returns:
            bool: True if any token is in the list
  
        Examples:
            >>> set_checker([1, 2, 3, 4, 5, 6])
            >>> add_token([2, 3])
            >>> check_token()
            True
            >>> add_token([3, 4, 6])
            False
        '''
        for i in range(len(self.checker_token)):
            len_token = 1
            while True:
                list_token = self.checker_token[i: i + len_token]
                position = self._find(list_token) + 1

                if self.black_token[position - 1] == list_token:
                    del self.black_token[position - 1]

                if position >= len(self.black_token) or len_token > len(self.black_token[position]) or len_token > len(list_token) or\
                                self.black_token[position][len_token - 1] != list_token[len_token - 1]:
                    break
                len_token += 1
        return False

if __name__ == '__main__':
    check_token = CheckToken()
    check_token.set_checker([1, 2, 3, 2, 2, 4, 45, 46, 4, 45, 52, 1, 21, 4, 5, 3, 4, 5, 1, 2])
    check_token.add_token([1, 2])
    check_token.add_token([5, 2])
    check_token.add_token([3, 4, 1])
    check_token.add_token([3, 4])
    check_token.add_token([2, 2])
    print check_token.black_token
    check_token.check_token()
    print check_token.black_token