import asyncio

from looi.client import LooiClient


async def main() -> None:
    client = LooiClient()
    devices = await client.scan()

    for device in devices:
        print(f"{device.address}  {device.name}")


if __name__ == "__main__":
    asyncio.run(main())
