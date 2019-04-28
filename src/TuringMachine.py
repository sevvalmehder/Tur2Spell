import copy


class TuringMachine(object):
    """The definition of Turing Machine."""

    def __init__(self, states, alphabet, transitions, start_state, blank, accept_state):
        """Initialize a Turing Machine
        ps: alphabet = input_alphabet = tape_alphabet
        """

        self.states = copy.copy(states)
        self.alphabet = copy.copy(alphabet)
        self.transitions = copy.deepcopy(transitions)
        self.start_state = copy.copy(start_state)
        self.accept_state = copy.copy(accept_state)
        self.blank = copy.copy(blank)
        self.validation()

    # NOT COMPLETED
    def validation(self):
        """Validate the Turing Machine tuples"""
        if self.start_state not in self.start_state:
            raise ValueError("start_state must be in states set")

    def execute(self, input_tape):
        output_tape = ""
        return output_tape
