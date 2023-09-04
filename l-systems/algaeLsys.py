from turtle import *

axiom="A"

def rule(axiom):
	r=""
	for i in axiom:
		if i=="A":r+="AB"
		if i=="B":r+="A"
	return r

speed(0)
hideturtle()

for g in range(15):
	axiom=rule(axiom)

print(axiom)
for j in axiom:
	if j=="A":
		right(60)
		forward(20)
	if j=="B":
		left(60)
		forward(20)

done()