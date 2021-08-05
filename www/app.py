import logging
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

logging.basicConfig(level=logging.INFO)


async def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


async def init(loop):
    app = web.Application()
    app_runner = web.AppRunner(app)
    app.router.add_route('GET', '/', index)
    await app_runner.setup()
    server = await loop.create_server(app_runner.server, '127.0.0.1', 8000)
    logging.info('Server started at http://127.0.0.1:8000/...')
    return server


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
