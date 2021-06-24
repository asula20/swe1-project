from tkinter import *
from sys import *
import os


def openGameTab():
    os.system('python games.py')


def openHomeTab():
    os.system('python main.py')

def openGame1():
    os.system('python game1.py')

def openGame2():
    os.system('python game2.py')

root = Tk()
root.title('Learn Python')
root.geometry("1645x928")

# Defining the image
background = PhotoImage(file="images/game_tab.png")
# Setting up the background
screen = Label(root, image=background)
screen.place(x=0, y=0, relwidth=1, relheight=1)

# Creating a canvas(for removing background color of buttons)
canvas = Canvas(root, width=800,height=500)
canvas.pack(fill="both",expand=True)

#Setting image for the canvas
canvas.create_image(0,0,image =background, anchor="nw")

#Button Images
home_btn= PhotoImage(file="images/home_btn.png")
games_btn=PhotoImage(file="images/games_btn.png")
quizzes_btn=PhotoImage(file="images/quizzes_btn.png")
forum_btn=PhotoImage(file="images/forum_btn.png")
start_game1=PhotoImage(file="images/start_btn.png")
start_game2=PhotoImage(file="images/start_btn.png")

#Adding buttons
button_home= Button(root,image =home_btn, text="Home",command= openHomeTab)
button_games= Button(root,image=games_btn, text="Games", command= openGameTab)
button_quizzes= Button(root,image=quizzes_btn, text="Quizzes")
button_forum= Button(root,image=forum_btn, text="Forum")
button_game1= Button(root,image=start_game1,command=openGame1,bg="#7a658c", borderwidth=0)
button_game2= Button(root,image=start_game2,command=openGame2,bg="#7a658c", borderwidth=0)


#Adding windows for the menu buttons
bh_window= canvas.create_window(477,-4, anchor="nw", window=button_home)
bg_window= canvas.create_window(658,-6, anchor="nw", window=button_games)
bq_window= canvas.create_window(867,-5, anchor="nw", window=button_quizzes)
bf_window= canvas.create_window(1084,-6, anchor="nw", window=button_forum)
btn_game1_window= canvas.create_window(295,550, anchor="nw", window=button_game1)
btn_game2_window= canvas.create_window(1070,550, anchor="nw", window=button_game2)
root.mainloop()
