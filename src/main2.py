
import sys
from TuringMachine import TuringMachine 

def main():
	#The Turkish Alphabet
	input_alphabet={
					'consonants':['b', 'c', 'd', 'g', 'ğ', 'j', 'l','m', 'n', 'r', 'v', 'y','y', 'z', 'ç',  'f', 'h', 'k', 'p', 's', 'ş', 't'], 
					'vowels':['a', 'ı', 'o', 'u', 'e', 'i' ,'ö', 'ü']
					}
	#tape alphabet
	tape_alphabet={
					'consonants':['b', 'c', 'd', 'g', 'ğ', 'j', 'l','m', 'n', 'r', 'v', 'y',
								'y', 'z', 'ç',  'f', 'h', 'k', 'p', 's', 'ş', 't'], 
					'vowels':['a', 'ı', 'o', 'u', 'e', 'i' ,'ö', 'ü'],
					'other':['-', '#', 'E']
					}
	#set of states
	states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}
	#initial state
	initial_state='q0'
	accept_states={'q4', 'q5'}
	reject_states={'q7'}
	#Transitions
	transitions={
			#Q0
			'q0':{
				'consonant': ('q2', 'consonant', 'R'), 
				'vowel' : ('q1', 'vowel', 'R')
			},
			'q1':{
				'consonant': ('q3', tape_alphabet['other'][0]+'consonant', 'R'), 
				'vowel' : ('q7', tape_alphabet['other'][2], 'R')
			},
			'q2':{
				'consonant': ('q7', tape_alphabet['other'][2], 'R'), 
				'vowel' : ('q1', 'vowel', 'R')
			},
			'q3':{
				'consonant': ('q7', tape_alphabet['other'][2], 'R'), 
				'vowel' : ('q4', 'vowel', 'R')
			},
			'q4':{
				'consonant': ('q5', 'consonant', 'R'), 
				'vowel' : ('q7', tape_alphabet['other'][2], 'R'),
				tape_alphabet['other'][1]:('q6',  tape_alphabet['other'][2], 'R'),
				tape_alphabet['other'][2]:('q1',  tape_alphabet['other'][2], 'R'),
			},
			'q5':{
				tape_alphabet['other'][1]:('q6',  tape_alphabet['other'][2], 'R'),
				tape_alphabet['other'][2]:('q1',  tape_alphabet['other'][2], 'R'),
			}
	}
	blank='*' #Note: ne atayacagimi bilemedigim icin '*' atadim 
	print(transitions)
	nTuringMachine = TuringMachine(states, input_alphabet, tape_alphabet, blank, transitions, initial_state, accept_states, reject_states)
	while True:
	    word = input("Enter a word (or Press ENTER to quit): ")
	    if not word:
	        break
	    print("Your input:", word)
	    output=nTuringMachine.execute(word)
	    print("Turing Machine: ", output)
			

if __name__=='__main__':
	main()