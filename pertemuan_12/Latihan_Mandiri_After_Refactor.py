"""
====================================================
LATIHAN MANDIRI – DOKUMENTASI & VERSION CONTROL
Studi Kasus: Sistem Booking Hotel
====================================================

File ini merupakan pengembangan lanjutan dari hasil
refactoring SOLID pada sistem booking hotel dengan:
- Penambahan Docstring (Google Style)
- Penggunaan Logging (INFO & WARNING)
====================================================
"""
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
# ==================================================
# LOGGING CONFIGURATION
# ==================================================
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s"
)
logger = logging.getLogger(__name__)
# ==================================================
# MODEL
# ==================================================
@dataclass
class Booking:
    """
    Menyimpan data booking hotel.

    Attributes:
        customer_name (str): Nama pelanggan.
        room_type (str): Jenis kamar yang dipesan.
        status (str): Status booking.
    """
    customer_name: str
    room_type: str
    status: str = "pending"
# ==================================================
# ABSTRAKSI (INTERFACE)
# ==================================================
class IRoomValidator(ABC):
    """
    Interface untuk validasi kamar hotel.
    """

    @abstractmethod
    def validate(self, booking: Booking) -> bool:
        """
        Melakukan validasi ketersediaan kamar.

        Args:
            booking (Booking): Data booking.

        Returns:
            bool: True jika kamar valid, False jika tidak.
        """
        pass
class IPaymentProcessor(ABC):
    """
    Interface untuk pemrosesan pembayaran.
    """

    @abstractmethod
    def process(self, booking: Booking) -> bool:
        """
        Memproses pembayaran booking.

        Args:
            booking (Booking): Data booking.

        Returns:
            bool: True jika pembayaran berhasil.
        """
        pass
class INotificationService(ABC):
    """
    Interface untuk layanan notifikasi.
    """

    @abstractmethod
    def send(self, booking: Booking):
        """
        Mengirim notifikasi booking.

        Args:
            booking (Booking): Data booking.
        """
        pass
# ==================================================
# IMPLEMENTASI RULE & SERVICE
# ==================================================
class RoomValidator(IRoomValidator):
    """
    Rule validasi kamar hotel.
    """
    def validate(self, booking: Booking) -> bool:
        """
        Mengecek apakah kamar tersedia.
        Args:
            booking (Booking): Data booking.
        Returns:
            bool: Status validasi kamar.
        """
        if booking.room_type in ["standard", "deluxe"]:
            logger.info("Kamar %s tersedia.", booking.room_type)
            return True

        logger.warning("Kamar %s tidak tersedia.", booking.room_type)
        return False
class CreditCardPayment(IPaymentProcessor):
    """
    Pembayaran menggunakan Credit Card.
    """
    def process(self, booking: Booking) -> bool:
        """
        Memproses pembayaran credit card.

        Args:
            booking (Booking): Data booking.

        Returns:
            bool: Status pembayaran.
        """
        logger.info("Memproses pembayaran Credit Card untuk %s.", booking.customer_name)
        return True
class EmailNotification(INotificationService):
    """
    Notifikasi booking melalui email.
    """
    def send(self, booking: Booking):
        """
        Mengirim email konfirmasi booking.

        Args:
            booking (Booking): Data booking.
        """
        logger.info("Email konfirmasi dikirim ke %s.", booking.customer_name)
# ==================================================
# SERVICE UTAMA (Seperti RegistrationService)
# ==================================================
class BookingService:
    """
    Service utama untuk mengelola proses booking hotel.
    """

    def __init__(
        self,
        room_validator: IRoomValidator,
        payment_processor: IPaymentProcessor,
        notifier: INotificationService
    ):
        """
        Constructor BookingService.

        Args:
            room_validator (IRoomValidator): Validator kamar.
            payment_processor (IPaymentProcessor): Metode pembayaran.
            notifier (INotificationService): Layanan notifikasi.
        """
        self.room_validator = room_validator
        self.payment_processor = payment_processor
        self.notifier = notifier

    def book(self, booking: Booking) -> bool:
        """
        Menjalankan proses booking hotel.

        Args:
            booking (Booking): Data booking.

        Returns:
            bool: True jika booking berhasil.
        """
        logger.info("Memulai booking untuk %s.", booking.customer_name)

        if not self.room_validator.validate(booking):
            logger.warning("Booking gagal karena kamar tidak valid.")
            return False

        if self.payment_processor.process(booking):
            booking.status = "confirmed"
            self.notifier.send(booking)
            logger.info("Booking berhasil.")
            return True

        logger.warning("Booking gagal pada tahap pembayaran.")
        return False
# ==================================================
# PROGRAM UTAMA
# ==================================================
if __name__ == "__main__":
    validator = RoomValidator()
    payment = CreditCardPayment()
    notifier = EmailNotification()

    booking = Booking("Andi", "deluxe")
    service = BookingService(validator, payment, notifier)
    service.book(booking)