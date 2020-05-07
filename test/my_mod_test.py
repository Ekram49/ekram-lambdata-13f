#test/my_mod.py

from my_lambdata.my_mod import enlarge

import unittest

class TestMyMod(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(enlarge(9), 900)


if __name__ == '__main__':
    unittest.main()