class Celcius:
    def __init__(self, suhu):
        self.suhu = suhu

    def get_celcius(self):
        val = self.suhu - 273.15  # Ubah rumus untuk konversi dari Kelvin ke Celcius
        return val

    def get_fahrenheit(self):
        val = (9/5 * (self.suhu - 273.15)) + 32  # Konversi dari Kelvin ke Celcius terlebih dahulu, lalu ke Fahrenheit
        return val

    def get_reamur(self):
        val = (4/5 * (self.suhu - 273.15))  # Konversi dari Kelvin ke Celcius terlebih dahulu, lalu ke Reamur
        return val

    def get_kelvin(self):
        val = self.suhu  # Karena ini adalah kelas untuk suhu dalam Kelvin
        return val

suhu = input("Masukkan suhu dalam Kelvin: ")
C = Celcius(float(suhu))
val = C.get_kelvin()

F = C.get_fahrenheit()
R = C.get_reamur()
K = C.get_celcius()

print(str(val) + " Kelvin, sama dengan:")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")
print(str(K) + " Celcius")

