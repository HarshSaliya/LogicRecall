import asyncio
import time
import random

start = time.time()

class DevicePoller:
    
    def __init__(self, name):
        self.name = name
        
    async def connect(self):
        delay = random.randint(1,5)
        print(f"{self.name}: Connecting...")
        await asyncio.sleep(delay)
        print(f"{self.name}: Connected in {delay}s")


    async def fetch_data(self):
        delay = random.randint(1, 3)
        print(f"{self.name}: Fetching data...")
        await asyncio.sleep(delay)
        print(f"{self.name}: Data received")
        return f"{self.name} DATA"

    async def poll(self):
        await self.connect()
        data = await self.fetch_data()
        return data

async def main():
    devices = [
        DevicePoller("Cisco"),
        DevicePoller("PaloAlto"),
        DevicePoller("Fortinet")
    ]

    results = await asyncio.gather(
        *(device.poll() for device in devices)
    )

    print("\nFinal Results:", results)


asyncio.run(main())

end = time.time()
print(f"Total time: {end - start:.4f} seconds")