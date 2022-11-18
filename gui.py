from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("GUI")           # Title at the top of the window
root.geometry("500x500")    # Size of window
root.iconbitmap("c:/pythondev/gui/newicon.ico") #icon top left of window, replaces tkinter feather
root.option_add("*tearOff", False) #removes tearoff from top of menu


# Functions
def clicked():
    global label_greeting
    answer_one = entry_name.get()
    label_greeting = Label(root, text="Hey, " + answer_one)
    label_greeting.pack()

def hide():
    label_greeting.pack_forget() #Hides label_greeting

def show():
    label_greeting.pack()

def blank_command():
    label_blank = Label(root, text="Woo! Menu items rock!")
    label_blank.pack()

def new():
    hide_menu_frames()
    label_name_prompt.pack()
    entry_name.pack()
    frame_file_new.pack(pady=5)

def flux():
    hide_menu_frames()
    frame_settings_flux.pack(pady=5)

def hide_menu_frames():
    label_name_prompt.pack_forget()
    entry_name.pack_forget()
    frame_file_new.pack_forget()
    frame_settings_flux.pack_forget()


### Menu Setup ###

# Main Menu - Holds all of the menu items and sub menus
menu_main = Menu(root) # puts a Menu widget in the root and assigns it to menu_main
root.config(menu=menu_main)


# File Menu
menu_file = Menu(menu_main)
menu_main.add_cascade(label="File", menu=menu_file)

menu_file.add_command(label="New", command=new)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)


# Settings Menu
menu_settings = Menu(menu_main)
menu_main.add_cascade(label="Settings", menu=menu_settings)

menu_settings.add_command(label="Flux Capacitance", command=flux)
menu_settings.add_command(label="Brightness", command=blank_command)
menu_settings.add_command(label="Sound", command=blank_command)


# Labels
label_header = Label(root, text="App Header", fg="blue", bg="#00ffff", font=("TkDefaultFont",25), relief="ridge", width=100)
label_intro = Label(root, text="Go to File > New to get started.")
label_name_prompt = Label(root, text="Enter Your Name:")

label_header.pack() #pack layout as appose to grid
label_intro.pack(pady=5)


# Entry Field
entry_name = Entry(root, width=25)


# Frame - File/New
frame_file_new = Frame(root, width=200, height=200, bd=4, bg="blue", relief="sunken")


# Frame - Settings/Flux
frame_settings_flux = Frame(root, width=200, height=200, bd=4, bg="blue", relief="sunken")

label_settings_flux = Label(frame_settings_flux, text="Flux Frame")
label_settings_flux.pack(padx=10, pady=10)


# Buttons - File/New
button_submit = Button(frame_file_new, text="Submit", command=clicked)
button_hide = Button(frame_file_new, text="Hide", command=hide)
button_show = Button(frame_file_new, text="Show", command=show)

button_submit.grid(row=0,column=0, columnspan=3, padx=1, pady=1)
button_hide.grid(row=1,column=1, padx=1)
button_show.grid(row=1,column=2, padx=1)



# Add Images
# image_forest = ImageTk.PhotoImage(Image.open("forest.jpg"))
# label_forest = Label(image=image_forest)
# label_forest.pack()












root.mainloop()