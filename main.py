from aiohttp import web
import json
from core.server.gradient import create


async def handle(request):
    response_obj = {"status": "success"}
    return web.Response(text=json.dumps(response_obj))


app = web.Application()
app.router.add_routes([web.get("/", handle), web.post("/gradient", create)])

web.run_app(app, host="localhost", port=8080)
