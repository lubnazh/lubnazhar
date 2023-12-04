from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W
from googletrans import Translator

class FrmTranslator:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("500x250")  # Meningkatkan tinggi jendela sedikit untuk menampung label judul
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        self.tampilkanJudul(title)  # Memanggil metode untuk menampilkan judul
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # pasang Label
        Label(mainFrame, text='Lubna Azhar Latipah 220511156', font=('Arial', 10, 'bold')).grid(row=0, column=1,
            sticky=W, padx=5, pady=5, columnspan=3)  # Menambahkan label judul

        Label(mainFrame, text='Masukkan teks:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Terjemahan English').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Terjemahan Italy').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Terjemahan Norwegia').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        
        # pasang textbox
        self.txtSumber = Entry(mainFrame, width=50) 
        self.txtSumber.grid(row=1, column=1, padx=5, pady=5)

        self.txtHasil = Entry(mainFrame, width=50) 
        self.txtHasil.grid(row=3, column=1, padx=5, pady=5)

        self.txtHasil2 = Entry(mainFrame, width=50) 
        self.txtHasil2.grid(row=4, column=1, padx=5, pady=5)

        self.txtHasil3 = Entry(mainFrame, width=50) 
        self.txtHasil3.grid(row=5, column=1, padx=5, pady=5)

        # Pasang Button
        self.btnTranslate = Button(mainFrame, text='Translate!',
            command=self.onTranslate)
        self.btnTranslate.grid(row=2, column=1, padx=5, pady=5, columnspan=2) 

    def tampilkanJudul(self, title):
        Label(self.parent, text=title, font=('Arial', 14, 'bold')).pack(pady=10)

    def onTranslate(self):
        penterjemah = Translator()

        hasil = penterjemah.translate(self.txtSumber.get(), src='id', dest='en') 
        hasil2 = penterjemah.translate(self.txtSumber.get(), src='id', dest='it')
        hasil3 = penterjemah.translate(self.txtSumber.get(), src='id', dest='no')
       
        self.txtHasil.insert(END, hasil.text)
        self.txtHasil2.insert(END, hasil2.text)
        self.txtHasil3.insert(END, hasil3.text)

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    judul = "Program Translator"  # Judul yang ingin Anda gunakan
    aplikasi = FrmTranslator(root, judul)
    root.mainloop()
