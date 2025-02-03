import random as r

with open('list.txt', 'r') as plik:
	list = plik.readlines()
	list = [i.strip('\n') for i in list]
print("Guess the word! (only the first character from input will be counted)")
wordd = r.choice(list)
word = [i for i in wordd]
guess = ['_' for i in word]
lifes = 10
guessed = []
print(f'   Chances: {lifes}\n   {" ".join(guess)}')

while lifes > 0:
	char = input().lower()[0:1]
	if char in word:
		for i in range(word.count(char)):
			guess[word.index(char)], word[word.index(char)] = word[word.index(char)], guess[word.index(char)] 
		print(f'   Chances: {lifes}\n   {" ".join(guess)}')
		guessed.append(char)
	elif char in guessed:
		print(f"You already tried {char.upper()}.")
	else:
		lifes -= 1
		print(f"Letter {char.upper()} is not in this word.\nChances left: {lifes}")
		guessed.append(char)
	if len(set(word)) == 1:
		print('You won!')
print(f'You lost! The word was {wordd}.')
