class TMTape():

    def __init__(self, input):
        self.tape = list(input)
        self.cur_pos = 0

    def is_end(self, blank_symbol):
        """Return true if the tape end, otherwise return false"""
        return self.tape[self.cur_pos] == blank_symbol

    def read_tape(self):
        return self.tape[self.cur_pos]

    def get_tape(self):
        return "".join(self.tape)

    def move(self, direction):

        if direction == 'R':
            self.cur_pos += 1
        elif direction == 'L':
            self.cur_pos -= 1
