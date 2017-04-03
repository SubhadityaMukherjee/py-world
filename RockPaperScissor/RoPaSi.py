import os
os.system('color F0')
w = 0
l = 0
d = 0
t = w+l+d
print "Okay, Lets play Rock, Paper, Scissors... You know the rules..."
while True:
	import random
	n = random.randint(1,3)
	if n == 1:
		n = "r"
		a = "Rock"
	elif n == 2:
		n = "p"
		a = "Paper"
	elif n == 3:
		n = "s"
		a = "Scissors"

	u = raw_input("Enter r for rock, p for paper or s for scissor. And d when you are done.")
	if u == "r" and n == "r":
		print "I choose", a
		x = "Draw"
		print x
	elif u == "r" and n == "p":
		print "I choose", a
		x = "You You Win This Time"
		print x
	elif u == "r" and n == "s":
		print "I choose", a
		x = "You Lose"
		print x
	elif u == "p" and n == "r":
		print "I choose", a
		x = "You Lose"
		print x
	elif u == "p" and n == "p":
		print "I choose", a
		x = "Draw"
		print x
	elif u == "p" and n == "s":
		print "I choose", a
		x = "You You Win This Time"
		print x
	elif u == "s" and n == "r":
		print "I choose", a
		x = "You You Win This Time"
		print x
	elif u == "s" and n == "p":
		print "I choose", a
		x = "You Lose"
		print x
	elif u == "s" and n == "s":
		print "I choose", a
		x = "Draw"
		print x
	elif u == 'd':
                break
	else:
		x = "Play properly dude"
		print x
		
		
	if x == "Draw":
		d+=1
		t += 1
	elif x == "You You Win This Time":
		w+=1
		t+=1
	elif x == "You Lose":
		l+=1
		t+=1
	elif x == "Play properly dude":
		t +=1

	print "Lose:",l, " ", "Win:", w, "  ", "Draw:"," ", d, "Total:"," ", t

