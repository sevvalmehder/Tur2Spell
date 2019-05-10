import copy
from TMTape import TMTape
from TMStatus import TMStatus


class TuringMachine(object):
    """The definition of Turing Machine."""

    def __init__(self, states, input_alphabet, tape_alphabet, blank, transitions, start_state, accept_state,
                 reject_state):
        """Initialize a Turing Machine."""

        self.tape = None
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

    def is_final(self, status):
        """Check whether the given status is the final"""
        if status.cur_state == self.accept_state or \
                status.cur_state == self.reject_state:
            return True
        else:
            return False

    def execute(self, input_tape):
        self.validate_input(input_tape)

        self.tape = TMTape(input_tape)

        # Set the current status with start state and tape
        cur_status = TMStatus(self.start_state, self.transitions)

        # While the current status is not accepted update the status
        while not self.is_final(cur_status):
            cur_status.update(self.tape)

        # If the input is accepted
        if cur_status.cur_state == self.accept_state:
            result = "accepted"
        else:
            result = "rejected"

        return self.tape.get_tape(), result
