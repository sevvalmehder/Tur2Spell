



def main():
	vowels=input(' Enter vowels by space: ').split()
	consonants=input(' Enter consonants by space: ').split()
	print(vowels, consonants)
	alphabet=[]
	alphabet.append(vowels)
	alphabet.append(consonants)
	stringList=[]
	stringList.append("vowels")
	stringList.append("consonants")
	#dictionary
	myAlphabet=dict(zip(stringList, alphabet))
	print("alphabet:", myAlphabet)
	#define an object of Turing Machine
	#TuringMachine=TuringMachineClass(myAlphabet)
	while True:
	    word = input("Enter a word (or Press ENTER to quit): ")
	    if not word:
	        break
	    print("Your input:", word)
	    output="kkkkkk"
	    #output=TuringMachine.execute(word)
	    print("Turing Machine: ", output)



if __name__=='__main__':
	main()