from produk import Produk, ProdukElektronik, ProdukDigital


def main():
    print(f"=== {Produk.nama_toko} ===\n")

    # Instansiasi Object (gunakan nama variabel yang berbeda untuk tiap produk)
    laptop1 = ProdukElektronik("ELK01", "Laptop Gaming MSI Thin 15", 11500000, 5, 24)
    laptop2 = ProdukElektronik("ELK02", "Laptop MSI Titan 18 HX Dragon Edition Draco Epic", 119000000, 10, 12)
    laptop3 = ProdukElektronik("ELK03", "Laptop ROG Zephyrus G16", 43000000, 10, 12)
    laptop4 = ProdukElektronik("ELK04", "Laptop Legion 9i", 95000000, 10, 12)
    hp = ProdukElektronik("ELK05", "Smartphone REDMAGIC 12 PRO", 25000000, 10, 12)
    keyboard = ProdukElektronik("ELK06", "Keyboard Logitech K380s", 590000, 15, 12)
    mouse = ProdukElektronik("ELK07", "Mouse Wireless Logitech", 350000, 20, 12)
    software = ProdukDigital("DGI01", "Lisensi Windows 11 Pro", 450000, 30, "Lifetime Key")

    # Menguji Setter (@property) & Instance Method
    laptop4.harga = 18500000
    laptop4.kurangi_stok(1)

    # Menyimpan semua objek ke dalam list (Polymorphism)
    daftar_produk = [laptop1, laptop2, laptop3, laptop4, hp, keyboard, mouse, software]

    # Menguji Class Method (@classmethod)
    Produk.ubah_pajak(0.12)
    print("--- Setelah Penyesuaian PPN menjadi 12% ---")
    for item in daftar_produk:
        print(f"{item.tampilkan_info()} | Harga Akhir: {Produk.format_rupiah(item.hitung_harga_akhir())}")

    # Menguji Validasi Encapsulation pada Setter
    print("\n--- Uji Validasi Harga Negatif ---")
    try:
        software.harga = -50000
    except ValueError as e:
        print(f"Validasi berhasil: {e}")


if __name__ == "__main__":
    main()