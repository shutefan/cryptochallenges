from typing import List
from set1_challenge3 import XorDecryptResult, decrypt_xor


def find_xored(filepath: str) -> List[XorDecryptResult]:
    results = []
    with open(filepath, 'r') as f:
        for line in f:
            results_for_line = decrypt_xor(line.rstrip("\n"))
            if results_for_line:
                results.extend(_get_highest_scoring(results_for_line))

    results.sort(key=lambda elem: elem.score, reverse=True)
    return results


def _get_highest_scoring(xs: List[XorDecryptResult]) -> List[XorDecryptResult]:
    highest: List[XorDecryptResult] = [xs[0]]
    for x in xs[1:]:
        if x.score == xs[0].score:
            highest.append(x)
    return highest

if __name__ == '__main__':
    input = "./challenge-data/4.txt"
    result = find_xored(input)
    for r in result:
        print("{} {}".format(r.score, r.decrypted))
