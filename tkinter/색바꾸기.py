from tkinter import *

def entfg() :
  ent_text = entry.get()
  print(ent_text)
  label['fg'] = ent_text

win = Tk()

label = Label(win, text = "message",highlightcolor = 'yellow')
label.pack()

entry = Entry(win, text = "enter word",highlightcolor = 'yellow')
entry.pack()

button = Button(win, text = "OK", bg = "red", fg = 'white', highlightcolor = 'yellow',command = entfg)
button.pack()

win.mainloop()