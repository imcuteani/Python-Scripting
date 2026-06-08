import telnetlib3
import asyncio

async def main():
    reader, writer = await telnetlib3.open_connection('localhost', 23)

    writer.write("echo 'Hello Telnet'\n")

    reply = await reader.read(1024)
    print('Server reply:', reply)

    writer.close()

asyncio.run(main())    