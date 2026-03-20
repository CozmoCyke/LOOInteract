from __future__ import annotations

from bleak import BleakClient, BleakScanner

from looi.constants import DEFAULT_TIMEOUT


class BleTransport:
    def __init__(self) -> None:
        self.client: BleakClient | None = None
        self.address: str | None = None

    async def scan(self, timeout: float = DEFAULT_TIMEOUT):
        return await BleakScanner.discover(timeout=timeout)

    async def connect(self, address: str, timeout: float = DEFAULT_TIMEOUT) -> None:
        self.address = address
        self.client = BleakClient(address, timeout=timeout)
        await self.client.connect()

    async def disconnect(self) -> None:
        if self.client is not None and self.client.is_connected:
            await self.client.disconnect()

    async def write(self, char_uuid: str, data: bytes, response: bool = False) -> None:
        if self.client is None or not self.client.is_connected:
            raise RuntimeError("BLE client is not connected")
        await self.client.write_gatt_char(char_uuid, data, response=response)

    async def read(self, char_uuid: str) -> bytes:
        if self.client is None or not self.client.is_connected:
            raise RuntimeError("BLE client is not connected")
        return await self.client.read_gatt_char(char_uuid)

    async def start_notify(self, char_uuid: str, callback) -> None:
        if self.client is None or not self.client.is_connected:
            raise RuntimeError("BLE client is not connected")
        await self.client.start_notify(char_uuid, callback)

    async def stop_notify(self, char_uuid: str) -> None:
        if self.client is None or not self.client.is_connected:
            raise RuntimeError("BLE client is not connected")
        await self.client.stop_notify(char_uuid)