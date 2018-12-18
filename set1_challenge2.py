def xor_buffers(hex_buf1: str, hex_buf2: str) -> str:
    raw1 = bytes.fromhex(hex_buf1)
    raw2 = bytes.fromhex(hex_buf2)
    xored = [b1 ^ b2 for b1, b2 in zip(raw1, raw2)]
    return bytes.hex(bytes(xored))
