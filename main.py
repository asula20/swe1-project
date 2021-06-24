from tkinter import *
from sys import *
import os
import json

def openGameTab():
    os.system('python games.py')


def openHomeTab():
    os.system('python main.py')

def openQuzzesTab():
    os.system('python quizzes.py')

def openForumTab():
    os.system('python forum.py')
progress=0
def clickBtn():
   global progress
   progress = progress + 17
   if progress>100:
       progress=100

   canvas.itemconfigure(a, text=str(progress)+ " %")

root = Tk()
root.title('Learn Python')
root.geometry("1645x928")

with open('did_u_know.json') as f:
    data = json.load(f)

# Defining the image
background = PhotoImage(file="images/bg.png")
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
c1_img=PhotoImage(file="images/chapter1.png")
c2_img=PhotoImage(file="images/chapter2.png")
c3_img=PhotoImage(file="images/chapter3.png")
c4_img=PhotoImage(file="images/chapter4.png")
c5_img=PhotoImage(file="images/chapter5.png")
c6_img=PhotoImage(file="images/chapter6.png")


#Adding buttons
button_home= Button(root,image =home_btn, text="Home",command= openHomeTab)
button_games= Button(root,image=games_btn, text="Games", command= openGameTab)
button_quizzes= Button(root,image=quizzes_btn, text="Quizzes",command=openQuzzesTab)
button_forum= Button(root,image=forum_btn, text="Forum",command=openForumTab)

button_c1= Button(root,image=c1_img,borderwidth=0, command=clickBtn)

button_c2= Button(root,image=c2_img,borderwidth=0,command=clickBtn)
button_c3= Button(root,image=c3_img,borderwidth=0,command=clickBtn)
button_c4= Button(root,image=c4_img,borderwidth=0,command=clickBtn)
button_c5= Button(root,image=c5_img,borderwidth=0,command=clickBtn)
button_c6= Button(root,image=c6_img,borderwidth=0,command=clickBtn)


#Adding Lable texts
canvas.create_text(869,176,text="The basics",font=("Sans Serif",24), fill="white")
canvas.create_text(924,756,text="Conditional Loops",font=("Sans Serif",24), fill="white")
canvas.create_text(1168,340,text="Conditional Logic",font=("Sans Serif",24), fill="white")
canvas.create_text(1118,630,text="Variables",font=("Sans Serif",24), fill="white")
canvas.create_text(342,340,text="Expressions",font=("Sans Serif",24), fill="white")
canvas.create_text(285,630,text="Loops and Patterns",font=("Sans Serif",24), fill="white")
canvas.create_text(1470,620,text="Guido van Rossum was looking for\n an interesting project to keep\n him occupied during Christmas\n so he created Python.",font=("Sans Serif",14), fill="black")


progress_txt= "0 %"
a= canvas.create_text(740,500,text=progress_txt,font=("Sans Serif",64), fill="gray")


#Adding windows for the menu buttons
bh_window= canvas.create_window(477,-4, anchor="nw", window=button_home)
bg_window= canvas.create_window(658,-6, anchor="nw", window=button_games)
bq_window= canvas.create_window(867,-5, anchor="nw", window=button_quizzes)
bf_window= canvas.create_window(1084,-6, anchor="nw", window=button_forum)

c1_window= canvas.create_window(685,140, anchor="nw", window=button_c1)
c2_window= canvas.create_window(436,290, anchor="nw", window=button_c2)
c3_window= canvas.create_window(940,290, anchor="nw", window=button_c3)
c4_window= canvas.create_window(453,587, anchor="nw", window=button_c4)
c5_window= canvas.create_window(940,580, anchor="nw", window=button_c5)
c6_window= canvas.create_window(685,706, anchor="nw", window=button_c6)



root.mainloop()
