import tkinter as tk
from tkinter import filedialog
import pygame

def choose_file():
    global file_path  # Mendeklarasikan file_path sebagai variabel global
    file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if file_path:
        play_button.config(state=tk.NORMAL)  # Aktifkan tombol play setelah memilih file

def play_music():
    if 'file_path' in globals():  # Pastikan file_path telah ada sebelum memainkan musik
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

root = tk.Tk()
root.title("MP3 Player")
root.configure(bg='lightblue')  # Background color

# Label for the name
label_nama = tk.Label(root, text="Lubna Azhar Latipah 220511156", bg='lightblue')  # Set background color
label_nama.pack(pady=5)

# Button to choose MP3 file
choose_button = tk.Button(root, text="Choose MP3 File", command=choose_file)
choose_button.pack(pady=10)

# Button to play the chosen MP3 file
play_button = tk.Button(root, text="Play", command=play_music, state=tk.DISABLED)  # Disable play button initially
play_button.pack(pady=5)

# Button to stop playing the music
stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack(pady=5, padx=20)

root.mainloop()

