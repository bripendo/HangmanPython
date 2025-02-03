import random as r

with open('list.txt', 'r') as plik:
	list = plik.readlines()
	list = [i.strip('\n') for i in list]

def Hangman():
	print("Guess the word!\nOnly the first character from input will matter.\nYou can also try to guess the word.")
	wordd = r.choice(list)
	word = [i for i in wordd]
	guess = ['_' for i in word]
	lifes = 10
	guessed = []
	print(f'   Chances: {lifes}\n   {" ".join(guess)}')
	while lifes > 0:
		char = input('   ')
		if char.lower() == wordd:
			print('You won!\n')
			lifes =-1
		elif len(char) > 2:
			char="-1"
		else:
				char = char[0:1]
		if char in word:
			for i in range(word.count(char)):
				guess[word.index(char)], word[word.index(char)] = word[word.index(char)], guess[word.index(char)] 
			print(f'   Chances: {lifes}\n   {" ".join(guess)}')
			guessed.append(char)
		elif char in guessed:
			print(f"You already tried {char.upper()}.")
		elif char == "-1":
			print("This answer is incorrect.")
		elif char.lower() == char.upper():
			print("This character is invalid.")
		elif lifes != -1:
			lifes -= 1
			print(f"Letter {char.upper()} is not in this word.\nChances left: {lifes}")
			guessed.append(char)
		if len(set(word)) == 1:
			print('You won!\n')
			lifes =-1
	if lifes == 0:
		print(f'You lost! The word was {wordd.capitalize()}.\n')

while True:
	Hangman()