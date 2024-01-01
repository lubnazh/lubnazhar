print("Konversi Suhu Reamur ke Suhu Lainnya")

def get_fahrenheit(suhu):
    F = (9/4 * float(suhu)) + 32
    return F

def get_celcius(suhu):
    C = (5/4 * float(suhu))
    return C

def get_kelvin(suhu):
    K = (5/4 * float(suhu)) + 273.15
    return K

# Entry
suhu = input("Masukkan suhu dalam Reamur: ")

# Menghitung hasil konversi
F = get_fahrenheit(suhu)
C = get_celcius(suhu)
K = get_kelvin(suhu)

# Output hasil konversi
print(suhu + " Reamur sama dengan ")
print(str(F) + " Fahrenheit")
print(str(C) + " Celcius")
print(str(K) + " Kelvin")
