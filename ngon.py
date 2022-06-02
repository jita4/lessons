from turtle import forward, left, exitonclick
number=int(input("How many angles in n-gon?"))
for i in range(number):
    forward(50)
    left(180-180*(1-2/number) )
exitonclick()