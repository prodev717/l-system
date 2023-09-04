from turtle import *

axiom="F-G-G"

def rule(axiom):
	r=""
	for i in axiom:
		if i=="F":r+="F-G+F+G-F"
		if i=="G":r+="GG"
		if i=="+":r+="+"
		if i=="-":r+="-"	
	return r

penup()
setpos(-115,100)
pendown()
speed(0)
hideturtle()

for g in range(3):
	axiom=rule(axiom)

print(axiom)
for j in axiom:
	if j=="F" or j=="G":
		forward(30)
	if j=="+":
		left(120)
	if j=="-":
		right(120)

done()