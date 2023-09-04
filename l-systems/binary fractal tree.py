from turtle import *

axiom="0"

def rule(axiom):
	r=""
	for i in axiom:
		if i=="0":r+="1[0]0"
		if i=="1":r+="11"
		if i=="[":r+="["
		if i=="]":r+="]"	
	return r

speed(0)
left(90)
penup()
back(250)
pendown()
hideturtle()

p=[]
a=[]

for g in range(7):
	axiom=rule(axiom)

print(axiom)
for j in axiom:
	if j=="0" or j=="1":
		forward(3)
	if j=="[":
		p.append(pos())
		a.append(heading())
		left(45)
	if j=="]":
		penup()
		setpos(p.pop())
		setheading(a.pop())
		pendown()
		right(45)

done()