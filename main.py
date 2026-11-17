from produk import Produk, ProdukDigital, ProdukElektronik


def main():
  print(f"=== {Produk.nama_toko} ===\n")

  # Instansiasi Object
  laptop = ProdukElektronik("EL01", "Laptop Gaming MSI", 20000000, 5, 24)
  hp = ProdukElektronik("EL02", "Smartphone Red Magic", 15000000, 10, 12)
  keyboard = ProdukElektronik("EL03", "Keyboard Logitech", 1500000, 15, 6)
  mouse = ProdukElektronik("EL04", "Mouse Razer", 800000, 20, 6)
  Software = ProdukDigital("DG01", "Lisensi Software Pro", 300000, 20, 15)

  # Menguji Setter (@property) & Instance Method
  laptop.harga = 18500000
  laptop.kurangi_stok(1)

  # Demonstrasi Polymorphism
  daftar_produk: list[Produk] = [laptop, hp, keyboard, mouse, Software]
  for item in daftar_produk:
    print(item.tampilkan_info())

  # Menguji Class Method
  print("\n--- Setelah Penyesuaian PPN menjadi 12% ---")
  Produk.ubah_pajak(0.12)
  for item in daftar_produk:
    print(item.tampilkan_info())

  # Menguji Validasi Encapsulation pada Setter
  print("\n--- Uji Validasi Harga Negatif ---")
  try:
    Software.harga = -50000
  except ValueError as e:
    print(f"Validasi berhasil: {e}")
    
if __name__ == "__main__":
  main()