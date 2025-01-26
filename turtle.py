from turtle import Turtle, Screen

# Initialize the turtle and screen
sashu = Turtle()
sashu.shape("turtle")
sashu.color('blue')

while True:
    # Get the user's choice
    choose = input("Enter 1 to turn right\nEnter 2 to turn left\nEnter 3 to move forward\nEnter 4 to move backward\nEnter 0 to exit: ")

    # Handle each choice
    if choose == '3' or choose == '4':
        # Ask for the distance and convert it to a number
        distance = int(input("How far do you want Sashu to move? "))
        if choose == '3':
            sashu.forward(distance)
        elif choose == '4':
            sashu.backward(distance)
    elif choose == '1':
        # Turn right
        sashu.right(90)
    elif choose == '2':
        # Turn left
        sashu.left(90)
    elif choose == '0':
        break
    else:
        print("Invalid choice, please try again.")

# Keep the screen open until clicked
screen = Screen()
screen.title("HELLO")
screen.exitonclick()
