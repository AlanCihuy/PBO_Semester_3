import unittest
from diskon_service import DiskonCalculator

class TestDiskonLanjut(unittest.TestCase):

    def setUp(self):
        self.calc = DiskonCalculator()

    def test_diskon_float_33_persen(self):
        """Tes 5: Diskon float 33% pada harga 999"""
        hasil = self.calc.hitung_diskon(999, 33)
        expected = 999 - (999 * 0.33)
        self.assertAlmostEqual(hasil, expected, places=2)

    def test_edge_case_harga_nol(self):
        """Tes 6: Edge Case harga awal 0"""
        hasil = self.calc.hitung_diskon(0, 50)
        self.assertEqual(hasil, 0.0)

if __name__ == "__main__":
    unittest.main()
