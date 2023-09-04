from turtle import *

axiom="X"

def rule(axiom):
	r=""
	for i in axiom:
		if i=="X":r+="F+[[X]-X]-F[-FX]+X"
		if i=="F":r+="FF"
		if i=="[":r+="["
		if i=="]":r+="]"
		if i=="+":r+="+"
		if i=="-":r+="-"	
	return r

speed(0)
left(90)
penup()
back(250)
pendown()
hideturtle()

p=[]
a=[]

for g in range(6):
	axiom=rule(axiom)

print(axiom)
for j in axiom:
	if j=="F":
		forward(3)
	if j=="[":
		p.append(pos())
		a.append(heading())
	if j=="]":
		penup()
		setpos(p.pop())
		setheading(a.pop())
		pendown()
	if j=="+":
		left(25)
	if j=="-":
		right(25)

done()