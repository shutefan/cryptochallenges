from typing import List
import string
import itertools


class XorDecryptResult:
    def __init__(self, score: int, cypher: str, encrypted: str,
                 decrypted: str) -> None:
        self.score = score
        self.cypher = cypher
        self.encrypted = encrypted
        self.decrypted = decrypted

    def __str__(self) -> str:
        return "score: {}, cypher: {}, encrypted: {}, decrypted: {}".format(
            self.score, self.cypher, self.encrypted, self.decrypted)

    def __repr__(self) -> str:
        return self.__str__()


def decrypt_xor(encrypted: str) -> List[XorDecryptResult]:
    raw = bytes.fromhex(encrypted)
    results = []

    for c in string.ascii_letters:
        decrypted = bytes([b ^ ord(c) for b in raw])
        as_ascii = decrypted.decode('ascii')
        score = _score(as_ascii)
        results.append(XorDecryptResult(score, c, encrypted, as_ascii))

    results.sort(key=lambda elem: elem.score, reverse=True)
    return results


def _score(candidate: str) -> int:
    score = 0
    for c in candidate:
        if str.isalpha(c) or c == " ":
            score += 1
    return score
