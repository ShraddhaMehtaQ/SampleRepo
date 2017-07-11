letter = raw_input("Input a letter of the alphabet: ")
letter = letter.lower()
if(letter in 'aeiou'):
	print letter," is a vowel"
else:
	print letter," is a consonant"