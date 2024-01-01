import tkinter as tk
from tkinter import filedialog
from PIL import Image
import pytesseract

def extract_text():
    def get_text_from_image(image_path):
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        extracted_text = get_text_from_image(file_path)
        text_display.delete(1.0, tk.END)  # Menghapus teks sebelumnya
        text_display.insert(tk.END, extracted_text)  # Menampilkan teks hasil ekstraksi

root = tk.Tk()
root.title("Extract Text from Image")

# Button untuk memilih file gambar
choose_button = tk.Button(root, text="Choose Image File", command=extract_text)
choose_button.pack(pady=10)

# Area tampilan teks untuk hasil ekstraksi
text_display = tk.Text(root, height=15, width=50)
text_display.pack(padx=10, pady=5)

root.mainloop()

