# FranZ x Store — Sistem Manajemen Inventaris Produk (Python OOP & Flask)

Aplikasi manajemen produk elektronik dan digital yang dibangun menggunakan bahasa pemrograman **Python** dengan menerapkan konsep **Pemrograman Berorientasi Objek (Object-Oriented Programming / OOP)**. 

Proyek ini menyediakan dua antarmuka sekaligus:
1. **Mode Terminal (CLI)** menggunakan Python standar (`main.py`).
2. **Mode Web Interaktif** menggunakan framework **Flask** dan penyimpanan data otomatis berbasis **JSON** (`app_flask.py`).

---

## Identitas Pembuat
* **Nama:** Frands Sisco
* **GitHub:** [@FranZ-ZeroTwo](https://github.com/FranZ-ZeroTwo)
* **Proyek:** Tugas UTS Pemrograman Berorientasi Objek (Python)

---

## Penerapan Pilar & Konsep OOP (`produk.py`)

Seluruh logika bisnis dan struktur data toko dirancang di dalam modul `produk.py` dengan menerapkan konsep berikut:

1. **Abstraction (`ABC` & `@abstractmethod`)**
   * Kelas `Produk` didefinisikan sebagai *Abstract Base Class* sehingga tidak dapat diinstansiasi secara langsung dan mewajibkan setiap kelas turunannya mengimplementasikan metode `tampilkan_info()`.
2. **Encapsulation (`@property` & `@harga.setter`)**
   * Menggunakan atribut *private* (`__harga`) dan *protected* (`_stok`) untuk menjaga integritas data.
   * Perubahan harga melalui *setter* dilengkapi validasi otomatis yang menolak angka negatif (`ValueError`), serta metode `tambah_stok()` dan `kurangi_stok()` yang memvalidasi ketersediaan stok.
3. **Inheritance (Pewarisan)**
   * `ProdukElektronik` mewarisi kelas `Produk` dengan tambahan atribut `garansi_bulan`.
   * `ProdukDigital` mewarisi kelas `Produk` dengan tambahan atribut `jenis_lisensi`.
4. **Polymorphism**
   * Penerapan *method overriding* pada `tampilkan_info()` sehingga objek `ProdukElektronik` dan `ProdukDigital` menampilkan detail spesifik yang berbeda saat dipanggil secara seragam.
5. **Class Method & Static Method**
   * `@classmethod ubah_pajak()`: Mengubah persentase PPN toko yang berlaku secara global untuk seluruh objek produk.
   * `@staticmethod format_rupiah()`: Fungsi utilitas untuk memformat angka nominal menjadi format mata uang Rupiah (`Rp`).

---

## Struktur Direktori Proyek

```text
FranZ x Store/
├── produk.py          # Definisi kelas OOP (Produk, ProdukElektronik, ProdukDigital)
├── main.py            # Program utama versi Terminal / Command Line (CLI)
├── storage.py         # Modul baca/tulis data produk ke format JSON
├── app_flask.py       # Server web Flask (Routing & manajemen CRUD)
├── data_toko.json     # Penyimpanan data inventaris persisten (otomatis terbuat)
├── templates/
│   └── index.html     # Antarmuka web dashboard (HTML & CSS)
└── README.md          # Dokumentasi proyek
```

---

## Cara Menjalankan Proyek

### 1. Menjalankan Versi Terminal (CLI)
Versi ini hanya menggunakan library bawaan Python tanpa perlu instalasi paket eksternal:
```bash
python main.py
```

### 2. Menjalankan Versi Web (Flask)
1. Instal library **Flask**:
   ```bash
   pip install flask
   ```
2. Jalankan server web:
   ```bash
   python app_flask.py
   ```
3. Buka browser dan akses alamat:
   ```text
   [http://127.0.0.1:5000](http://127.0.0.1:5000)
   ```

---

## Fitur Utama Versi Web
* **Dashboard Ringkasan:** Menampilkan total jenis produk, total unit stok tersedia, dan estimasi total nilai aset toko secara *real-time*.
* **Tambah Produk Baru:** Mendukung penambahan kategori *Produk Elektronik* (input masa garansi) maupun *Produk Digital* (input jenis lisensi) secara dinamis.
* **Uji Validasi Encapsulation:** Mengubah harga produk langsung dari tabel dengan validasi otomatis terhadap input harga negatif.
* **Manajemen Stok & Pajak:** Tombol cepat tambah/kurang stok (`+1` / `-1`), hapus produk, serta pembaruan tarif PPN toko secara global.
* **Penyimpanan Persisten:** Setiap perubahan data otomatis tersimpan ke dalam file `data_toko.json`.