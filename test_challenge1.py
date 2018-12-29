import unittest
import set1_challenge1


class TestChallenge(unittest.TestCase):

    def test(self):
        hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        b64_string = set1_challenge1.hex_to_b64(hex_string)
        self.assertEqual(
            b64_string, "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")


if __name__ == '__main__':
    unittest.main()
