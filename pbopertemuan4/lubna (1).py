import tkinter as tk
import math

# Fungsi untuk menghitung luas permukaan bola
def hitung_luas_permukaan():
    r = float(jari_jari_entry.get())
    luas_permukaan = 4 * math.pi * r**2
    hasil_luas_permukaan_label.config(text=f"Luas Permukaan: {luas_permukaan:.2f}")

# Fungsi untuk menghitung volume bola
def hitung_volume():
    r = float(jari_jari_entry.get())
    volume = (4/3) * math.pi * r**3
    hasil_volume_label.config(text=f"Volume: {volume:.2f}")

# Membuat jendela aplikasi
app = tk.Tk()
app.title("Aplikasi Bola")

# Membuat label "Nama"
nama_label = tk.Label(app, text="LUBNA AZHAR LATIPAH:")
nama_label.pack()

# Membuat label "Jari-jari"
jari_jari_label = tk.Label(app, text="Jari-jari Bola:")
jari_jari_label.pack()

# Membuat input jari-jari
jari_jari_entry = tk.Entry(app)
jari_jari_entry.pack()

# Tombol untuk menghitung luas permukaan
luas_permukaan_button = tk.Button(app, text="Hitung Luas Permukaan", command=hitung_luas_permukaan)
luas_permukaan_button.pack()

# Label untuk menampilkan hasil luas permukaan
hasil_luas_permukaan_label = tk.Label(app, text="")
hasil_luas_permukaan_label.pack()

# Tombol untuk menghitung volume
volume_button = tk.Button(app, text="Hitung Volume", command=hitung_volume)
volume_button.pack()

# Label untuk menampilkan hasil volume
hasil_volume_label = tk.Label(app, text="")
hasil_volume_label.pack()

app.mainloop()