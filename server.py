import hug
from hug_middleware_cors import CORSMiddleware

api = hug.API(__name__)
api.http.add_middleware(CORSMiddleware(api))

@hug.get('/demo')
def get_demo():
    return {'result': 'Hello World'}

@hug.get('/demo/{param}')
def get_demo(param):
    return {'result': 'Hello {0}'.format(param)}

@hug.post('/demo')
def post_demo(name: 'your name'):
    return {'result': 'Hello {0}'.format(name)}

@hug.put('/demo/{param}')
def get_demo(param, name):
    old_name = param
    new_name = name
    return {'result': 'Goodbye {0} ... Hello {1}'.format(old_name, new_name)}

@hug.delete('/demo/{param}')
def get_demo(param):
    return {'result': 'Goodbye {0}'.format(param)}
