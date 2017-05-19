import unittest
import requests
import json

URL = 'http://localhost:8000'

class GetTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_nonparam(self):
        resp = requests.get('{0}/demo'.format(URL))
        data = json.loads(resp.content.decode())
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data, {'result': 'Hello World'})

    def test_param(self):
        resp = requests.get('{0}/demo/Mir'.format(URL))
        data = json.loads(resp.content.decode())
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data, {'result': 'Hello Mir'})

class PostTest(unittest.TestCase):

    def test_post(self):
        resp = requests.post(
                '{0}/demo'.format(URL),
                json={'name': 'Mundo'}
                )
        data = json.loads(resp.content.decode())
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data, {'result': 'Hello Mundo'})

class PutTest(unittest.TestCase):

    def test_put(self):
        resp = requests.put(
                '{0}/demo/Carl'.format(URL),
                json={'name': 'Junior'}
                )
        data = json.loads(resp.content.decode())
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data, {'result': 'Goodbye Carl ... Hello Junior'})

class DeleteTest(unittest.TestCase):

    def test_param(self):
        resp = requests.delete('{0}/demo/Cruel_World'.format(URL))
        data = json.loads(resp.content.decode())
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data, {'result': 'Goodbye Cruel_World'})

class OptionsTest(unittest.TestCase):

    def test_nonparam(self):
        resp = requests.options('{0}/demo'.format(URL))
        methods = resp.headers['access-control-allow-methods'].replace(' ', '')
        self.assertEqual(resp.status_code, 204)
        allow = resp.headers['allow'].replace(' ', '')
        self.assertSetEqual(
                set(methods.split(',')),
                set(['OPTIONS', 'GET', 'POST'])
                )
        self.assertSetEqual(
                set(allow.split(',')),
                set(['OPTIONS', 'GET', 'POST'])
                )

    def test_param(self):
        resp = requests.options('{0}/demo/1'.format(URL))
        methods = resp.headers['access-control-allow-methods'].replace(' ', '')
        allow = resp.headers['allow'].replace(' ', '')
        self.assertEqual(resp.status_code, 204)
        self.assertSetEqual(
                set(methods.split(',')),
                set(['OPTIONS', 'GET', 'DELETE', 'PUT'])
                )
        self.assertSetEqual(
                set(allow.split(',')),
                set(['OPTIONS', 'GET', 'DELETE', 'PUT'])
                )
