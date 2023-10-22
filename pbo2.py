# Meminta pengguna untuk memasukkan total pembelian
total_pembelian = float(input("Masukkan total pembelian: $"))

# Menghitung diskon berdasarkan total pembelian
if total_pembelian >= 200:
    diskon = 0.10  # Diskon 10% untuk pembelian di atas atau sama dengan $200
else:
    diskon = 0.05  # Diskon 5% untuk pembelian kurang dari $200

# Menghitung jumlah diskon
jumlah_diskon = total_pembelian * diskon

# Menghitung total yang harus dibayar setelah diskon
total_setelah_diskon = total_pembelian - jumlah_diskon

# Menampilkan informasi tentang pembelian dan diskon
print(f"Total Pembelian: ${total_pembelian:.2f}")
print(f"Diskon: ${jumlah_diskon:.2f}")
print(f"Total Setelah Diskon: ${total_setelah_diskon:.2f}")





