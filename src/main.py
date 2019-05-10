from TuringMachine import TuringMachine


def main():
    # The Turkish Alphabet
    input_alphabet = {
        'c': ['b', 'c', 'd', 'g', 'ğ', 'j', 'l', 'm', 'n', 'r', 'v', 'y', 'y', 'z', 'ç', 'f', 'h', 'k', 'p',
                       's', 'ş', 't'],
        'v': ['a', 'ı', 'o', 'u', 'e', 'i', 'ö', 'ü'],
        '#': ['#']
    }
    # tape alphabet
    tape_alphabet = {
        'c': ['b', 'c', 'd', 'g', 'ğ', 'j', 'l', 'm', 'n', 'r', 'v', 'y',
                       'y', 'z', 'ç', 'f', 'h', 'k', 'p', 's', 'ş', 't'],#consonants = c
        'v': ['a', 'ı', 'o', 'u', 'e', 'i', 'ö', 'ü'],#vowels=v
        '#': ['#'],
        '-': ['-']
    }
    # set of states
    states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10'}
    # initial state
    initial_state = 'q0'
    accept_state = 'q9'
    reject_state = 'q10'
    # Transitions
    transitions = {
        # Q0
        'q0': {
            'c': ('q2', 'c', 'R'),
            'v': ('q1', 'v', 'R'),
            '#': (reject_state, '', 'R') #reject
        },
        'q1': {
            'c': ('q3', 'c', 'R'),
            'v': (reject_state, '', 'R'), #reject
            '#': (accept_state, '', 'R')

        },
        'q2': {
            'c': (reject_state, '', 'R'),
            'v': ('q1', 'v', 'R'),
            '#': (reject_state, '', 'R')
        },
        'q3': {
            'c': ('q8', 'c', 'R'),
            'v': ('q4', 'v', 'L'),
            '#': (accept_state, '', 'R') #accept
        },
        'q4': {
            'c': ('q5', tape_alphabet['-'][0]+'c', 'R'),
            'v': (reject_state, '', 'R'),
            '#': (accept_state, '', 'R') 
        },
        'q5': {
            'c': (reject_state, '', 'R'),
            'v': ('q6', 'v', 'R'),
            '#': (accept_state, '', 'R') 
        },
        'q6': {
            'c': ('q7', 'c', 'R'),
            'v': (reject_state, '', 'R'),
            '#': (accept_state, '', 'R') 
        },
        'q7': {
            'c': ('q5', tape_alphabet['-'][0]+'c', 'R'),
            'v': ('q8', 'v', 'L'),
            '#': (accept_state, '', 'R') 
        },
         'q8': {
            'c': ('q5', tape_alphabet['-'][0]+'c', 'R'),
            'v': ('q4', 'v', 'L'),
            '#': (accept_state, '', 'R') 
        }
    }
    blank = '#'
    #print(transitions)
    spelling_turing_machine = TuringMachine(states, input_alphabet, tape_alphabet, blank, transitions, initial_state,accept_state, reject_state)
    while True:
        word = input("Enter a word (or Press ENTER to quit): ")
        if not word:
            break
        print("Your input:", word)
        output = spelling_turing_machine.execute(word)
        print("Turing Machine: ", output)


if __name__ == '__main__':
    main()
