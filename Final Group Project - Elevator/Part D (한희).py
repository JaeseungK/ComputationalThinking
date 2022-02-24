from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("elevator")
root.geometry("170x100+100+100")
root.resizable(False, False)

# 엘레베이터 호기 텍스트
text1 = Label(root, text = 'EV1', width=5)
text2 = Label(root, text = 'EV2', width=5)
text3 = Label(root, text = 'EV3', width=5)

text1.grid(row=0, column=0)
text2.grid(row=0, column=1)
text3.grid(row=0, column=2)


# 엘레베이터 층수 텍스트

floor1 = Label(root, text =str(ev1_floor))
floor2 = Label(root, text =str(ev2_floor))
floor3 = Label(root, text =str(ev3_floor))

floor1.grid(row=1, column=0)
floor2.grid(row=1, column=1)
floor3.grid(row=1, column=2)

# 엘레베이터 상태 텍스트

icon_list = ['▲','▼','-']

stance_icon = []

for i in range (3) :
  if stance[i] == 'up' :
    icon = icon_list[0]
  elif stance[i] == 'down' :
    icon = icon_list[1]
  elif stance[i] == 'stay' :
    icon = icon_list[2]
  
  stance_icon.append(icon)

print(stance_icon)

stance1 = Label(root, text = stance_icon[0])
stance2 = Label(root, text = stance_icon[1])
stance3 = Label(root, text = stance_icon[2])

stance1.grid(row=2, column=0)
stance2.grid(row=2, column=1)
stance3.grid(row=2, column=2)

input_window = Entry(root, width=5)
input_window.grid(row=3, column=1)

text_list = [text1, text2, text3]
floor_list = [floor1, floor2, floor3]
stance_list = [stance1, stance2, stance3]
button1 = Button(root, width=5, text = "CALL", overrelief="solid", command = turnred)
button1.grid(row=3, column=2)

root.mainloop()
