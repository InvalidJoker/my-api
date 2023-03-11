from aiohttp import web
import json
from core.server.create import create

async def handle(request):
    response_obj = {'status': 'success'}
    return web.Response(text=json.dumps(response_obj))

app = web.Application()
app.router.add_routes([
    web.get('/', handle),
    web.post('/create', create)
])

web.run_app(app, host='localhost', port=8080)