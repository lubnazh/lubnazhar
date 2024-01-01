import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

def get_celcius():
    suhu = float(txtReamur.get()) * 5/4
    txtCelcius.delete(0, END)
    txtCelcius.insert(END, suhu)

def get_fahrenheit():
    suhu = float(txtReamur.get()) * 9/4 + 32
    txtFahrenheit.delete(0, END)
    txtFahrenheit.insert(END, suhu)

def get_kelvin():
    suhu = float(txtReamur.get()) * 5/4 + 273
    txtKelvin.delete(0, END)
    txtKelvin.insert(END, suhu)

def hitung():
    get_celcius()
    get_fahrenheit()
    get_kelvin()

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Suhu Reamur")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label 
suhu = Label(frame, text="Reamur:")
suhu.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Textbox 
txtReamur = Entry(frame)
txtReamur.grid(row=0, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=1, column=1, sticky=W, padx=5, pady=5)

C = Label(frame, text="Celcius:")
C.grid(row=2, column=0, sticky=W, padx=5, pady=5)

F = Label(frame, text="Fahrenheit:")
F.grid(row=3, column=0, sticky=W, padx=5, pady=5)

K = Label(frame, text="Kelvin:")
K.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox 
txtCelcius = Entry(frame)
txtCelcius.grid(row=2, column=1, sticky=W, padx=5, pady=5)

txtFahrenheit = Entry(frame)
txtFahrenheit.grid(row=3, column=1, sticky=W, padx=5, pady=5)

txtKelvin = Entry(frame)
txtKelvin.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
