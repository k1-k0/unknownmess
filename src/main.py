from models import objects, Message

from aiohttp import web


async def get_messages(request):
    messages = await app.objects.execute(Message.select())
    messages = {m.id: (m.title, m.text) for m in messages}
    return web.json_response({'messages': messages})


async def set_message(request):
    data = await request.json()
    await app.objects.create(Message, **data)
    return web.Response()


app = web.Application()
app.objects = objects
app.add_routes([web.get('/messages', get_messages)])
app.add_routes([web.post('/messages', set_message)])
web.run_app(app)
