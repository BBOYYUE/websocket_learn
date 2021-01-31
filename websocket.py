import asyncio
import websockets
import json
import time


async def run(message):
    async with websockets.connect('ws://39.100.229.171:8082',ping_timeout = 60) as websocket:
        await websocket.send(message[0])
        await asyncio.gather(
            listen(websocket),
            heart(websocket,message[1])
        )

async def listen(websocket):
    while True:
        data = await websocket.recv()
        print(data)

async def heart(websocket,message):
    while True:        
        await websocket.send(message)
        await asyncio.sleep(30)


class Test:    
    def getData(self):
        data = {
            "method":self.method,
            "equipment_number":self.equipment_number,
            "message":self.message
        }

        heart = {
            "method":"send",
            "equipment_number":self.equipment_number,
            "message":{
                "message":"test",
                "tapType":113
            }
        }

        return [json.dumps(data),json.dumps(heart)]

        
class debug(Test):
    def __init__(self):
        self.method = "listen"
        self.equipment_number = 999
        self.tapType = 0
        self.message = ""


        


debug = debug()
loop = asyncio.get_event_loop()
data = debug.getData()

"""单个测试"""
loop.run_until_complete(run(data))

"""同时运行多个测试"""
# task = []
# for i in [value for value in range(0,1000)]:
#     task.append(run(data))
# loop.run_until_complete(asyncio.wait(task))

loop.close()