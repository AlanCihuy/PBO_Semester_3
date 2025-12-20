# Debug Report – Bug PPN 10%

## Tujuan
Menemukan bug perhitungan PPN 10% yang menyebabkan harga akhir lebih besar dari seharusnya.

## Langkah Debugging
1. Tambahkan breakpoint:
   pdb.set_trace()

2. Jalankan program:
   python diskon_service.py

3. Periksa nilai variabel menggunakan perintah `p`.

## Hasil Observasi
Input:
- harga_awal = 1000
- persentase_diskon = 10

Perintah pdb:
(pdb) p harga_setelah_diskon
900.0

(pdb) p ppn
90.0

(pdb) p harga_akhir
990.0

## Analisis
Harga setelah diskon sudah benar (900).
Namun PPN 10% ditambahkan lagi di fungsi ini,
padahal sistem lain juga menambahkan PPN.

## Kesimpulan
PPN dihitung dua kali.
Solusi: Hilangkan perhitungan PPN dari fungsi hitung_diskon.
