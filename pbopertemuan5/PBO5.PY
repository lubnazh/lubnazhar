import tkinter as tk

# Data jadwal kuliah (contoh)
jadwal = {
    "Senin": ["Mata Kuliah Arsitektur dan Organisasi KOmputer 08:00-10.00", "Mata Kuliah AIK - 10:01-11:40"],
    "Selasa": ["Mata Kuliah Manajemen Proyek 09:40-11:40", "Mata Kuliah PBO 13:00-15:30"],
    "Rabu": ["Mata Kuliah Kalkulus 08:00-10:00", "Mata Kuliah Sistem Informasi Apsi 13:00-15:30"],
    "Kamis": ["Tidak Ada Perkuliahan"],
    "Jumat": ["Mata Kuliah Komunikasi Data 09:40-11:40", "Mata Kuliah Statistik dan Probabilitas 13:00-14:40", "Mata Kuliah Struktur Data 15:00-17:30"]
}

# Fungsi untuk menampilkan jadwal berdasarkan hari yang dipilih
def tampilkan_jadwal():
    hari_terpilih = hari_var.get()
    jadwal_text.config(state=tk.NORMAL)
    jadwal_text.delete(1.0, tk.END)  # Menghapus teks sebelumnya
    if hari_terpilih in jadwal:
        for jadwal_item in jadwal[hari_terpilih]:
            jadwal_text.insert(tk.END, jadwal_item + "\n")
    else:
        jadwal_text.insert(tk.END, "Tidak ada jadwal untuk hari ini.")
    jadwal_text.config(state=tk.DISABLED)

app = tk.Tk()
app.title("Aplikasi Jadwal Kuliah")

label_nama = tk.Label(app, text="Lubna Azhar Latipah 220511156")
label_nama.pack(pady=5)

frame_input = tk.Frame(app)
frame_input.pack(pady=5)

label_hari = tk.Label(frame_input, text="Pilih Hari:")
label_hari.pack(side=tk.LEFT)

# Daftar hari
hari_var = tk.StringVar()
hari_var.set("Senin")  # Hari default
hari_option_menu = tk.OptionMenu(frame_input, hari_var, *jadwal.keys())
hari_option_menu.pack(side=tk.LEFT)

button_tampilkan = tk.Button(frame_input, text="Tampilkan Jadwal", command=tampilkan_jadwal)
button_tampilkan.pack(side=tk.LEFT)

jadwal_text = tk.Text(app, height=10, width=70, state=tk.DISABLED)
jadwal_text.pack(padx=10, pady=10)

app.mainloop()


