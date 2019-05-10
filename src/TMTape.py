class TMTape():

    def __init__(self, input, blank):
        self.tape = list(input)
        self.cur_pos = 0
        self.blank_symbol = blank
        self.add_blank()

    def read_tape(self):
        return self.tape[self.cur_pos]

    def write_to_tape(self, out):
        self.tape[self.cur_pos] = out

    def get_tape(self):
        return "".join(self.tape)

    def move(self, direction):

        if direction == 'R':
            self.cur_pos += 1
        elif direction == 'L':
            self.cur_pos -= 1

    def add_blank(self):
        self.tape.append(self.blank_symbol)

