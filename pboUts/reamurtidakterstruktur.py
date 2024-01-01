print("Konversi Suhu Reamur ke Suhu Lainnya")

# Masukan suhu dalam Reamur
suhu = input("Masukkan suhu dalam Reamur: ")

# Konversi ke Fahrenheit
F = (9/4 * float(suhu)) + 32

# Konversi ke Celcius
C = (5/4 * float(suhu))

# Konversi ke Kelvin
K = (5/4 * float(suhu)) + 273.15

# Output hasil konversi
print(suhu + " Reamur sama dengan ")
print(str(F) + " Fahrenheit")
print(str(C) + " Celcius")
print(str(K) + " Kelvin")
