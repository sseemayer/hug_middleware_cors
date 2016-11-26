import hug
from hug_middleware_cors import CORSMiddleware

api = hug.API(__name__)
api.http.add_middleware(CORSMiddleware(api))


@hug.post('/demo')
def demo(name: 'your name'):
    return {"result": "Hello {0}".format(name)}
