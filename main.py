from tkinter import *

root = Tk()
root.title('Learn Python')
root.geometry("1645x928")

# Defining the image
background = PhotoImage(file="images/bg.PNG")
# Setting up the background
screen = Label(root, image=background)
screen.place(x=0, y=0, relwidth=1, relheight=1)

# Creating a canvas(for removing background color of buttons)
canvas = Canvas(root, width=800,height=500)
canvas.pack(fill="both",expand=True)

#Setting image for the canvas
canvas.create_image(0,0,image =background, anchor="nw")

#Button Images
home_btn= PhotoImage(file="images/home_btn.PNG")
games_btn=PhotoImage(file="images/games_btn.PNG")
quizzes_btn=PhotoImage(file="images/quizzes_btn.PNG")
forum_btn=PhotoImage(file="images/forum_btn.PNG")

#Adding buttons
button_home= Button(root,image =home_btn, text="Home")
button_games= Button(root,image=games_btn, text="Games")
button_quizzes= Button(root,image=quizzes_btn, text="Quizzes")
button_forum= Button(root,image=forum_btn, text="Forum")

#Adding Lable texts
canvas.create_text(868,180,text="The basics",font=("Sans Serif",24), fill="white")


bh_window= canvas.create_window(477,-4, anchor="nw", window=button_home)
bg_window= canvas.create_window(658,-6, anchor="nw", window=button_games)
bq_window= canvas.create_window(867,-5, anchor="nw", window=button_quizzes)
bf_window= canvas.create_window(1084,-6, anchor="nw", window=button_forum)



root.mainloop()
