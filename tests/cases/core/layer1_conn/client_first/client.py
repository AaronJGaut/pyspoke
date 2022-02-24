import sys
import os
import asyncio
import spoke

name = os.getenv("name", "unnamed")
count = int(os.getenv("count", 1000))
delay = float(os.getenv("delay", 1))


async def main():
    client = spoke.conn.socket.Client()
    async with await client.connect() as conn:
        print("Connected")

        async def echo(conn):
            try:
                async for data in conn:
                    print(f"recv: {data.decode('utf8')}")
            except ConnectionError:
                pass
            print("Disconnected")

        asyncio.create_task(echo(conn))

        try:
            for i in range(count):
                msg = "{} {}".format(name, i)
                print(f"sending: {msg}")
                await conn.send(msg.encode("utf8"))
                await asyncio.sleep(delay)
        except ConnectionError:
            pass


asyncio.run(main())
