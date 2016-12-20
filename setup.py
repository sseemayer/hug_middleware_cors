from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hug_middleware_cors',
    version='1.0.0',

    description='CORS middleware for the hug framework',
    long_description=long_description,

    url='https://github.com/sseemayer/hug_middleware_cors',

    author='Stefan Seemayer',
    author_email='stefan@seemayer.de',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='hug cors middleware access-control-allow-origin',

    py_modules=["hug_middleware_cors"],

    install_requires=['hug'],

)
