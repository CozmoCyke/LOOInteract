# Known BLE characteristic UUIDs for LOOI

UUID_FE00 = "0000fe00-0000-1000-8000-00805f9b34fb"
UUID_FED0 = "0000fed0-0000-1000-8000-00805f9b34fb"
UUID_FED1 = "0000fed1-0000-1000-8000-00805f9b34fb"
UUID_FED2 = "0000fed2-0000-1000-8000-00805f9b34fb"
UUID_FED9 = "0000fed9-0000-1000-8000-00805f9b34fb"
UUID_FF02 = "0000ff02-0000-1000-8000-00805f9b34fb"

KNOWN_CHARACTERISTICS = {
    "fe00": UUID_FE00,
    "fed0": UUID_FED0,
    "fed1": UUID_FED1,
    "fed2": UUID_FED2,
    "fed9": UUID_FED9,
    "ff02": UUID_FF02,
}

DEFAULT_TIMEOUT = 10.0

# Simple known commands
LAMP_OFF = bytes.fromhex("00")
LAMP_ON = bytes.fromhex("03")