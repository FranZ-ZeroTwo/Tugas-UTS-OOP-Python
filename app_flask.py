from flask import Flask, render_template, request, redirect, url_for, flash
from produk import Produk, ProdukElektronik, ProdukDigital
from storage import muat_data, simpan_data

app = Flask(__name__)
app.secret_key = "franz-x-store-secret-key"


@app.route("/")
def index():
    daftar_produk = muat_data()
    total_aset = sum(item.harga * item.stok for item in daftar_produk)
    total_stok = sum(item.stok for item in daftar_produk)
    return render_template(
        "index.html",
        nama_toko=Produk.nama_toko,
        pajak_persen=round(Produk.pajak * 100, 2),
        daftar_produk=daftar_produk,
        total_aset=Produk.format_rupiah(total_aset),
        total_stok=total_stok,
        format_rupiah=Produk.format_rupiah,
    )


@app.route("/tambah", methods=["POST"])
def tambah_produk():
    daftar_produk = muat_data()
    tipe = request.form.get("tipe")
    kode = request.form.get("kode", "").strip().upper()
    nama = request.form.get("nama", "").strip()

    try:
        harga = float(request.form.get("harga", 0))
        stok = int(request.form.get("stok", 0))

        if any(p.kode == kode for p in daftar_produk):
            raise ValueError(f"Kode produk '{kode}' sudah digunakan!")
        if stok < 0:
            raise ValueError("Stok awal tidak boleh negatif!")

        if tipe == "elektronik":
            garansi = int(request.form.get("garansi_bulan", 12))
            produk_baru = ProdukElektronik(kode, nama, harga, stok, garansi)
        else:
            lisensi = request.form.get("jenis_lisensi", "Personal").strip()
            produk_baru = ProdukDigital(kode, nama, harga, stok, lisensi)

        daftar_produk.append(produk_baru)
        simpan_data(daftar_produk)
        flash(f"Berhasil menambahkan {nama} ({kode}).", "success")
    except ValueError as e:
        flash(f"Validasi Gagal: {e}", "error")

    return redirect(url_for("index"))


@app.route("/stok/<kode>/<aksi>", methods=["POST"])
def ubah_stok(kode, aksi):
    daftar_produk = muat_data()
    try:
        for item in daftar_produk:
            if item.kode == kode:
                if aksi == "tambah":
                    item.tambah_stok(1)
                elif aksi == "kurang":
                    item.kurangi_stok(1)
                simpan_data(daftar_produk)
                flash(f"Stok {item.nama} diperbarui menjadi {item.stok}.", "success")
                break
    except ValueError as e:
        flash(f"Validasi Stok: {e}", "error")

    return redirect(url_for("index"))


@app.route("/harga/<kode>", methods=["POST"])
def ubah_harga(kode):
    daftar_produk = muat_data()
    try:
        harga_baru = float(request.form.get("harga_baru", 0))
        for item in daftar_produk:
            if item.kode == kode:
                # Memicu @harga.setter pada kelas Produk
                item.harga = harga_baru
                simpan_data(daftar_produk)
                flash(f"Harga {item.nama} diubah menjadi {Produk.format_rupiah(item.harga)}.", "success")
                break
    except ValueError as e:
        flash(f"Validasi Encapsulation: {e}", "error")

    return redirect(url_for("index"))


@app.route("/pajak", methods=["POST"])
def ubah_pajak():
    daftar_produk = muat_data()
    try:
        pajak_persen = float(request.form.get("pajak_persen", 11))
        # Memicu @classmethod ubah_pajak
        Produk.ubah_pajak(pajak_persen / 100)
        simpan_data(daftar_produk)
        flash(f"Tarif PPN toko diperbarui menjadi {pajak_persen}%.", "success")
    except ValueError as e:
        flash(f"Validasi Pajak: {e}", "error")

    return redirect(url_for("index"))


@app.route("/hapus/<kode>", methods=["POST"])
def hapus_produk(kode):
    daftar_produk = muat_data()
    daftar_produk = [item for item in daftar_produk if item.kode != kode]
    simpan_data(daftar_produk)
    flash(f"Produk {kode} telah dihapus.", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)