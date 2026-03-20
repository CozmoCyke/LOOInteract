from __future__ import annotations

from looi.constants import LAMP_OFF, LAMP_ON, UUID_FED2, UUID_FED9
from looi.transport_ble import BleTransport


class LooiClient:
    def __init__(self) -> None:
        self.transport = BleTransport()

    async def scan(self, timeout: float = 10.0):
        return await self.transport.scan(timeout=timeout)

    async def connect(self, address: str, timeout: float = 10.0) -> None:
        await self.transport.connect(address=address, timeout=timeout)

    async def disconnect(self) -> None:
        await self.transport.disconnect()

    async def lamp_on(self) -> None:
        await self.transport.write(UUID_FED2, LAMP_ON, response=False)

    async def lamp_off(self) -> None:
        await self.transport.write(UUID_FED2, LAMP_OFF, response=False)

    async def read_sensors_raw(self) -> bytes:
        return await self.transport.read(UUID_FED9)