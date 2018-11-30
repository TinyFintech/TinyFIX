try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Tiny FIX API',
    'author': 'Tiny',
    'url': 'https://github.com/TinyFintech/TinyFIX',
    'download_url': 'https://github.com/TinyFintech/TinyFIX',
    'author_email': 'tinywork2018@gmail.com.',
    'version': '0.1',
    'install_requires': [''],
    'packages': ['tinyfix', 'tinyfix/FIX44'],
    'scripts': [],
    'name': 'tinyfix'
}

setup(**config)