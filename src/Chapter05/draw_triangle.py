import turtle

from typing import List, Tuple


def draw_triangle(points, color, my_turtle: turtle.Turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()


def get_mid(p1: Tuple[float, float], p2: Tuple[float, float]) -> Tuple[float, float]:
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def sierpinski(points: List[Tuple[float, float]], degree: int, my_turtle: turtle.Turtle) -> None:
    # colormap = ["red", "orange", "yellow", "green", "blue", "violet", "white"]
    colormap = ["#eeeeee", "#cccccc", "#aaaaaa", "#888888", "#666666", "#444444", "#222222"]
    draw_triangle(points, colormap[degree], my_turtle)
    if degree > 0:
        sierpinski(
            points=[points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])],
            degree=degree - 1,
            my_turtle=my_turtle,
        )
        sierpinski(
            points=[points[1], get_mid(points[1], points[2]), get_mid(points[0], points[1])],
            degree=degree - 1,
            my_turtle=my_turtle,
        )
        sierpinski(
            points=[points[2], get_mid(points[0], points[2]), get_mid(points[1], points[2])],
            degree=degree - 1,
            my_turtle=my_turtle,
        )


def main():
    my_turtle = turtle.Turtle()
    my_window = turtle.Screen()
    my_points = [(-180, -150), (0, 150), (180, -150)]
    sierpinski(points=my_points, degree=3, my_turtle=my_turtle)
    my_window.exitonclick()


if __name__ == "__main__":
    main()
