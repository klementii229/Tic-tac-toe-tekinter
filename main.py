from tkinter import *
from tkinter import ttk
import tkinter as tk
from dadada import buttons



window = Tk()
window.title("Crestiki-noliki")
window.geometry("520x560")
window.iconbitmap(default="icon.ico")
clic = 0








def on_button_click0():
    global clic
    global buttons
    if clic % 2 == 0:
      buttons[0]["text"] = "X"
      clic += 1
      winlose012()
      winlose048()
      winlose036()

    else:
        buttons[0]["text"] = "O"
        clic += 1
        winlose012()
        winlose048()
        winlose036()
def on_button_click1():
    global clic
    global buttons
    if clic % 2 == 0:
      buttons[1]["text"] = "X"
      clic += 1
      winlose012()
    else:
        buttons[1]["text"] = "O"
        clic += 1
        winlose012()
def on_button_click2():
    global clic
    global buttons
    if clic % 2 == 0:
      buttons[2]["text"] = "X"
      clic += 1
      winlose012()
      winlose246()
      winlose258()
    else:
        buttons[2]["text"] = "O"
        clic += 1
        winlose012()
        winlose246()
        winlose258()
def on_button_click3():
    global clic
    global buttons
    if clic % 2 == 0:
      buttons[3]["text"] = "X"
      clic += 1
      winlose345()
      winlose036()
    else:
        buttons[3]["text"] = "O"
        clic += 1
        winlose345()
        winlose036()
def on_button_click4():
    global clic
    global buttons
    if clic % 2 == 0:
      buttons[4]["text"] = "X"
      clic += 1
      winlose345()
      winlose048()
      winlose246()
      winlose147()
    else:
        buttons[4]["text"] = "O"
        clic += 1
        winlose345()
        winlose048()
        winlose246()
        winlose147()
def on_button_click5():
    global clic
    global buttons
    if clic % 2 == 0:
      buttons[5]["text"] = "X"
      clic += 1
      winlose345()
      winlose258()

    else:
        buttons[5]["text"] = "O"
        clic += 1
        winlose345()
        winlose258()
def on_button_click6():
    global clic
    global buttons
    if clic % 2 == 0:
      buttons[6]["text"] = "X"
      clic += 1
      winlose678()
      winlose246()
      winlose036()
    else:
        buttons[6]["text"] = "O"
        clic += 1
        winlose678()
        winlose246()
        winlose036()
def on_button_click7():
    global clic
    global buttons
    if clic % 2 == 0:
      buttons[7]["text"] = "X"
      clic += 1
      winlose678()
      winlose147()
    else:
        buttons[7]["text"] = "O"
        clic += 1
        winlose678()
        winlose147()
def on_button_click8():
    global clic
    global buttons
    if clic % 2 == 0:
      buttons[8]["text"] = "X"
      clic += 1
      winlose678()
      winlose048()
      winlose258()
    else:
        buttons[8]["text"] = "O"
        clic += 1
        winlose678()
        winlose048()
        winlose258()




buttons[0] = tk.Button(window, text="", font=("Arial", 20), width=10, height=5, command= on_button_click0)
buttons[0].grid(row=0, column=0)

buttons[1] = tk.Button(window, text="", font=("Arial", 20), width=10, height=5, command= on_button_click1)
buttons[1].grid(row=0, column=1)

buttons[2] = tk.Button(window, text="", font=("Arial", 20), width=10, height=5, command= on_button_click2)
buttons[2].grid(row=0, column=2)

buttons[3] = tk.Button(window, text="", font=("Arial", 20), width=10, height=5, command= on_button_click3)
buttons[3].grid(row=1, column = 0)

buttons[4] = tk.Button(window, text="", font=("Arial", 20), width=10, height=5, command= on_button_click4)
buttons[4].grid(row=1, column=1)

buttons[5] = tk.Button(window, text="", font=("Arial", 20), width=10, height=5, command= on_button_click5)
buttons[5].grid(row=1, column=2)

buttons[6] = tk.Button(window, text="", font=("Arial", 20), width=10, height=5, command= on_button_click6)
buttons[6].grid(row=2, column=0)

buttons[7] = tk.Button(window, text="", font=("Arial", 20), width=10, height=5, command= on_button_click7)
buttons[7].grid(row=2, column=1)

buttons[8] = tk.Button(window, text="", font=("Arial", 20), width=10, height=5, command= on_button_click8)
buttons[8].grid(row=2, column=2)


def winlose012():
    if buttons[0]["text"] == buttons[1]["text"] == buttons[2]["text"]:
        print("Победа")
        #root = Tk()
        #root.title("Crestiki-noliki")
        #root.geometry("300x300")
        #label = ttk.Label(text="Hello METANIT.COM", font=("Arial", 14))
        #label.pack()
        #dont work
        #i dont undertstand

def winlose345():
    if buttons[3]["text"] == buttons[4]["text"] == buttons[5]["text"]:
        print("Победа")

def winlose678():
    if buttons[6]["text"] == buttons[7]["text"] == buttons[8]["text"]:
        print("Победа")

def winlose048():
    if buttons[0]["text"] == buttons[4]["text"] == buttons[8]["text"]:
        print("Победа")

def winlose246():
    if buttons[2]["text"] == buttons[4]["text"] == buttons[6]["text"]:
        print("Победа")

def winlose036():
    if buttons[0]["text"] == buttons[3]["text"] == buttons[6]["text"]:
        print("Победа")

def winlose147():
    if buttons[1]["text"] == buttons[4]["text"] == buttons[7]["text"]:
        print("Победа")


def winlose258():
    if buttons[2]["text"] == buttons[5]["text"] == buttons[8]["text"]:
        print("Победа")










#def zxc():
 #   global i
  #  for i in range(3):
   #     if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"]:
    #        return True
     #   if buttons[0][0] == buttons[1][1] == buttons[2][2]:
      #      return True
       # if buttons[0][2] == buttons[1][1] == buttons[2][0]:
        #    return True
#for i in range(3):
 #   for j in range(3):
  #      buttons[i][j] = tk.Button(window, text="", font=("Arial", 20), width=10, height=5, command=lambda row=i, col=j: on_button_click(row, col))
   #     buttons[i][j].grid(row=i, column=j)




#zxc()
#if zxc == True:
 #   print("win")


window.mainloop()