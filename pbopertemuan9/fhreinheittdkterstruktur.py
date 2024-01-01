print("Konversi Suhu Fahrenheit")

# Entry
suhu = input("Masukkan suhu dalam Fahrenheit: ")

# rumus
C = (float(suhu) - 32) * 5/9
R = (float(suhu) - 32) * 4/9
K = (float(suhu) - 32) * 5/9 + 273.15

# output
print(suhu + " Fahrenheit sama dengan ")
print(str(C) + " Celsius")
print(str(R) + " Reamur")
print(str(K) + " Kelvin")
