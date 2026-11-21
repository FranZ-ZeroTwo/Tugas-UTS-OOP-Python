# FranZ x Store — Sistem Manajemen Inventaris Produk (Python OOP & Flask)

Aplikasi manajemen produk elektronik dan digital yang dibangun menggunakan bahasa pemrograman **Python** dengan menerapkan konsep **Pemrograman Berorientasi Objek (Object-Oriented Programming / OOP)**. 

Proyek ini menyediakan dua antarmuka sekaligus:
1. **Mode Terminal (CLI)** menggunakan Python standar (`main.py`).
2. **Mode Web Interaktif (Opsional)** menggunakan framework **Flask** dan penyimpanan data otomatis berbasis **JSON** (`app_flask.py`).

---

## Identitas Pembuat
* **Nama:** Frands Sisco
* **Nim:** [14012500104]
* **Kelas:** 3A_KOM
* **GitHub:** [@FranZ-ZeroTwo](https://github.com/FranZ-ZeroTwo)
* **Proyek:** Tugas UTS Pemrograman Berorientasi Objek (Python)

---

## Penerapan Konsep OOP (`main.py`)

Seluruh logika bisnis pada `main.py` dibangun di atas empat pilar utama OOP dan metode khusus Python:

| Konsep OOP | Implementasi di dalam Kode |
| :--- | :--- |
| **Class & Object** | Kelas induk `Produk` serta kelas turunan `ProdukElektronik` dan `ProdukDigital` yang diinstansiasi ke dalam `katalog`. |
| **Encapsulation** | Atribut privat `self.__harga` dan `self.__stok` dilindungi dan divalidasi melalui `@property`, `@harga.setter` (`> 0`), serta `@stok.setter` (`>= 0`). |
| **Inheritance** | `ProdukElektronik` (menambah atribut `garansi_bulan`) dan `ProdukDigital` (menambah atribut `platform`) mewarisi atribut dan metode `Produk` via `super().__init__()`. |
| **Polymorphism** | *Method overriding* pada `tampilkan_info()` di masing-masing subclass untuk menampilkan informasi spesifik produk fisik maupun digital. |
| **Class Variable & Method** | `nama_toko`, `total_produk`, dan `total_pendapatan` diakses melalui `@classmethod` (`get_total_produk()`, `get_total_pendapatan()`). |
| **Static Method** | Utilitas mandiri `format_rupiah()` untuk pemformatan mata uang IDR dan `hitung_pajak_ppn()` untuk kalkulasi PPN 11%. |

---

## Penerapan Pilar & Konsep OOP (`produk.py`) (Opsional)

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
├── produk.py          # Definisi kelas OOP (Produk, ProdukElektronik, ProdukDigital) (opsional)
├── main.py            # Program utama versi Terminal / Command Line (CLI)
├── storage.py         # Modul baca/tulis data produk ke format JSON (opsional)
├── app_flask.py       # Server web Flask (Routing & manajemen CRUD) (opsional)
├── data_toko.json     # Penyimpanan data inventaris persisten (otomatis terbuat) (opsional)
├── templates/
│   └── index.html     # Antarmuka web dashboard (HTML & CSS) (opsional)
└── README.md          # Dokumentasi proyek
```

---

## Cara Menjalankan Proyek

### 1. Menjalankan Versi Terminal (CLI)
Versi ini hanya menggunakan library bawaan Python tanpa perlu instalasi paket eksternal:
```bash
python main.py
```

### 2. Menjalankan Versi Web (Flask) (Opsional)
1. Instal library **Flask**:
   ```bash
   pip install flask
   ```
   Jika tidak bisa install maka jalankan code di bawah ini menggunakan PowerShell:
   ```bash
   & "$env:USERPROFILE\.local\bin\uv.exe" pip install --system --break-system-packages flask
   ```
   Cek daftar paket yang terpasang untuk memastikan flask sudah masuk ke environment Python tersebut:
   ```bash
   & "$env:USERPROFILE\.local\bin\uv.exe" pip list --system
   ```
3. Jalankan server web:
   ```bash
   python app_flask.py
   ```
4. Buka browser dan akses alamat:
   ```text
   [http://127.0.0.1:5000](http://127.0.0.1:5000)
   ```

---

## Fitur Utama Versi Web (Opsional)
* **Dashboard Ringkasan:** Menampilkan total jenis produk, total unit stok tersedia, dan estimasi total nilai aset toko secara *real-time*.
* **Tambah Produk Baru:** Mendukung penambahan kategori *Produk Elektronik* (input masa garansi) maupun *Produk Digital* (input jenis lisensi) secara dinamis.
* **Uji Validasi Encapsulation:** Mengubah harga produk langsung dari tabel dengan validasi otomatis terhadap input harga negatif.
* **Manajemen Stok & Pajak:** Tombol cepat tambah/kurang stok (`+1` / `-1`), hapus produk, serta pembaruan tarif PPN toko secara global.
* **Penyimpanan Persisten:** Setiap perubahan data otomatis tersimpan ke dalam file `data_toko.json`.
