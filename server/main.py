import asyncio
import const

async def handle_client(reader, writer):
    data=await reader.read(const.MAX_BYTES)
    print(data)

async def main():
    # 创建服务器
    server = await asyncio.start_server(
        handle_client, const.HOST, const.LISTEN_PORT
    )
    print(f"Server listening on {const.HOST}:{const.LISTEN_PORT}")

    # 让服务器一直运行
    async with server:
        await server.serve_forever()


asyncio.run(main())