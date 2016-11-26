# hug CORS middleware

A [hug](https://github.com/timothycrosley/hug) middleware for allowing CORS (cross-origin resource sharing) requests from hug servers.

## Usage

```python
import hug
from hug_middleware_cors import CORSMiddleware

api = hug.API(__name__)
api.http.add_middleware(CORSMiddleware(api))

@hug.post('/demo')
def demo(name: 'your name'):
    return {"result": "Hello {0}".format(name)}
```

## Installation
TODO: create a nice way of installing this.

## License
MIT License

See LICENSE for details
