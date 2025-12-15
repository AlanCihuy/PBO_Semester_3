# Refactoring Log: SOLID Implementation

Ringkasan teknis transformasi kode legacy `OrderManager` menuju Clean Architecture.

---

## 1. Single Responsibility Principle (SRP)
> *Pisahkan kode berdasarkan alasan perubahannya.*

* ** Problem (Monolith):** Class `OrderManager` overload. Ia menangani logika bisnis, transaksi pembayaran, hingga pengiriman email sekaligus.
* ** Solution (Decoupling):** Pecah tanggung jawab menjadi micro-component:
    * `CheckoutService`: Orkestrator alur.
    * `PaymentService`: Khusus logika gerbang pembayaran.
    * `NotificationService`: Khusus handling alert/email.

## 2. Open/Closed Principle (OCP)
> *Tambah fitur baru tanpa menyentuh kode lama.*

* ** Problem (Rigid):** Menambah metode pembayaran baru (misal: E-Wallet) memaksa kita mengedit blok `if-else` raksasa di kode utama. Risiko bug tinggi.
* ** Solution (Polymorphism):** Gunakan **Strategy Pattern**. Metode baru cukup dibuat sebagai class baru yang mengadopsi interface `IPayment`. Kode lama tetap aman (closed for modification).

## 3. Dependency Inversion Principle (DIP)
> *Bergantung pada kontrak (interface), bukan detail.*

* ** Problem (Tight Coupling):** Modul checkout memanggil langsung class `CreditCardPayment`. Kode jadi kaku dan susah di-unit test (karena susah di-mock).
* ** Solution (Injection):** Terapkan **Dependency Injection**. `CheckoutService` hanya tahu interface abstrak. Implementasi asli (Bank/QRIS) disuntikkan dari luar saat runtime.

---

1.  **Testability:** Mudah membuat mock object untuk pengujian.
2.  **Scalability:** Menambah fitur pembayaran semudah membuat file baru.
3.  **Maintainability:** Bug di satu fitur tidak akan merembet ke fitur lain.