import turtle 

window = turtle.Screen()
window.bgcolor("red")


def draw_petals():
	sophia = turtle.Turtle() 
	sophia.shape("triangle")
	sophia.color("yellow")

	sophia.right(90)
	sophia.forward(500)
	sophia.backward(500)
	sophia.left(90)


	for i in range(1, 37): 
		sophia.left(120)
		sophia.forward(100)
		sophia.right(60)
		sophia.forward(100)
		sophia.right(120)
		sophia.forward(100)
		sophia.right(60)
		sophia.forward(100)
		sophia.right(130)


	
#draw_flower()
draw_petals()
window.exitonclick()
