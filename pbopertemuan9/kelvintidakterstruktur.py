print("Konversi Suhu Kelvin")

# Entry
suhu = input("Masukkan suhu dalam Kelvin: ")

# rumus
C = float(suhu) - 273.15
F = (9/5 * (float(suhu) - 273.15)) + 32
R = (4/5 * (float(suhu) - 273.15))

# output
print(suhu + " Kelvin sama dengan ")
print(str(C) + " Celsius")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")

