import unittest

from encrypt_sp.helper.rot_13 import *

class TestRot13(unittest.TestCase):

    def test_rot13_fixed_strings(self):
        self.assertEqual(rot13('test'), 'grfg')
        self.assertEqual(rot13('Test'), 'Grfg')
        self.assertEqual(rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%')

    def test_rot13_decrypt(self):
        self.assertEqual(rot13('grfg'), 'test')
        self.assertEqual(rot13('Grfg'), 'Test')
        self.assertEqual(rot13('nN oO mM 1234 *!?%'), 'aA bB zZ 1234 *!?%')



if __name__ == '__main__':
    unittest.main()