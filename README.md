# hug CORS middleware

A [hug](https://github.com/timothycrosley/hug) middleware for allowing CORS (cross-origin resource sharing) requests from hug servers.

## Installation

```bash
pip install hug_middleware_cors
```

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

## Demoing

  1. Check out this repository and navigate to its root
  2. Start a hug server on port 8000 using: `hug -f server.py`
  3. Start a static http server on port 8080 using `python -m http.server 8080`
  4. Go to [http://localhost:8080](http://localhost:8080) to send a preflighted CORS request to the hug server.

## License
MIT License

See LICENSE for details
