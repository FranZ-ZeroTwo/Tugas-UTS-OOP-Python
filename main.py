class Produk:
    # Class Variables
    nama_toko = "FranZ x Store"
    total_produk = 0
    total_pendapatan = 0.0

    # Constructor & Encapsulation (Private Attributes)
    def __init__(self, kode: str, nama: str, harga: float, stok: int):
        self.kode = kode.upper()    # Public instance variable
        self.nama = nama            # Public instance variable
        self.__harga = 0.0          # Private attribute (Encapsulation)
        self.__stok = 0             # Private attribute (Encapsulation)

        # Menggunakan setter untuk validasi nilai awal
        self.harga = harga
        self.stok = stok

        Produk.total_produk += 1

    # Property Method: Getter & Setter untuk Harga
    @property
    def harga(self) -> float:
        return self.__harga

    @harga.setter
    def harga(self, nilai_baru: float):
        if nilai_baru > 0:
            self.__harga = nilai_baru
        else:
            raise ValueError("Harga produk harus lebih dari Rp0.")

    # Property Method: Getter & Setter untuk Stok
    @property
    def stok(self) -> int:
        return self.__stok

    @stok.setter
    def stok(self, jumlah_baru: int):
        if jumlah_baru >= 0:
            self.__stok = jumlah_baru
        else:
            raise ValueError("Stok tidak boleh bernilai negatif.")

    # Instance Methods
    def tambah_stok(self, jumlah: int):
        if jumlah > 0:
            self.__stok += jumlah
            print(f"\n[Berhasil] Stok '{self.nama}' bertambah +{jumlah}. Total stok: {self.__stok}")
        else:
            print("\n[Gagal] Jumlah penambahan stok harus lebih dari 0.")

    def beli(self, jumlah: int) -> bool:
        if jumlah <= 0:
            print("\n[Gagal] Jumlah pembelian minimal 1 unit.")
            return False
        if jumlah > self.__stok:
            print(f"\n[Gagal] Stok '{self.nama}' tidak mencukupi (Tersisa: {self.__stok}).")
            return False

        self.__stok -= jumlah
        subtotal = self.__harga * jumlah
        pajak = Produk.hitung_pajak_ppn(subtotal)
        total_bayar = subtotal + pajak
        Produk.total_pendapatan += subtotal

        print("\n" + "=" * 42)
        print("           STRUK PEMBELIAN")
        print("=" * 42)
        print(f"Produk     : {self.nama} ({self.kode})")
        print(f"Harga      : {Produk.format_rupiah(self.__harga)} x {jumlah}")
        print(f"Subtotal   : {Produk.format_rupiah(subtotal)}")
        print(f"PPN (11%)  : {Produk.format_rupiah(pajak)}")
        print(f"Total Bayar: {Produk.format_rupiah(total_bayar)}")
        print("=" * 42)
        return True

    def tampilkan_info(self):
        print(f"[{self.kode}] {self.nama}")
        print(f"  Harga : {Produk.format_rupiah(self.__harga)}")
        print(f"  Stok  : {self.__stok} tersedia")

    # Class Methods
    @classmethod
    def get_total_produk(cls) -> int:
        return cls.total_produk

    @classmethod
    def get_total_pendapatan(cls) -> float:
        return cls.total_pendapatan

    # Static Methods
    @staticmethod
    def format_rupiah(nominal: float) -> str:
        return f"Rp{nominal:,.0f}".replace(",", ".")

    @staticmethod
    def hitung_pajak_ppn(nominal: float, tarif: float = 0.11) -> float:
        return nominal * tarif


# Inheritance & Polymorphism: Produk Elektronik (Fisik)
class ProdukElektronik(Produk):
    def __init__(self, kode: str, nama: str, harga: float, stok: int, garansi_bulan: int):
        super().__init__(kode, nama, harga, stok)
        self.garansi_bulan = garansi_bulan

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"  Jenis : Elektronik Fisik (Garansi {self.garansi_bulan} bulan)")
        print("-" * 45)


# Inheritance & Polymorphism: Produk Digital (Voucher / Lisensi)
class ProdukDigital(Produk):
    def __init__(self, kode: str, nama: str, harga: float, stok: int, platform: str):
        super().__init__(kode, nama, harga, stok)
        self.platform = platform

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"  Jenis : Produk Digital (Platform: {self.platform})")
        print("-" * 45)


def cari_produk(katalog: list, kode: str):
    for item in katalog:
        if item.kode == kode.strip().upper():
            return item
    return None


def jalankan_aplikasi():
    # Data awal katalog
    katalog = [
        ProdukElektronik("ELK01", "Laptop Gaming MSI Thin 15", 11500000, 5, 24),
        ProdukElektronik("ELK02", "Laptop MSI Titan 18 HX Dragon Edition Draco Epic", 119000000, 10, 12),
        ProdukElektronik("ELK03", "Laptop ROG Zephyrus G16", 43000000, 10, 12),
        ProdukElektronik("ELK04", "Laptop Legion 9i", 95000000, 10, 12),
        ProdukElektronik("ELK05", "Smartphone REDMAGIC 12 PRO", 25000000, 10, 12),
        ProdukElektronik("ELK06", "Keyboard Logitech K380s", 590000, 15, 12),
        ProdukElektronik("ELK07", "Mouse Wireless Logitech", 350000, 20, 12),
        ProdukDigital("DGI01", "Lisensi Windows 11 Pro", 450000, 30, "Lifetime Key")
    ]

    while True:
        print(f"\n=== {Produk.nama_toko.upper()} ===")
        print("1. Lihat Katalog Produk")
        print("2. Simulasi Penjualan (Beli Produk)")
        print("3. Tambah Produk Baru")
        print("4. Restock Produk")
        print("5. Ubah Harga Produk")
        print("6. Lihat Laporan Penjualan")
        print("0. Keluar")

        pilihan = input("\nPilih menu (0-6): ").strip()

        if pilihan == "1":
            print("\n--- KATALOG PRODUK ---")
            for item in katalog:
                item.tampilkan_info()

        elif pilihan == "2":
            print("\n--- SIMULASI PENJUALAN ---")
            kode = input("Masukkan Kode Produk (contoh: ELK01): ")
            produk = cari_produk(katalog, kode)
            if produk:
                try:
                    jumlah = int(input(f"Jumlah beli '{produk.nama}' (Stok: {produk.stok}): "))
                    produk.beli(jumlah)
                except ValueError:
                    print("\n[Error] Masukkan jumlah dalam bentuk angka bulat.")
            else:
                print("\n[Error] Kode produk tidak ditemukan.")

        elif pilihan == "3":
            print("\n--- TAMBAH PRODUK BARU ---")
            jenis = input("Jenis produk (1 = Elektronik, 2 = Digital): ").strip()
            if jenis not in ("1", "2"):
                print("\n[Error] Pilihan jenis tidak valid.")
                continue

            kode = input("Kode Produk (contoh: ELK08 / DGI02): ").strip().upper()
            if not kode:
                print("\n[Error] Kode produk tidak boleh kosong.")
                continue
            if cari_produk(katalog, kode):
                print("\n[Error] Kode produk sudah digunakan.")
                continue

            nama = input("Nama Produk: ").strip()
            if not nama:
                print("\n[Error] Nama produk tidak boleh kosong.")
                continue

            try:
                harga = float(input("Harga Produk (Rp): "))
                stok = int(input("Stok Awal: "))

                if jenis == "1":
                    garansi = int(input("Masa Garansi (bulan): "))
                    if garansi < 0:
                        raise ValueError("Masa garansi tidak boleh negatif.")
                    katalog.append(ProdukElektronik(kode, nama, harga, stok, garansi))
                else:
                    platform = input("Platform / Sistem (contoh: Steam, Netflix, Windows): ").strip()
                    if not platform:
                        raise ValueError("Platform tidak boleh kosong.")
                    katalog.append(ProdukDigital(kode, nama, harga, stok, platform))

                print(f"\n[Berhasil] Produk '{nama}' ditambahkan ke katalog.")
            except ValueError as e:
                print(f"\n[Error] Input tidak valid: {e}")

        elif pilihan == "4":
            print("\n--- RESTOCK PRODUK ---")
            kode = input("Masukkan Kode Produk: ")
            produk = cari_produk(katalog, kode)
            if produk:
                try:
                    tambahan = int(input(f"Jumlah stok masuk untuk '{produk.nama}': "))
                    produk.tambah_stok(tambahan)
                except ValueError:
                    print("\n[Error] Masukkan angka yang valid.")
            else:
                print("\n[Error] Kode produk tidak ditemukan.")

        elif pilihan == "5":
            print("\n--- UBAH HARGA PRODUK ---")
            kode = input("Masukkan Kode Produk: ")
            produk = cari_produk(katalog, kode)
            if produk:
                print(f"Harga saat ini: {Produk.format_rupiah(produk.harga)}")
                try:
                    harga_baru = float(input("Masukkan harga baru (Rp): "))
                    produk.harga = harga_baru  # Memanggil @harga.setter
                    print(f"\n[Berhasil] Harga '{produk.nama}' diperbarui menjadi {Produk.format_rupiah(produk.harga)}")
                except ValueError as e:
                    print(f"\n[Error] Gagal mengubah harga: {e}")
            else:
                print("\n[Error] Kode produk tidak ditemukan.")

        elif pilihan == "6":
            pendapatan = Produk.get_total_pendapatan()
            ppn = Produk.hitung_pajak_ppn(pendapatan)
            print("\n--- LAPORAN PENJUALAN ---")
            print(f"Total Jenis Produk : {Produk.get_total_produk()} item")
            print(f"Pendapatan Bersih  : {Produk.format_rupiah(pendapatan)}")
            print(f"Total PPN (11%)    : {Produk.format_rupiah(ppn)}")

        elif pilihan == "0":
            print("\nProgram selesai. Terima kasih!")
            break

        else:
            print("\n[Error] Menu tidak tersedia, silakan pilih 0-6.")


if __name__ == "__main__":
    jalankan_aplikasi()