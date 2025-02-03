with open('list.txt', 'r') as plik:
	list = plik.readlines()
	list = [i.strip('\n') for i in list]
with open('list.txt','w') as popraw:
	list = set(list)
	for i in list:
		popraw.write(i+'\n')