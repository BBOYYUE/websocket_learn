import asyncio

async def listen():
	while True:
		await hello()

async def hello():
	print(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(listen())
loop.close()