# ==============================================================================
# -- Global function ----------------------------------------------------------
# ==============================================================================
def type_of_letter(letter):
    consonants = ['b', 'c', 'd', 'g', 'ğ', 'j', 'l', 'm', 'n', 'r', 'v', 'y', 'y', 'z', 'ç', 'f', 'h', 'k', 'p',
                  's', 'ş', 't']
    vowels = ['a', 'ı', 'o', 'u', 'e', 'i', 'ö', 'ü']

    if letter in consonants:
        return 'c'
    elif letter in vowels:
        return 'v'
    else:
        return '#'


# ==============================================================================
# -- TMStatus class ------------------------------------------------------------
# ==============================================================================
class TMStatus:

    def __init__(self, state, transitions):
        # Create a dictionary for keep the current state and tape index
        self.machine_steps = []
        self.cur_state = state
        self.transition = transitions
        # Initialize the machine_steps with first step
        self.machine_steps.append((self.cur_state, 0))
        self.count_pos = 0

    def get_transition(self, tape_symbol):
        """Return the transition function for current state"""

        # What is the type of the tape_symbol
        symbol = type_of_letter(tape_symbol)

        if self.cur_state in self.transition and \
                symbol in self.transition[self.cur_state]:
            return self.transition[self.cur_state][symbol]
        else:
            return None

    def update(self, tape):
        """Go to the next status"""

        control_strings = []

        # Get the transition
        # transition form: (next state, tape output, direction)
        tape_symbol = tape.read_tape()
        transition = self.get_transition(tape_symbol)

        # Control strings
        control_strings.append( ( "The current state: {}, the input symbol: {}".format(self.cur_state, tape_symbol),
                               "The transition: {}".format(transition)) )

        if transition is not None:

            # Set the current state
            self.cur_state = transition[0]

            # Write this output to the tape
            if transition[1] is not '':
                to_write = tape_symbol if transition[1][0] != '-' else str('-' + tape_symbol)
                self.count_pos = self.count_pos + 0 if transition[1][0] != '-' else self.count_pos + 1
                tape.write_to_tape(to_write)

            # Move to the head of the tape
            tape.move(transition[2])

            # update the machine_steps dictionary

            self.machine_steps.append((self.cur_state, tape.cur_pos + self.count_pos))

            return True, control_strings
        return False, control_strings
