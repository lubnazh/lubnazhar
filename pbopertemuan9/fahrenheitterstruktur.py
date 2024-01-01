print("Konversi Suhu Fahrenheit")

def get_celsius(suhu):
    C = (float(suhu) - 32) * 5/9
    return C

def get_reamur(suhu):
    R = (float(suhu) - 32) * 4/9
    return R

def get_kelvin(suhu):
    K = (float(suhu) - 32) * 5/9 + 273.15
    return K

# Entry
suhu = input("Masukkan suhu dalam Fahrenheit: ")

# rumus
C = get_celsius(suhu)
R = get_reamur(suhu)
K = get_kelvin(suhu)

# output
print(suhu + " Fahrenheit sama dengan ")
print(str(C) + " Celsius")
print(str(R) + " Reamur")
print(str(K) + " Kelvin")
