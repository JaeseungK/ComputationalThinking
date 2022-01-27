import random

ev1_floor=random.randrange(1,46)
ev2_floor=random.randrange(1,46)
ev3_floor=random.randrange(1,46)

print("elevators are on floor:", ev1_floor, ev2_floor, ev3_floor)

ev_moving=['up', 'down', 'stay']

ev1_state=random.choice(ev_moving)
ev2_state=random.choice(ev_moving)
ev3_state=random.choice(ev_moving)

print("elevators are in state:", ev1_state, ev2_state, ev3_state)

from tkinter import *
root = Tk()
root.title("elevator")

label = Label(root, text="Please input your floor", fg="blue")
label.pack()

ent = Entry(root)
ent.pack()

def ent_f():
    me_floor=ent.get()
    print("I am on", me_floor,"th floor")

button = Button(root, text='OK', fg="red", command=ent_f)
button.pack()

root.mainloop()