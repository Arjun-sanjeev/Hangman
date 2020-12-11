import random
from words import words
import string

# Get a valid(without '-' or spaces) word from the given words
def get_valid_word():
	word = random.choice(words) # Randomly chooses a word from the given list

	while '-' in word or ' ' in word:
		word = random.choice(words)
	return(word.upper())

def hangman():

	word = get_valid_word()
	word_letters = set(word)
	alphabet_letters = set(string.ascii_uppercase)
	used_letters = set()
	

	while len(word_letters)>0: #Iterates untill all the letters are found

		#Already used letters
		print("Used words : ", ' '.join(used_letters))
		word_list = []
		#Words found till now  
		'''
		print(word_list)
		for letter in word:
			if letter in used_letters:
				word_list.append(letter)
			else:
				word_list.append('-')
		'''

		word_list = [letter if letter in used_letters else '-' for letter in word]


		print("Current word :", ' '.join(word_list))


		user_input = input("Enter your letter: ").upper()

		if user_input in alphabet_letters - used_letters: #Checks if input is an alphabet and is not already used
			used_letters.add(user_input)
			

			if user_input in word_letters: #Checks is guessed letter is inthe word
				word_letters.remove(user_input)

		elif user_input in used_letters:
			print("Character already used! Please try again! ")

		else:
			print("Invalid Character! ")
		print(used_letters)

	print("Congrats! You have found the word ",word)

hangman()


