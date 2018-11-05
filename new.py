with open('balance.txt','r') as f:
	balance = 0
	for line in f:
		item = line.rstrip().split()
		if item[0] == 'D':
			balance += int(item[1])
		else:
			balance -= int(item[1])

print(balance)
