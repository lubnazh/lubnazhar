import tkinter as tk

def convert_temperature():
    try:
        temp = float(entry.get())
        if var.get() == 1:  # Celcius to other units
            fahrenheit = (temp * 9/5) + 32
            reamur = temp * 4/5
            kelvin = temp + 273.15
            output_label.config(text=f"{temp} °C = {fahrenheit:.2f} °F, {reamur:.2f} °Re, {kelvin:.2f} K")
        elif var.get() == 2:  # Fahrenheit to other units
            celcius = (temp - 32) * 5/9
            reamur = (temp - 32) * 4/9
            kelvin = (temp - 32) * 5/9 + 273.15
            output_label.config(text=f"{temp} °F = {celcius:.2f} °C, {reamur:.2f} °Re, {kelvin:.2f} K")
        elif var.get() == 3:  # Reamur to other units
            celcius = temp * 5/4
            fahrenheit = temp * 9/4 + 32
            kelvin = temp * 5/4 + 273.15
            output_label.config(text=f"{temp} °Re = {celcius:.2f} °C, {fahrenheit:.2f} °F, {kelvin:.2f} K")
        elif var.get() == 4:  # Kelvin to other units
            celcius = temp - 273.15
            fahrenheit = (temp - 273.15) * 9/5 + 32
            reamur = (temp - 273.15) * 4/5
            output_label.config(text=f"{temp} K = {celcius:.2f} °C, {fahrenheit:.2f} °F, {reamur:.2f} °Re")
        else:
            output_label.config(text="Pilih jenis konversi suhu")
    except ValueError:
        output_label.config(text="Masukkan angka yang valid")

# Create the main window
root = tk.Tk()
root.title("Konversi Suhu")
root.configure(bg='lightblue')  # Background color

# Label Nama
label_nama = tk.Label(root, text="Lubna Azhar Latipah 220511156", bg='lightblue')
label_nama.pack()

# Create the input entry
entry = tk.Entry(root)
entry.pack()

# Create a radio button for temperature units with different background colors and padx
var = tk.IntVar()
var.set(0)

celcius_button = tk.Radiobutton(root, text="Celcius", variable=var, value=1, bg='yellow', pady=20, padx=10)
fahrenheit_button = tk.Radiobutton(root, text="Fahrenheit", variable=var, value=2, bg='lightgreen', pady=20, padx=15)
reamur_button = tk.Radiobutton(root, text="Reamur", variable=var, value=3, bg='blue', pady=20, padx=20)
kelvin_button = tk.Radiobutton(root, text="Kelvin", variable=var, value=4, bg='lightpink', pady=40, padx=25)

celcius_button.pack()
fahrenheit_button.pack()
reamur_button.pack()
kelvin_button.pack()

# Create a button to perform the conversion with background and foreground colors
convert_button = tk.Button(root, text="Konversi", command=convert_temperature, bg="pink", fg="black")
convert_button.pack()

# Create a label to display the output
output_label = tk.Label(root, text="")
output_label.pack()

# Run the main loop
root.mainloop()


