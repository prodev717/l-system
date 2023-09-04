from turtle import *

axiom="F"

def rule(axiom):
	r=""
	for i in axiom:
		if i=="F":r+="F+G"
		if i=="G":r+="F-G"
		if i=="+":r+="+"
		if i=="-":r+="-"	
	return r
	
speed(0)
hideturtle()

for g in range(12):
	axiom=rule(axiom)

print(axiom)
for j in axiom:
	if j=="F" or j=="G":
		forward(3)
	if j=="+":
		left(90)
	if j=="-":
		right(90)

done()