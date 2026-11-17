# Project Sederhana OOP Python - FranZ x Store

Repository ini berisi implementasi konsep **Object-Oriented Programming (OOP)** menggunakan bahasa Python **FranZ x Store**.

## Struktur File
- `produk.py` : Modul definisi kelas abstrak `Produk` serta kelas turunan `ProdukElektronik` dan `ProdukDigital`.
- `main.py` : File utama untuk instansiasi objek produk dan pengujian metode OOP.

## Konsep OOP yang Diterapkan
1. **Class & Object**: Pembuatan blueprint `Produk` beserta instansiasi objek (`Laptop Gaming MSI`, `Smartphone Red Magic`, `Keyboard Logitech`, `Mouse Razer`, dan `Lisensi Software Pro`).
2. **Encapsulation & Property**: Penggunaan atribut private (`__harga`) yang diakses dan divalidasi melalui decorator `@property` dan `@harga.setter`.
3. **Jenis-jenis Method**:
   - *Instance Method* (`kurangi_stok`)
   - *Class Method* (`@classmethod` pada `ubah_pajak`)
   - *Static Method* (`@staticmethod` pada `format_rupiah`)
4. **Abstraction**: Penggunaan modul `abc` (`ABC` dan `@abstractmethod`) pada kelas induk `Produk`.
5. **Inheritance & Polymorphism**: Pewarisan sifat ke kelas `ProdukElektronik` dan `ProdukDigital` dengan *method overriding* pada `hitung_harga_akhir()` dan `tampilkan_info()`.

## Cara Menjalankan
Buka terminal di dalam folder proyek, lalu jalankan perintah:
```bash
python main.py
```

## Identitas Mahasiswa
- **Nama:** Frands Sisco
- **NIM:** [14012500104]
- **Kelas:** [3A-KOM]