import pandas as pd
import turtle


data = pd.read_csv('50_states.csv')
print(data.set_index('state').to_dict())
states = data['state'].tolist()

screen = turtle.Screen()
screen.title('US state Game')
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
t = turtle.Turtle()
t.hideturtle()
t.penup()

c = 0
while len(states) > 0:
    a = screen.textinput(title=f"Guess the state ({c}/50)", prompt=" Enter state's names: ").title()

    if a in states:
        c+=1
        states.remove(a)
        x = data[data['state'] == a]['x'].values[0]
        y = data[data['state'] == a]['y'].values[0]
        print(x, y)
        t.goto(x, y)
        t.write(a, False, 'center', ('Arial', 10, 'normal'))
    else:
        print('Wrong input.')
        continue
