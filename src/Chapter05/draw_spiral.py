import turtle


def draw_spiral(my_turtle: turtle.Turtle, line_len):
    if line_len > 0:
        turtle.width(width=5)
        turtle.forward(distance=line_len)
        turtle.right(angle=22.5)
        draw_spiral(my_turtle=t, line_len=line_len - 0.5)


t = turtle.Turtle()
my_window = turtle.Screen()
draw_spiral(my_turtle=t, line_len=150)
my_window.exitonclick()
