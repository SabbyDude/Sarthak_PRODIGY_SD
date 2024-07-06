import tkinter as tk

def convert_temperature():
    num = float(entry_temperature.get())
    temp = unit.get()
    result = ""
    
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
