from turtle import *

axiom="F"

def rule(axiom):
	r=""
	for i in axiom:
		if i=="F":r+="F+F-F-F+F"
		if i=="+":r+="+"
		if i=="-":r+="-"	
	return r

penup()
back(125)
pendown()
speed(0)
hideturtle()

for g in range(3):
	axiom=rule(axiom)

print(axiom)
for j in axiom:
	if j=="F":
		forward(10)
	if j=="+":
		left(90)
	if j=="-":
		right(90)

done()