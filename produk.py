from abc import ABC, abstractmethod


# 1. ABSTRACTION: Kelas abstrak sebagai kerangka dasar
class Produk(ABC):
    nama_toko = "FranZ x Store"
    pajak = 0.11  # PPN 11%

    def __init__(self, kode: str, nama: str, harga: float, stok: int):
        self.kode = kode
        self.nama = nama
        self._stok = stok       # Protected attribute
        self.__harga = 0.0      # Private attribute
        self.harga = harga      # Memanggil setter untuk validasi

    # 2. ENCAPSULATION: Getter & Setter
    @property
    def harga(self) -> float:
        return self.__harga

    @harga.setter
    def harga(self, nilai: float):
        if nilai < 0:
            raise ValueError("Harga produk tidak boleh negatif!")
        self.__harga = float(nilai)

    @property
    def stok(self) -> int:
        return self._stok

    def hitung_harga_akhir(self) -> float:
        return self.__harga + (self.__harga * self.pajak)

    def tambah_stok(self, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah penambahan stok harus lebih dari 0!")
        self._stok += jumlah

    def kurangi_stok(self, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah pengurangan stok harus lebih dari 0!")
        if jumlah > self._stok:
            raise ValueError(f"Stok {self.nama} tidak mencukupi (tersisa {self._stok})!")
        self._stok -= jumlah

    @abstractmethod
    def tampilkan_info(self) -> str:
        pass

    @classmethod
    def ubah_pajak(cls, pajak_baru: float):
        if pajak_baru < 0:
            raise ValueError("Persentase pajak tidak boleh negatif!")
        cls.pajak = pajak_baru

    @staticmethod
    def format_rupiah(nominal: float) -> str:
        return f"Rp {nominal:,.0f}".replace(",", ".")


# 3. INHERITANCE & 4. POLYMORPHISM: Subclass Produk Elektronik
class ProdukElektronik(Produk):
    def __init__(self, kode: str, nama: str, harga: float, stok: int, garansi_bulan: int):
        super().__init__(kode, nama, harga, stok)
        self.garansi_bulan = garansi_bulan

    def tampilkan_info(self) -> str:
        return (
            f"[Elektronik] {self.kode} - {self.nama} | "
            f"Garansi: {self.garansi_bulan} Bulan | Stok: {self._stok}"
        )


# 3. INHERITANCE & 4. POLYMORPHISM: Subclass Produk Digital
class ProdukDigital(Produk):
    def __init__(self, kode: str, nama: str, harga: float, stok: int, jenis_lisensi: str):
        super().__init__(kode, nama, harga, stok)
        self.jenis_lisensi = jenis_lisensi

    def tampilkan_info(self) -> str:
        return (
            f"[Digital] {self.kode} - {self.nama} | "
            f"Lisensi: {self.jenis_lisensi} | Stok: {self._stok}"
        )