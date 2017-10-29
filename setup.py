try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Ex47',
    'author': 'Conrad Thiele',
    'url': 'Url to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'tcratius@gmail.com',
    'version': '0.1',
    'install_requires': ['nose', 'pytest'],
    'packages': ['ex47', 'tests'],
    'scripts': [],
    'name': 'Ex47'

}

setup(**config)
