from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("GUI")           # Title at the top of the window
root.geometry("500x500")    # Size of window
root.iconbitmap("c:/pythondev/gui/newicon.ico") #icon top left of window, replaces tkinter feather
root.option_add("*tearOff", False) #reviews - - - from top of menu

def blank_command():
    pass

# Menu Setup

menu_main = Menu(root)
root.config(menu=menu_main)

menu_file = Menu(menu_main)
menu_main.add_cascade(label="File", menu=menu_file)
menu_file.add_command(label="New", command=blank_command)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

# Functions
def clicked():
    global label_four
    answer_one = entry_one.get()
    label_four = Label(root, text="Hey, " + answer_one)
    label_four.pack()

def hide():
    label_four.pack_forget()


def show():
    label_four.pack()

# Add Images
# image_forest = ImageTk.PhotoImage(Image.open("forest.jpg"))
# label_forest = Label(image=image_forest)
# label_forest.pack()

# Labels
label_one = Label(root, text="App Header", fg="blue", bg="#00ffff", font=("TkDefaultFont",25), relief="ridge")
label_one.pack() #pack layout as appose to grid

label_two = Label(root, text="By Devon")
label_two.pack()

label_three = Label(root, text="Enter Your Name:")
label_three.pack()

# Entry Field
entry_one = Entry(root, width=25)
entry_one.pack()

# Buttons
button_submit = Button(root, text="Submit", command=clicked)
button_submit.pack(pady=10)

button_hide = Button(root, text="Hide", command=hide)
button_hide.pack(pady=10)

button_show = Button(root, text="Show", command=show)
button_show.pack(pady=10)













root.mainloop()