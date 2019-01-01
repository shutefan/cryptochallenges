import itertools


def encrypt_xor(input: str, key: str) -> str:
    input_bytes = input.encode(encoding='ascii')
    key_bytes = key.encode(encoding='ascii')
    xored_input = [i ^ k for i, k in zip(
        input_bytes, itertools.cycle(key_bytes))]
    return bytes.hex(bytes(xored_input))
