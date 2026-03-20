from __future__ import annotations


def hex_to_bytes(data: str) -> bytes:
    cleaned = data.replace(" ", "").replace("\n", "").replace("\r", "")
    if len(cleaned) % 2 != 0:
        raise ValueError(f"Hex string must contain an even number of characters: {cleaned}")
    return bytes.fromhex(cleaned)


def bytes_to_hex(data: bytes) -> str:
    return data.hex()


def inc_u16(value: int) -> int:
    return (value + 1) & 0xFFFF