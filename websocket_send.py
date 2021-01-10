import asyncio
import websockets
import json
import time

async def run(message):
    async with websockets.connect('ws://39.100.229.171:8082') as websocket:
        while True:
            time.sleep(10)
            await websocket.send(message)     



class Test:    
    def getData(self):
        data = {
            "method":self.method,
            "equipment_number":self.equipment_number,
            "message":self.message
        }

        return json.dumps(data)
        
class debug(Test):
    def __init__(self):
        self.method = "send"
        self.equipment_number = 999
        self.tapType = 0
        self.message = {
            "message":"test",
            "tapType":self.tapType
        }


        


debug = debug()

loop = asyncio.get_event_loop()

"""单个测试"""
loop.run_until_complete(run(debug.getData()))

"""同时运行多个测试"""
# task = [run(TestListenOne.getData()),run(TestListenTwo.getData())]
# loop.run_until_complete(asyncio.wait(task))


loop.close()