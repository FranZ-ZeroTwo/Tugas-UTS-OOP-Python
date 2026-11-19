import json
import os
from produk import Produk, ProdukElektronik, ProdukDigital

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_DATA = os.path.join(BASE_DIR, "data_toko.json")


def simpan_data(daftar_produk: list[Produk]):
    data_simpan = {
        "pajak": Produk.pajak,
        "produk": []
    }
    for item in daftar_produk:
        if isinstance(item, ProdukElektronik):
            data_simpan["produk"].append({
                "tipe": "elektronik",
                "kode": item.kode,
                "nama": item.nama,
                "harga": item.harga,
                "stok": item.stok,
                "garansi_bulan": item.garansi_bulan
            })
        elif isinstance(item, ProdukDigital):
            data_simpan["produk"].append({
                "tipe": "digital",
                "kode": item.kode,
                "nama": item.nama,
                "harga": item.harga,
                "stok": item.stok,
                "jenis_lisensi": item.jenis_lisensi
            })

    with open(FILE_DATA, "w", encoding="utf-8") as f:
        json.dump(data_simpan, f, indent=4)


def muat_data() -> list[Produk]:
    if not os.path.exists(FILE_DATA):
        # Data awal bawaan jika file JSON belum ada
        data_awal = [
            ProdukElektronik("ELK-01", "Laptop Gaming MSI Thin 15", 11500000, 5, 24),
            ProdukElektronik("ELK-02", "Mouse Wireless Logitech", 350000, 15, 12),
            ProdukDigital("DIG-01", "Lisensi Windows 11 Pro", 450000, 30, "Lifetime Key"),
        ]
        simpan_data(data_awal)
        return data_awal

    with open(FILE_DATA, "r", encoding="utf-8") as f:
        raw = json.load(f)

    Produk.ubah_pajak(raw.get("pajak", 0.11))
    daftar_produk = []

    for d in raw.get("produk", []):
        if d["tipe"] == "elektronik":
            daftar_produk.append(
                ProdukElektronik(d["kode"], d["nama"], d["harga"], d["stok"], d["garansi_bulan"])
            )
        elif d["tipe"] == "digital":
            daftar_produk.append(
                ProdukDigital(d["kode"], d["nama"], d["harga"], d["stok"], d["jenis_lisensi"])
            )

    return daftar_produk