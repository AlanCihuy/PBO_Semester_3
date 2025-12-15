# === KODE BURUK (SEBELUM REFACTOR) ===
class BookingManager:  # Melanggar SRP, OCP, DIP
    def process_booking(self, customer_name, room_type, payment_method):
        print(f"Booking untuk {customer_name}")

        # Validasi kamar
        if room_type == "deluxe":
            print("Kamar Deluxe tersedia")
        elif room_type == "standard":
            print("Kamar Standard tersedia")
        else:
            print("Tipe kamar tidak tersedia")
            return False

        # Pembayaran (hardcoded)
        if payment_method == "credit_card":
            print("Memproses pembayaran Credit Card")
        elif payment_method == "bank_transfer":
            print("Memproses pembayaran Bank Transfer")
        else:
            print("Metode pembayaran tidak valid")
            return False

        # Notifikasi
        print(f"Mengirim email konfirmasi ke {customer_name}")
        print("Booking sukses")
        return True
