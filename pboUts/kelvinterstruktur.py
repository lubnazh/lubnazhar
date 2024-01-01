print("Konversi Suhu Kelvin")

def get_celsius(suhu):
    C = float(suhu) - 273.15
    return C

def get_fahrenheit(suhu):
    F = (9/5 * (float(suhu) - 273.15)) + 32
    return F

def get_reamur(suhu):
    R = (4/5 * (float(suhu) - 273.15))
    return R

# Entry
suhu = input("Masukkan suhu dalam Kelvin: ")

# rumus
C = get_celsius(suhu)
F = get_fahrenheit(suhu)
R = get_reamur(suhu)

# output
print(suhu + " Kelvin sama dengan ")
print(str(C) + " Celsius")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")
