import turtle
def draw_square(turtle_obj, size=100):
    for i in range(4):
        turtle_obj.forward(size)
        turtle_obj.left(90)



def draw_spiral(t):
    for i in range(100):
        t.forward(i)
        t.left(91)

    def main():
        t = turtle.Turtle()
        t.speed(1)
        draw_spiral(t)
        turtle.mainloop()

if __name__ == "__main__":
    main()

#########################################################################

age = int(input("Enter your age: "))

if age < 21:
    print("No you cannot")
elif age >= 65:
    print("You are too old")
else:
    print("Yes you can")


if score>= 80:
    print("B")
elif score >= 90:
    print("A")
elif score >= 70:
    print("C")
else:
    print("F")

