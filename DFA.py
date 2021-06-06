class DFA:
    def __init__(self, alphabet: set, all_states: list, start_state: str,
                 finish_states: list, transitions: dict):
        self.state = start_state
        self.alphabet = alphabet
        self.all_states = all_states
        self.start_state = start_state
        self.finish_states = finish_states
        self. transitions = transitions

    def change_state(self, symbol):
        self.state = self.transitions[self.state][symbol]

    def test(self, string):
        for x in string:
            self.change_state(x)
        if self.state in self.finish_states:
            return "YES YES YES"
        else:
            return "NO"


