import asyncio
import json
import pickle


from const import *

class AsyncClient(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
    
    async def c2s(self, message):
        reader, writer = await asyncio.open_connection(self.ip, self.port)
        data = json.dumps(message).encode()

        writer.write(data)
        # 等待缓冲区写完
        await writer.drain()