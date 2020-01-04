#
#TicTacToe
#
# Imports
from tkinter import *
import tkinter.messagebox
window = Tk()

window.title("TicTacToe")  # title of the window
p1 = StringVar()
p2 = StringVar()

player1 = Label(window, text="Player1", font="Helvetica 14 bold")
player2 = Label(window, text="Player2", font="Helvetica 14 bold")
e1 = Entry(window, textvariable=p1)  # entry for player1's name
e2 = Entry(window, textvariable=p2)  # entry for player2's name

# Positioning Player, Labels and Entries
player1.grid(row=0)
player2.grid(row=1)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

#
# Functions
#

# Function that disables the buttons after the game ends


def disablebutton():
    b1.configure(state=DISABLED)
    b2.configure(state=DISABLED)
    b3.configure(state=DISABLED)
    b4.configure(state=DISABLED)
    b5.configure(state=DISABLED)
    b6.configure(state=DISABLED)
    b7.configure(state=DISABLED)
    b8.configure(state=DISABLED)
    b9.configure(state=DISABLED)

# Function for click reaction


bclick = 1
click_num = 0  # Variable to check for Tie


def click(button):
    global bclick, click_num, p1, p2, p1_text, p2_text
    if button["text"] == " " and bclick == 1:
        button["text"] = "X"
        bclick = 0
        click_num += 1
        win()
    elif button["text"] == " " and bclick == 0:
        button["text"] = "O"
        bclick = 1
        click_num += 1
        win()


def win():
    if (b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" or
       b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X" or
       b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" or
       b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" or
       b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X" or
       b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" or
       b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" or
       b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X"):
        disablebutton()
        p1_text = p1.get() + " Wins!"
        tkinter.messagebox.showinfo("TicTacToe", p1_text)
    elif (b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" or
         b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O" or
         b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O" or
         b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O" or
         b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O" or
         b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O" or
         b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O" or
         b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O"):
        disablebutton()
        p2_text = p2.get() + " Wins!"
        tkinter.messagebox.showinfo("TicTacToe", p2_text)
    elif click_num == 8:
        tkinter.messagebox.showinfo("TicTacToe", "Its a Tie!")


# To give space before the buttons
space = Label(window)
space.grid(row=3)

# Buttons Changing Values
b1 = Button(window, text=" ", height=4, width=12, font="Helvetica 18 bold", bg="gray", fg="white", command=lambda: click(b1))
b1.grid(row=4, column=0)
b2 = Button(window, text=" ", height=4, width=12, font="Helvetica 18 bold", bg="gray", fg="white", command=lambda: click(b2))
b2.grid(row=4, column=1)
b3 = Button(window, text=" ", height=4, width=12, font="Helvetica 18 bold", bg="gray", fg="white", command=lambda: click(b3))
b3.grid(row=4, column=2)
b4 = Button(window, text=" ", height=4, width=12, font="Helvetica 18 bold", bg="gray", fg="white", command=lambda: click(b4))
b4.grid(row=5, column=0)
b5 = Button(window, text=" ", height=4, width=12, font="Helvetica 18 bold", bg="gray", fg="white", command=lambda: click(b5))
b5.grid(row=5, column=1)
b6 = Button(window, text=" ", height=4, width=12, font="Helvetica 18 bold", bg="gray", fg="white", command=lambda: click(b6))
b6.grid(row=5, column=2)
b7 = Button(window, text=" ", height=4, width=12, font="Helvetica 18 bold", bg="gray", fg="white", command=lambda: click(b7))
b7.grid(row=6, column=0)
b8 = Button(window, text=" ", height=4, width=12, font="Helvetica 18 bold", bg="gray", fg="white", command=lambda: click(b8))
b8.grid(row=6, column=1)
b9 = Button(window, text=" ", height=4, width=12, font="Helvetica 18 bold", bg="gray", fg="white", command=lambda: click(b9))
b9.grid(row=6, column=2)
win()

window.mainloop()
#ysm