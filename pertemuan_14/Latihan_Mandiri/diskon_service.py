import pdb

class DiskonCalculator:
    """Menghitung harga akhir setelah diskon."""

    def hitung_diskon(self, harga_awal: float, persentase_diskon: int) -> float:
        # pdb.set_trace()

        # Hitung diskon
        jumlah_diskon = harga_awal * persentase_diskon / 100
        harga_setelah_diskon = harga_awal - jumlah_diskon

        # BUG BARU: PPN 10% ditambahkan tidak sengaja
        ppn = harga_setelah_diskon * 0.10
        harga_akhir = harga_setelah_diskon + ppn

        return harga_akhir
