"""
====================================================
LATIHAN MANDIRI – REFACTORING SOLID
Studi Kasus: Sistem Booking Hotel
====================================================
Penjelasan Singkat:
File ini merupakan hasil refactoring sistem booking hotel
dengan menerapkan prinsip SOLID, khususnya:
- SRP (Single Responsibility Principle)
- OCP (Open/Closed Principle)
- DIP (Dependency Inversion Principle)
Kode sebelum refactor tidak disertakan sesuai instruksi.
====================================================
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass

# ==================================================
# MODEL
# ==================================================
@dataclass
class Booking:
    """
    Model data Booking.
    Bertanggung jawab hanya menyimpan data booking.
    (Penerapan SRP)
    """
    customer_name: str
    room_type: str
    status: str = "pending"
# ==================================================
# ABSTRAKSI (INTERFACE)
# ==================================================
class IPaymentProcessor(ABC):
    """
    Kontrak untuk semua metode pembayaran.
    Mendukung OCP & DIP.
    """
    @abstractmethod
    def process(self, booking: Booking) -> bool:
        pass
class INotificationService(ABC):
    """
    Kontrak untuk semua layanan notifikasi.
    Mendukung OCP & DIP.
    """
    @abstractmethod
    def send(self, booking: Booking):
        pass
class IRoomValidator(ABC):
    """
    Kontrak untuk validasi kamar hotel.
    Mendukung SRP & DIP.
    """
    @abstractmethod
    def validate(self, booking: Booking) -> bool:
        pass
# ==================================================
# IMPLEMENTASI KONKRIT (PLUG-IN)
# ==================================================
class RoomValidator(IRoomValidator):
    """
    Implementasi validasi kamar hotel.
    """
    def validate(self, booking: Booking) -> bool:
        if booking.room_type in ["standard", "deluxe"]:
            print(f"Kamar {booking.room_type} tersedia.")
            return True
        print("Kamar tidak tersedia.")
        return False
class CreditCardPayment(IPaymentProcessor):
    """
    Implementasi pembayaran menggunakan Credit Card.
    """
    def process(self, booking: Booking) -> bool:
        print("Payment: Memproses Credit Card.")
        return True
class EmailNotification(INotificationService):
    """
    Implementasi notifikasi melalui email.
    """
    def send(self, booking: Booking):
        print(f"Notif: Email konfirmasi dikirim ke {booking.customer_name}.")
# ==================================================
# KELAS KOORDINATOR (SRP & DIP)
# ==================================================
class BookingService:
    """
    Kelas koordinator booking hotel.
    Tanggung jawab:
    - Mengorkestrasi proses booking
    - Tidak mengandung logika detail implementasi
    Menerapkan:
    - SRP: hanya mengatur alur booking
    - DIP: bergantung pada abstraksi
    """
    def __init__(
        self,
        room_validator: IRoomValidator,
        payment_processor: IPaymentProcessor,
        notifier: INotificationService
    ):
        self.room_validator = room_validator
        self.payment_processor = payment_processor
        self.notifier = notifier
    def book(self, booking: Booking) -> bool:
        if not self.room_validator.validate(booking):
            return False

        if self.payment_processor.process(booking):
            booking.status = "confirmed"
            self.notifier.send(booking)
            print("Booking berhasil.\n")
            return True
        return False
# ==================================================
# PEMBUKTIAN OCP (CHALLENGE)
# ==================================================
class QrisPayment(IPaymentProcessor):
    """
    Metode pembayaran baru (QRIS).
    Ditambahkan tanpa mengubah BookingService.
    (Pembuktian OCP)
    """
    def process(self, booking: Booking) -> bool:
        print("Payment: Memproses QRIS.")
        return True
# ==================================================
# PROGRAM UTAMA
# ==================================================
if __name__ == "__main__":
    # Dependency setup
    validator = RoomValidator()
    notifier = EmailNotification()
    # Skenario 1: Credit Card
    booking1 = Booking("Andi", "deluxe")
    cc_payment = CreditCardPayment()
    service_cc = BookingService(validator, cc_payment, notifier)
    print("--- Booking dengan Credit Card ---")
    service_cc.book(booking1)
    # Skenario 2: QRIS (Pembuktian OCP)
    booking2 = Booking("Budi", "standard")
    qris_payment = QrisPayment()
    service_qris = BookingService(validator, qris_payment, notifier)
    print("--- Booking dengan QRIS (OCP Proof) ---")
    service_qris.book(booking2)
