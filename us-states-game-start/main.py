import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
data = pandas.read_csv("50_states.csv")
screen.addshape(image)
turtle.shape(image)
states = data.state.to_list()
is_on = True
guessed = []
answer = screen.textinput(title="Guess the State", prompt="What's another state?").title()



while is_on:
    if len(guessed) < 50:
        if answer in states and answer not in guessed:
            guessed.append(answer)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer)
            answer = screen.textinput(title=f"{len(guessed)}/50", prompt="What's another state?").title()
        else:
            answer = screen.textinput(title=f"{len(guessed)}/50", prompt="What's another state?").title()
    else:
        is_on = False
screen.mainloop()
