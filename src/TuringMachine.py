import copy


class TuringMachine(object):
    """The definition of Turing Machine."""

    def __init__(self, states, input_alphabet, tape_alphabet, blank, transitions, start_state, accept_state,
                 reject_state):
        """Initialize a Turing Machine."""

        self.states = copy.copy(states)
        self.input_alphabet = copy.copy(input_alphabet)
        self.tape_alphabet = copy.copy(tape_alphabet)
        self.blank = copy.copy(blank)
        self.transitions = copy.deepcopy(transitions)
        self.start_state = copy.copy(start_state)
        self.accept_state = copy.copy(accept_state)
        self.reject_state = copy.copy(reject_state)
        self.validation()

    def validation(self):
        """Validate the Turing Machine tuples"""

        # Every input symbols must be in tape symbols
        for symbol in self.input_alphabet:
            if symbol not in self.tape_alphabet:
                raise ValueError("Every input symbols must be in tape symbols")

        # Start state, accept state and reject state must be in states set
        if self.start_state not in self.states:
            raise ValueError("start_state must be in states set")
        if self.accept_state not in self.states:
            raise ValueError("accept_state must be in states set")
        if self.reject_state not in self.states:
            raise ValueError("reject_state must be in states set")

        # Reject state must be different from accept state
        if self.accept_state == self.reject_state:
            raise ValueError("Reject state must be different from start state")

    def validate_input(self, input):
        """"Validation function for turing machine input"""

        # The last element of input must be blank symbol
        if input[-1] != '#':
            raise ValueError("Input must end with blank symbol({})".format(self.blank))

        # Every element in input must be element of input_alphabet
        for elm in input[:-1]:
            if elm not in self.input_alphabet['vowels'] and elm not in self.input_alphabet['consonants']:
                raise ValueError("{} is not in input_alphabet".format(elm))

    def execute(self, input_tape):
        self.validate_input(input_tape)
        output_tape = ""
        return output_tape
