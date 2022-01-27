 # A 

import random

ev1_floor = random.randint(1, 46)
ev2_floor = random.randint(1, 46)
ev3_floor = random.randint(1, 46)

floor = [ev1_floor, ev2_floor, ev3_floor]

ev_stance = ['up', 'down', 'stay']

ev1_stance = random.choice(ev_stance)
ev2_stance = random.choice(ev_stance)
ev3_stance = random.choice(ev_stance)

stance = [ev1_stance, ev2_stance, ev3_stance]

#======================================================

# B

while True:
    if (ev1_floor == 1 and ev1_stance == 'down') or (ev1_floor == 46 and ev1_stance == 'up'):
        ev1_stance == random.choice(ev_stance)
    elif (ev2_floor == 1 and ev2_stance == 'down') or (ev2_floor == 46 and ev2_stance == 'up'):
        ev2_stance = random.choice(ev_stance)
    elif (ev3_floor == 1 and ev3_stance == 'down') or (ev3_floor == 46 and ev3_stance == 'up'):
        ev3_stance = random.choice(ev_stance)
    else:
        break

print("엘리베이터 현재위치 =", floor)
print("엘리베이터 이동상태 =", stance)

arriv = ['', '', '']

for i in range(3):
    if stance[i] == 'up':
        arriv[i] = random.randint(floor[i] + 1, 46)
    elif stance[i] == 'down':
        arriv[i] = random.randint(1, floor[i] - 1)
    else:
        arriv[i] = floor[i]

print("엘리베이터 목적지 =", arriv)

#=====================================================

# C


def turnred():
    my_floor = int(input_window.get())

    if not (1 <= my_floor <= 46):
        messagebox.showerror('', "Invalid Floor")
        root.mainloop()

    print("내 위치 =", my_floor)

    t_list = []

    for i in range(3):
        if stance[i] == 'stay':
            t = abs(my_floor - floor[i])
        else:
            t = abs(floor[i] - arriv[i]) + abs(my_floor - arriv[i])

        t_list.append(t)

    print('걸리는 시간 =', t_list)

    for i in range(3):
        if t_list[i] == min(t_list):
            target_ev = 'EV' + str(i + 1)

    print('가장 빠른 엘리베이터 =', target_ev)

    for i in range(3):
        if t_list[i] == min(t_list):
            target_evnum = i

    floor_list[target_evnum].configure(fg='red')
    text_list[target_evnum].configure(fg='red')
    stance_list[target_evnum].configure(fg='red')


#=======================================================

# D

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("elevator")
root.geometry("170x100+100+100")
root.resizable(False, False)

# 엘리베이터 호기 텍스트
text1 = Label(root, text='EV1', width=5)
text2 = Label(root, text='EV2', width=5)
text3 = Label(root, text='EV3', width=5)

text1.grid(row=0, column=0)
text2.grid(row=0, column=1)
text3.grid(row=0, column=2)

# 엘리베이터 층수 텍스트

floor1 = Label(root, text=str(ev1_floor))
floor2 = Label(root, text=str(ev2_floor))
floor3 = Label(root, text=str(ev3_floor))

floor1.grid(row=1, column=0)
floor2.grid(row=1, column=1)
floor3.grid(row=1, column=2)

# 엘리베이터 상태 텍스트

icon_list = ['▲', '▼', '-']

stance_icon = []

for i in range(3):
    if stance[i] == 'up':
        icon = icon_list[0]
    elif stance[i] == 'down':
        icon = icon_list[1]
    elif stance[i] == 'stay':
        icon = icon_list[2]

    stance_icon.append(icon)

print(stance_icon)

stance1 = Label(root, text=stance_icon[0])
stance2 = Label(root, text=stance_icon[1])
stance3 = Label(root, text=stance_icon[2])

stance1.grid(row=2, column=0)
stance2.grid(row=2, column=1)
stance3.grid(row=2, column=2)

input_window = Entry(root, width=5)
input_window.grid(row=3, column=1)

text_list = [text1, text2, text3]
floor_list = [floor1, floor2, floor3]
stance_list = [stance1, stance2, stance3]
button1 = Button(root, width=5, text="CALL", overrelief="solid", command=turnred)
button1.grid(row=3, column=2)

root.mainloop()
