from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import datetime
import os

def hello_world(request):
    name = os.environ.get('NAME')
    current_time = datetime.datetime.now()
    if name == None or len(name) == 0:
        name = "world"
    if name == "Gareth":
        name = "King " + name
    if current_time.hour < 12:
        message = "Good morning, "
    elif current_time.hour < 14:
        message = "Good afternoon, "
    else:
        message = "Good evening, "
    message = message + name + "!\n"
    return Response(message)

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
