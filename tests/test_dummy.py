import unittest

from todue.dummy import dummy


class TestDummy(unittest.TestCase):
    def test_dummy(self) -> None:
        self.assertTrue(dummy())
