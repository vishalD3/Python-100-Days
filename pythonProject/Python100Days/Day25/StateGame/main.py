import turtle
import pandas


screen = turtle.Screen()
screen.title("India State Games")
screen.setup(700,675)
#screen.setup(1000,800)
img = "states.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("statelist.csv")
all_states = data.states.to_list()
guessed_states = []

while len(guessed_states) < 37:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/37 State Guess Correct!",
                                    prompt="What's another state name are ? ").title()
    #print(answer_state)

    if answer_state == "Exit":
        # missing_state = []
        # for state in  all_states:
        #     if state not in guessed_states:
        #         missing_state.append(state)

        #print(missing_state)
        missing_state = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("States_to_Learn.csv")
        break

    # if answer_state  is one of the state in all states of the 36 state.csv
        #if they  got it right:
            #create turtle to write the name of the state at the state's x and y cor

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.states == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)

