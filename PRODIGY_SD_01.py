import tkinter as tk

def convert_temperature():
    num = float(entry_temperature.get()) #coverts the user value into a float-point number
    temp = unit.get() #checkes the user's choice of Celius, Farenheit or Kelvin
    result = ""
    #this if-elif-elif bridge converts the given temprature into the other two temprature units
    if temp == 'C':
        fr = num*(9/5) + 32
        kl = num + 273.15
        result = f"{fr:.2f}°F and {kl:.2f}K"
        
    elif temp == 'K':
        cs = num - 273.15
        fr = cs * (9/5) + 32
        result = f"{fr:.2f}°F and {cs:.2f}°C"
        
    elif temp == 'F':
        cs = (num - 32) * (5/9)
        kl = cs + 273.15
        result = f"{cs:.2f}°C and {kl:.2f}K"

    else:
        result = "Not a valid unit!"
    
    label_result.config(text=result)

#this bit of code is required to make the window and take the nessasary inputs
root = tk.Tk()
root.title("Temperature Converter")

tk.Label(root, text="Enter temperature:").pack()
entry_temperature = tk.Entry(root)
entry_temperature.pack()

unit = tk.StringVar()
units_frame = tk.Frame(root)
units_frame.pack()

tk.Radiobutton(units_frame, text='Celsius', variable=unit, value='C').pack(side=tk.LEFT)
tk.Radiobutton(units_frame, text='Fahrenheit', variable=unit, value='F').pack(side=tk.LEFT)
tk.Radiobutton(units_frame, text='Kelvin', variable=unit, value='K').pack(side=tk.LEFT)

tk.Button(root, text="Convert", command=convert_temperature).pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
