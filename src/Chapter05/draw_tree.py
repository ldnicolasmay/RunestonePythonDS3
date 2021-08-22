import turtle
from random import randrange


def draw_tree(branch_len: float, t: turtle.Turtle):
    if branch_len > 5:
        t.width(width=int(branch_len) // 10)
        t.pencolor((0.15, (150 - branch_len) / 150, 0.25))
        t.forward(branch_len)
        t.right(20)
        draw_tree(branch_len=branch_len - 15, t=t)
        t.left(40)
        draw_tree(branch_len=branch_len - 15, t=t)
        t.right(20)
        t.penup()
        t.backward(branch_len)
        t.pendown()


def draw_randomish_tree(branch_len: float, t: turtle.Turtle):
    if branch_len > 5:
        branch_len = branch_len + randrange(0, 10)
        turn_angle_1 = randrange(5, 55)
        turn_angle_2 = randrange(5, 55)
        t.width(width=int(branch_len) // 10)
        t.pencolor((0.15, (150 + 10 - branch_len) / (150 + 10), 0.25))
        t.forward(branch_len)
        t.right(turn_angle_1)
        draw_randomish_tree(branch_len=branch_len - 15, t=t)
        t.left(turn_angle_1 + turn_angle_2)
        draw_randomish_tree(branch_len=branch_len - 15, t=t)
        t.right(turn_angle_2)
        t.penup()
        t.backward(branch_len)
        t.pendown()


def main():
    t = turtle.Turtle()
    s = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    # draw_tree(150, t)
    # draw_randomish_tree(150, t)
    draw_randomish_tree(75, t)
    s.exitonclick()


main()
