from tkinter import *

root = Tk()
root.title("Conversion Calculator")           
root.geometry("400x300")
root.iconbitmap("c:/pythondev/gui/icon-calculator.ico")

# FUNCTIONS #

def measure_calc(entry_length_1 = 1.0):
    entry_answer1 = entry_length_1

    ### INCHES ###
    if dd_length_c1.get() == "Inches" and dd_length_c2.get() == "Feet":
        destroy_frame()
        final_length = float(entry_answer1) / 12
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()
        
    elif dd_length_c1.get() == "Inches" and dd_length_c2.get() == "Yards":
        destroy_frame()
        final_length = float(entry_answer1) / 36
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()
  
    elif dd_length_c1.get() == "Inches" and dd_length_c2.get() == "Miles":
        destroy_frame()
        final_length = float(entry_answer1) / 63360
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Inches" and dd_length_c2.get() == "Centimeters":
        destroy_frame()
        final_length = float(entry_answer1) * 2.54
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Inches" and dd_length_c2.get() == "Meters":
        destroy_frame()
        final_length = float(entry_answer1) / 39.37
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Inches" and dd_length_c2.get() == "Kilometers":
        destroy_frame()
        final_length = float(entry_answer1) / 39370
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    ### FEET ###
    elif dd_length_c1.get() == "Feet" and dd_length_c2.get() == "Inches":
        destroy_frame()
        final_length = float(entry_answer1) * 12
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Feet" and dd_length_c2.get() == "Yards":
        destroy_frame()
        final_length = float(entry_answer1) / 3
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Feet" and dd_length_c2.get() == "Miles":
        destroy_frame()
        final_length = float(entry_answer1) / 5280
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Feet" and dd_length_c2.get() == "Centimeters":
        destroy_frame()
        final_length = float(entry_answer1) * 30.48
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Feet" and dd_length_c2.get() == "Meters":
        destroy_frame()
        final_length = float(entry_answer1) / 3.281
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Feet" and dd_length_c2.get() == "Kilometers":
        destroy_frame()
        final_length = float(entry_answer1) / 3281
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    ### YARDS ###
    elif dd_length_c1.get() == "Yards" and dd_length_c2.get() == "Inches":
        destroy_frame()
        final_length = float(entry_answer1) * 36
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Yards" and dd_length_c2.get() == "Feet":
        destroy_frame()
        final_length = float(entry_answer1) * 3
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Yards" and dd_length_c2.get() == "Miles":
        destroy_frame()
        final_length = float(entry_answer1) / 1760
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Yards" and dd_length_c2.get() == "Centimeters":
        destroy_frame()
        final_length = float(entry_answer1) * 91.44
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Yards" and dd_length_c2.get() == "Meters":
        destroy_frame()
        final_length = float(entry_answer1) / 1.094
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Yards" and dd_length_c2.get() == "Kilometers":
        destroy_frame()
        final_length = float(entry_answer1) / 1094
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    ### MILES ###
    elif dd_length_c1.get() == "Miles" and dd_length_c2.get() == "Inches":
        destroy_frame()
        final_length = float(entry_answer1) * 63360
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Miles" and dd_length_c2.get() == "Feet":
        destroy_frame()
        final_length = float(entry_answer1) * 5280
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Miles" and dd_length_c2.get() == "Yards":
        destroy_frame()
        final_length = float(entry_answer1) * 1760
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Miles" and dd_length_c2.get() == "Centimeters":
        destroy_frame()
        final_length = float(entry_answer1) * 160900
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Miles" and dd_length_c2.get() == "Meters":
        destroy_frame()
        final_length = float(entry_answer1) * 1609
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Miles" and dd_length_c2.get() == "Kilometers":
        destroy_frame()
        final_length = float(entry_answer1) * 1.609
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    ### CENTIMETERS ###
    elif dd_length_c1.get() == "Centimeters" and dd_length_c2.get() == "Inches":
        destroy_frame()
        final_length = float(entry_answer1) / 2.54
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Centimeters" and dd_length_c2.get() == "Feet":
        destroy_frame()
        final_length = float(entry_answer1) / 30.48
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Centimeters" and dd_length_c2.get() == "Yards":
        destroy_frame()
        final_length = float(entry_answer1) / 91.44
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Centimeters" and dd_length_c2.get() == "Miles":
        destroy_frame()
        final_length = float(entry_answer1) / 160900
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Centimeters" and dd_length_c2.get() == "Meters":
        destroy_frame()
        final_length = float(entry_answer1) / 100
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Centimeters" and dd_length_c2.get() == "Kilometers":
        destroy_frame()
        final_length = float(entry_answer1) / 100000
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    ### METERS ###
    elif dd_length_c1.get() == "Meters" and dd_length_c2.get() == "Inches":
        destroy_frame()
        final_length = float(entry_answer1) * 39.37
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Meters" and dd_length_c2.get() == "Feet":
        destroy_frame()
        final_length = float(entry_answer1) * 3.281
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Meters" and dd_length_c2.get() == "Yards":
        destroy_frame()
        final_length = float(entry_answer1) * 1.094
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Meters" and dd_length_c2.get() == "Miles":
        destroy_frame()
        final_length = float(entry_answer1) / 1609
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Meters" and dd_length_c2.get() == "Centimeters":
        destroy_frame()
        final_length = float(entry_answer1) * 100
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Meters" and dd_length_c2.get() == "Kilometers":
        destroy_frame()
        final_length = float(entry_answer1) / 1000
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    ### KILOMETERS ###
    elif dd_length_c1.get() == "Kilometers" and dd_length_c2.get() == "Inches":
        destroy_frame()
        final_length = float(entry_answer1) * 39370
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Kilometers" and dd_length_c2.get() == "Feet":
        destroy_frame()
        final_length = float(entry_answer1) * 3281
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Kilometers" and dd_length_c2.get() == "Yards":
        destroy_frame()
        final_length = float(entry_answer1) * 1094
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Kilometers" and dd_length_c2.get() == "Miles":
        destroy_frame()
        final_length = float(entry_answer1) / 1.609
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Kilometers" and dd_length_c2.get() == "Centimeters":
        destroy_frame()
        final_length = float(entry_answer1) * 100000
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Kilometers" and dd_length_c2.get() == "Meters":
        destroy_frame()
        final_length = float(entry_answer1) * 1000
        label_length = Label(frame_length_answer, text="Success! The result is: " + str(round((final_length), 3)) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    else:
        destroy_frame()
        label_length2 = Label(frame_length_answer, text="No change!")
        label_length2.pack()

def destroy_frame():
    for widget in frame_length_answer.winfo_children():
        widget.destroy()


dd_length_c1 = StringVar(root)
dd_length_c1.set("Inches") # Dropdown default for choice 1

dd_length_c2 = StringVar(root)
dd_length_c2.set("Centimeters") # Dropdown default for choice 2

label_length_title = Label(root, text="Length Conversion", font=("TkDefaultFont",25), bg="#00ffff", bd=2, relief="ridge")
label_length_title.pack(pady=40)


# FRAMES #

frame_length = Frame(root)
frame_length.pack()

frame_length_answer = Frame(root, bd=1, bg="Blue")


# DROPDOWN OPTION MENUS #

dd_length_first = OptionMenu(frame_length, dd_length_c1, "Inches", "Feet", "Yards", "Miles", "Centimeters", "Meters", "Kilometers")
dd_length_first.grid(row=0, column=0)

label_frame_one = Label(frame_length, text="  To  ")
label_frame_one.grid(row=0, column=1)

dd_length_second = OptionMenu(frame_length, dd_length_c2, "Inches", "Feet", "Yards", "Miles", "Centimeters", "Meters", "Kilometers")
dd_length_second.grid(row=0, column=2)


# ENTRY FIELD #

entry_length_1 = Entry(root)
entry_length_1.pack(pady=10)


# BUTTON #
                                                        # lambda command allows a function to pass in a parameter
btn_length_calc = Button(root, text="Calculate!", command=lambda: measure_calc(entry_length_1.get()))
btn_length_calc.pack(pady=10)

frame_length_answer.pack()






root.mainloop()