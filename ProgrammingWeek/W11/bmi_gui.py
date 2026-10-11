import tkinter

def calculate():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height * height)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text="BMI: " + str(round(bmi, 2)) + " (" + category + ")")
    except ValueError:
        result_label.config(text="Please enter numbers only")

window = tkinter.Tk()
window.title("BMI Calculator")
window.geometry("400x300")

title_label = tkinter.Label(window, text="BMI Calculator")
title_label.pack(pady=20)

entry_frame = tkinter.Frame(window)
entry_frame.pack(pady=10)

weight_label = tkinter.Label(entry_frame, text="Weight (kg)")
weight_label.pack(side="left", padx=5)
entry_weight = tkinter.Entry(entry_frame, width=8)
entry_weight.pack(side="left", padx=5)

height_label = tkinter.Label(entry_frame, text="Height (m)")
height_label.pack(side="left", padx=5)
entry_height = tkinter.Entry(entry_frame, width=8)
entry_height.pack(side="left", padx=5)

button = tkinter.Button(window, text="Calculate", command=calculate)
button.pack(pady=20)

result_label = tkinter.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()