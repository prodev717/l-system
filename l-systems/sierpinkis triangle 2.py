from turtle import *

axiom="A"

def rule(axiom):
	r=""
	for i in axiom:
		if i=="A":r+="B-A-B"
		if i=="B":r+="A+B+A"
		if i=="+":r+="+"
		if i=="-":r+="-"	
	return r

penup()
setpos(-150,125)
pendown()
speed(0)
hideturtle()

for g in range(5):
	axiom=rule(axiom)

print(axiom)
for j in axiom:
	if j=="A" or j=="B":
		forward(10)
	if j=="+":
		left(60)
	if j=="-":
		right(60)

done()