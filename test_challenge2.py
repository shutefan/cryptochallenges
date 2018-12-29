import unittest
import set1_challenge2


class TestChallenge(unittest.TestCase):

    def test(self):
        buf1 = "1c0111001f010100061a024b53535009181c"
        buf2 = "686974207468652062756c6c277320657965"
        xored = set1_challenge2.xor_buffers(buf1, buf2)
        self.assertEqual(
            xored, "746865206b696420646f6e277420706c6179")


if __name__ == '__main__':
    unittest.main()
