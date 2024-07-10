import asyncio
import os
import sys
import json
current_path = os.path.dirname(os.path.realpath(__file__))
print(current_path)

top_path = os.path.dirname(current_path)
sys.path.append(top_path)
from share.const import *


async def handle_client(reader, writer):
    data=await reader.read(MAX_BYTES)
    data=data.decode()
    msg=json.loads(data)
    print(msg)

    s2cmsg ={

    }

    if msg['type'] == C2S_ADD_FLOWER:
        s2cmsg['type'] = S2C_ADD_FLOWER
        s2cmsg['pos'] = msg['pos']
    
    writer.write(json.dumps(s2cmsg).encode())
    await writer.drain()


async def main():
    # 创建服务器
    server = await asyncio.start_server(
        handle_client, HOST, LISTEN_PORT
    )
    print(f"Server listening on {HOST}:{LISTEN_PORT}")

    # 让服务器一直运行
    async with server:
        await server.serve_forever()


asyncio.run(main())