from aiohttp import web
from core.tools.gradient_maker import create_gradient
from core.tools.validator import validate_code, validate_numbers


async def create(request: web.Request) -> web.Response:
    if not request.can_read_body:
        return web.Response(body="Invalid request", status=400)

    json: dict = await request.json()
    if "colors" not in json or "width" not in json or "height" not in json:
        return web.Response(body="Invalid request", status=400)

    for code in json["colors"]:
        if not validate_code(code):
            return web.Response(body="Invalid request", status=400)

    if not validate_numbers(json["width"], json["height"]):
        return web.Response(body="Invalid request", status=400)

    result = create_gradient(json["colors"], width=json["width"], height=json["height"])

    return web.Response(body=result)
