import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=250)

w_label = Label(text="Enter Your Weight (kg)")
w_label.place(x=80, y=60)

w_entry = Entry(width=12)
w_entry.place(x=100, y=80)

h_label = Label(text="Enter Your Height (cm)")
h_label.place(x=80, y=100)

h_entry = Entry(width=12)
h_entry.place(x=100, y=120)

info_label = Label()
def show_result():
    global info_label
    h = h_entry.get()
    w = w_entry.get()
    if h == "" or w == "":
        info_label.config(text="Please enter both weight and height")
    else:
        try:
            bmi = round(float(w)/((float(h)/100)**2),2)
            if bmi < 18.5:
                info_label.config(text="Your bmi is " + str(bmi) + " Under Weight")
            elif 18.5<=bmi<=24.9:
                info_label.config(text="Your bmi is " + str(bmi) + " Normal")
            elif 25<=bmi<=29.9:
                info_label.config(text="Your bmi is " + str(bmi) + " Over Weight")
            elif 30<=bmi<=34.9:
                info_label.config(text="Your bmi is " + str(bmi) + " Obesity (Class I)")
            elif 35<=bmi<=39.9:
                info_label.config(text="Your bmi is " + str(bmi) + " Obesity (Class II)")
            else:
                info_label.config(text="Your bmi is " + str(bmi) + " Extreme Obesity")
        except:
            info_label.config(text="Please enter a valid number!")

    info_label.place(x=60, y=185)

c_button = Button(text="Calculate", command=show_result)
c_button.place(x=108, y=150)

window.mainloop()
