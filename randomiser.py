import random

plist = []
plist = open("Pokemon list.txt", "r").read().split("\n")
print(plist)
random.shuffle(plist)
num = eval(input("Enter number of players: "))

Players_list = []
for i in range(num):
	Players_list.append(plist[i*4:(i+1)*4])

print(Players_list)	

