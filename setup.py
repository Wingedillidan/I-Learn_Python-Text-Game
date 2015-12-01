try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A basic first game attempt.',
    'author': 'Collin McLean',
    'url': 'http://github.com/wingedillidan/game',
    'author_email': 'wingedillidan@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['game'],
    'scripts': [],
    'name': 'game'
}

setup(**config)
