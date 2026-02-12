import turtle

def draw_square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)

def main():
    t = turtle.Turtle()
    t.speed(1)
    draw_square(t)
    draw_square(t, size=50)
    turtle.mainloop()

if __name__ == "__main__":
    main()

def draw_spiral(t):
    draw_square(t, size=50)
    t.left(10)
    draw_square(t, size=50)
    t.left(10)
    draw_square(t, size=50)
    t.left(10)
    draw_square(t, size=50)
    t.left(10)

def main():
    t = turtle.Turtle()
    t.speed(1)
    draw_spiral(t)
    turtle.mainloop()
