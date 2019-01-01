import unittest
import textwrap
from set1_challenge5 import encrypt_xor


class TestChallenge(unittest.TestCase):

    def test(self):
        input = ("Burning 'em, if you ain't quick and nimble\n"
                 "I go crazy when I hear a cymbal")
        key = "ICE"
        encrypted = encrypt_xor(input, key)
        expected = ("0b3637272a2b2e63622c2e69692a23693a2a3"
                    "c6324202d623d63343c2a2622632427276527"
                    "2a282b2f20430a652e2c652a3124333a653e2"
                    "b2027630c692b20283165286326302e27282f")
        self.assertEqual(
            encrypted, expected)


if __name__ == '__main__':
    unittest.main()
