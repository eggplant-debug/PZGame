import asyncio
import json
import pickle
from share.const import *

from const import *

class AsyncClient(object):
    def __init__(self, game,ip, port):
        self.game =game
        self.ip = ip
        self.port = port
    
    async def c2s(self, message):
        reader, writer = await asyncio.open_connection(self.ip, self.port)
        data = json.dumps(message).encode()

        writer.write(data)
        # 等待缓冲区写完
        await writer.drain()

        message = await reader.read(MAX_BYTES)
        msg=json.loads(message.decode())
        print(msg)
        if msg['type'] == S2C_ADD_FLOWER:
            self.game.checkAddPlant(msg['pos'],SUNFLOWER_ID)