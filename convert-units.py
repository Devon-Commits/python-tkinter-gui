from tkinter import *

root = Tk()
root.title("Conversion Calculator")           
root.geometry("500x500")
root.iconbitmap("c:/pythondev/gui/icon-calculator.ico")

# Functions

def measure_calc(entry_length_1 = 1.0):
    entry_answer1 = entry_length_1
    global label_length
    ### INCHES ###
    if dd_length_c1.get() == "Inches" and dd_length_c2.get() == "Feet":
        final_length = float(entry_answer1) / 12
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Inches" and dd_length_c2.get() == "Yards":
        final_length = float(entry_answer1) / 36
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Inches" and dd_length_c2.get() == "Miles":
        final_length = float(entry_answer1) / 63360
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Inches" and dd_length_c2.get() == "Centimeters":
        final_length = float(entry_answer1) * 2.54
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Inches" and dd_length_c2.get() == "Meters":
        final_length = float(entry_answer1) / 39.37
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Inches" and dd_length_c2.get() == "Kilometers":
        final_length = float(entry_answer1) / 39370
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    ### FEET ###
    elif dd_length_c1.get() == "Feet" and dd_length_c2.get() == "Inches":
        final_length = float(entry_answer1) * 12
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Feet" and dd_length_c2.get() == "Yards":
        final_length = float(entry_answer1) / 3
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Feet" and dd_length_c2.get() == "Miles":
        final_length = float(entry_answer1) / 5280
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Feet" and dd_length_c2.get() == "Centimeters":
        final_length = float(entry_answer1) * 30.48
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Feet" and dd_length_c2.get() == "Meters":
        final_length = float(entry_answer1) / 3.281
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Feet" and dd_length_c2.get() == "Kilometers":
        final_length = float(entry_answer1) / 3281
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    ### YARDS ###
    elif dd_length_c1.get() == "Yards" and dd_length_c2.get() == "Inches":
        final_length = float(entry_answer1) * 36
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Yards" and dd_length_c2.get() == "Feet":
        final_length = float(entry_answer1) * 3
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Yards" and dd_length_c2.get() == "Miles":
        final_length = float(entry_answer1) / 1760
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Yards" and dd_length_c2.get() == "Centimeters":
        final_length = float(entry_answer1) * 91.44
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Yards" and dd_length_c2.get() == "Meters":
        final_length = float(entry_answer1) / 1.094
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Yards" and dd_length_c2.get() == "Kilometers":
        final_length = float(entry_answer1) / 1094
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    ### MILES ###
    elif dd_length_c1.get() == "Miles" and dd_length_c2.get() == "Inches":
        final_length = float(entry_answer1) * 63360
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Miles" and dd_length_c2.get() == "Feet":
        final_length = float(entry_answer1) * 5280
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Miles" and dd_length_c2.get() == "Yards":
        final_length = float(entry_answer1) * 1760
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Miles" and dd_length_c2.get() == "Centimeters":
        final_length = float(entry_answer1) * 160900
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Miles" and dd_length_c2.get() == "Meters":
        final_length = float(entry_answer1) * 1609
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Miles" and dd_length_c2.get() == "Kilometers":
        final_length = float(entry_answer1) * 1.609
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    ### CENTIMETERS ###
    elif dd_length_c1.get() == "Centimeters" and dd_length_c2.get() == "Inches":
        final_length = float(entry_answer1) / 2.54
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Centimeters" and dd_length_c2.get() == "Feet":
        final_length = float(entry_answer1) / 30.48
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Centimeters" and dd_length_c2.get() == "Yards":
        final_length = float(entry_answer1) / 91.44
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Centimeters" and dd_length_c2.get() == "Miles":
        final_length = float(entry_answer1) / 160900
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Centimeters" and dd_length_c2.get() == "Meters":
        final_length = float(entry_answer1) / 100
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Centimeters" and dd_length_c2.get() == "Kilometers":
        final_length = float(entry_answer1) / 100000
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    ### METERS ###
    elif dd_length_c1.get() == "Meters" and dd_length_c2.get() == "Inches":
        final_length = float(entry_answer1) * 39.37
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Meters" and dd_length_c2.get() == "Feet":
        final_length = float(entry_answer1) * 3.281
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Meters" and dd_length_c2.get() == "Yards":
        final_length = float(entry_answer1) * 1.094
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Meters" and dd_length_c2.get() == "Miles":
        final_length = float(entry_answer1) / 1609
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Meters" and dd_length_c2.get() == "Centimeters":
        final_length = float(entry_answer1) * 100
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Meters" and dd_length_c2.get() == "Kilometers":
        final_length = float(entry_answer1) / 1000
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    ### KILOMETERS ###
    elif dd_length_c1.get() == "Kilometers" and dd_length_c2.get() == "Inches":
        final_length = float(entry_answer1) * 39370
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Kilometers" and dd_length_c2.get() == "Feet":
        final_length = float(entry_answer1) * 3281
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Kilometers" and dd_length_c2.get() == "Yards":
        final_length = float(entry_answer1) * 1094
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Kilometers" and dd_length_c2.get() == "Miles":
        final_length = float(entry_answer1) / 1.609
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Kilometers" and dd_length_c2.get() == "Centimeters":
        final_length = float(entry_answer1) * 100000
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    elif dd_length_c1.get() == "Kilometers" and dd_length_c2.get() == "Meters":
        final_length = float(entry_answer1) * 1000
        label_length = Label(root, text="Success! The result is: " + str(final_length) + " "+ str(dd_length_c2.get()))
        label_length.pack()

    else:
        label_length2 = Label(root, text="No change!")
        label_length2.pack()

def hide():
    label_length.pack_forget()

dd_length_c1 = StringVar(root)
dd_length_c1.set("Inches") # Default

dd_length_c2 = StringVar(root)
dd_length_c2.set("Centimeters") # Default


dd_length_first = OptionMenu(root, dd_length_c1, "Inches", "Feet", "Yards", "Miles", "Centimeters", "Meters", "Kilometers")
dd_length_first.pack()

dd_length_second = OptionMenu(root, dd_length_c2, "Inches", "Feet", "Yards", "Miles", "Centimeters", "Meters", "Kilometers")
dd_length_second.pack()

entry_length_1 = Entry(root)
entry_length_1.pack()

btn_length_calc = Button(root, text="Calculate!", command=lambda: measure_calc(entry_length_1.get()))
btn_length_calc.pack()








root.mainloop()