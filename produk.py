from abc import ABC, abstractmethod


# 1. ABSTRACTION: Kelas abstrak sebagai kerangka dasar
class Produk(ABC):
  # Class Attribute (berlaku untuk semua objek)
  nama_toko = "FranZ x Store"
  pajak = 0.11  # PPN 11%

  def __init__(self, kode: str, nama: str, harga: float, stok: int):
    self.kode = kode  # Public attribute
    self.nama = nama  # Public attribute
    self._stok = stok  # Protected attribute
    self.__harga = 0  # Private attribute (Encapsulation)
    self.harga = harga  # Memanggil setter @harga.setter untuk validasi

  # 2. ENCAPSULATION menggunakan @property (Getter & Setter)
  @property
  def harga(self) -> float:
    return self.__harga

  @harga.setter
  def harga(self, nilai: float):
    if nilai < 0:
      raise ValueError("Harga tidak boleh bernilai negatif!")
    self.__harga = nilai

  # 3. INSTANCE METHOD (menggunakan parameter self)
  def kurangi_stok(self, jumlah: int):
    if jumlah <= self._stok:
      self._stok -= jumlah
    else:
      print(f"Stok {self.nama} tidak mencukupi!")

  # 4. CLASS METHOD (menggunakan parameter cls)
  @classmethod
  def ubah_pajak(cls, pajak_baru: float):
    cls.pajak = pajak_baru

  # 5. STATIC METHOD (fungsi bantu tanpa self maupun cls)
  @staticmethod
  def format_rupiah(nominal: float) -> str:
    return f"Rp{nominal:,.0f}".replace(",", ".")

  # Abstract Method (wajib di-override oleh kelas anak)
  @abstractmethod
  def hitung_harga_akhir(self) -> float:
    pass

  @abstractmethod
  def tampilkan_info(self) -> str:
    pass


# 6. INHERITANCE: Pewarisan dari kelas induk Produk
class ProdukElektronik(Produk):

  def __init__(
      self, kode: str, nama: str, harga: float, stok: int, garansi_bulan: int
  ):
    super().__init__(kode, nama, harga, stok)
    self.garansi_bulan = garansi_bulan

  # 7. POLYMORPHISM: Override method sesuai aturan produk elektronik
  def hitung_harga_akhir(self) -> float:
    return self.harga + (self.harga * Produk.pajak)

  def tampilkan_info(self) -> str:
    harga_str = self.format_rupiah(self.hitung_harga_akhir())
    return (
        f"[Elektronik] {self.kode} - {self.nama} | "
        f"Garansi: {self.garansi_bulan} bln | Stok: {self._stok} | "
        f"Harga (+PPN): {harga_str}"
    )


class ProdukDigital(Produk):

  def __init__(
      self, kode: str, nama: str, harga: float, stok: int, diskon_persen: float
  ):
    super().__init__(kode, nama, harga, stok)
    self.diskon_persen = diskon_persen

  # 7. POLYMORPHISM: Override method dengan perhitungan diskon khusus
  def hitung_harga_akhir(self) -> float:
    potongan = self.harga * (self.diskon_persen / 100)
    harga_diskon = self.harga - potongan
    return harga_diskon + (harga_diskon * Produk.pajak)

  def tampilkan_info(self) -> str:
    harga_str = self.format_rupiah(self.hitung_harga_akhir())
    return (
        f"[Digital]    {self.kode} - {self.nama} | "
        f"Diskon: {self.diskon_persen}% | Stok: {self._stok} | "
        f"Harga (+PPN): {harga_str}"
    )