__author__ = 'sunary'


import re


class State():

    def __init__(self, state, grammar_state):
        self.state = state
        self.grammar = []
        for gr_state in grammar_state:
            self.grammar.append({'state': gr_state, 'string': []})

    def set_grammar_string(self, state, string_state):
        '''
        find state start with other state, and set string

        Args:
            state (string): name of state
            string_state (string): grammar string

        Returns:
            bool: return True if found
        '''
        for grammar in self.grammar:
            if grammar['state'].startswith(state):
                grammar['string'] = string_state
                return True

        return False

    def get(self):
        '''
        get state name
        '''
        return self.state

    def get_grammar_state(self):
        '''
        get grammar state
        '''
        grammar_state = []
        for grammar in self.grammar:
            if grammar['state']:
                grammar_state.append(grammar['state'])

        return grammar_state

    def get_grammar_string(self):
        '''
        get grammar string
        '''
        grammar_string = []
        for grammar in self.grammar:
            if grammar['string']:
                grammar_string += grammar['string']

        return grammar_string

class StateMachine():

    def __init__(self):
        self.states = []

    def read_grammar(self):
        grammar_file = open('calculator_grammar.txt', 'r').read()
        self.grammar_lines = grammar_file.split('\n')

    def get_state_by_name(self, state):
        '''
        find state name

        Args:
            state (string): name of state

        Returns:
            the state found or False
        '''
        for grammar_state in self.states:
            if grammar_state.get() == state:
                return grammar_state

        return False

    def generator(self):
        for line in self.grammar_lines:
            get_state = line.split('=')
            get_state_input = get_state[1].split('|')
            grammar_state = []
            grammar_string = []
            for state in get_state_input:
                if self.get_start_state(state):
                    grammar_state.append(state)
                else:
                    grammar_string.append(state)

            if grammar_string:
                grammar_state.append('[leaf]')

            self.states.append(State(get_state[0], grammar_state))

            if grammar_string:
                self.states[-1].set_grammar_string('[leaf]', grammar_string)

        for state in self.states:
            if state.get_grammar_string():
                self.generate_state_string(state)

    def generate_state_string(self, state):
        '''
        generate grammar string

        Args:
            state: state need add grammar string
        '''
        for find_state in self.states:
            if find_state.set_grammar_string(state.get(), state.get_grammar_string()):
                self.generate_state_string(find_state)

    def get_start_state(self, grammar):
        '''
        find start state in grammar by A-Z or [...]

        Args:
            grammar (string): grammar string

        Returns
            start state if found or False
        '''
        if re.search('^[A-Z]', grammar):
            return grammar[:1]
        elif grammar.startswith('['):
            for i in range(len(grammar)):
                if grammar[i] == ']':
                    return grammar[:i + 1]

        return False

    def get_start_string(self, state_string, input):
        '''
        find start string of list grammar string

        Args:
            state_string (list of strings): list grammar
            input (character): character need check

        Returns:
            state string startswith input if found or False
        '''
        for state_str in state_string:
            if state_str.startswith(input):
                return state_str

        return False

    def __str__(self):
        str_return = 'Start of states:'
        for state in self.states:
            str_return += '\n state: %s, input: %s -- %s' % (state.get(), state.get_grammar_state(), state.get_grammar_string())

        return str_return

class CompilerCalculator():

    def __init__(self):
        self.state_machine = StateMachine()

    def get_grammar(self):
        self.state_machine.read_grammar()
        self.state_machine.generator()

    def process(self, input):
        self.valid = False
        for grammar in self.state_machine.states[0].grammar:
            self.check_grammar(input, grammar['state'])

        return self.valid

    def check_grammar(self, input_string, grammar):
        '''
        check grammar

        Args:
            input_string (string): string need check grammar
            grammar (string): grammar

        Returns:
            set flag 'valid' if string is match with grammar
        '''

        if self.valid or not (input_string or grammar):
            self.valid = True
            return
        elif not (input_string and grammar):
            return

        if self.state_machine.get_start_state(grammar):
            grammar_state = self.state_machine.get_start_state(grammar)

            if self.state_machine.get_state_by_name(grammar_state):
                for state in self.state_machine.get_state_by_name(grammar_state).grammar:

                    if self.state_machine.get_start_state(state['state']):
                        new_grammar = state['state'] + grammar[len(grammar_state):]
                        self.check_grammar(input_string, new_grammar)

                    if input_string[0] in state['string']:
                        self.check_grammar(input_string[1:], grammar[len(grammar_state):])
                    elif self.state_machine.get_start_string(state['string'], input_string[0]):
                        new_grammar = self.state_machine.get_start_string(state['string'], input_string[0])[1:] + grammar[len(grammar_state):]
                        self.check_grammar(input_string[1:], new_grammar)
        else:
            self.check_grammar(input_string[1:], grammar[1:])

if __name__ == '__main__':
    calculator = CompilerCalculator()
    calculator.get_grammar()
    print calculator.process('((12*3))-(456-789)')