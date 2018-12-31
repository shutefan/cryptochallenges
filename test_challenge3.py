import unittest
from set1_challenge3 import *


class TestChallenge(unittest.TestCase):

    def test(self):
        input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
        result = decrypt_xor(input)
        self.assertEqual(
            result[0].decrypted, "Cooking MC's like a pound of bacon")


if __name__ == '__main__':
    unittest.main()
