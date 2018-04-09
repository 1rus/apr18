from setuptools import setup

config = {
    'description': 'Basic framework template for selenium UI tests',
    'author': "Ruslan Rizvanov",
    'url': '#####.com',
    'download_url': 'github.com',
    'author_email': 'rus4ca@gmail.com',
    'version': '0.1',
    'packages': ['framework'],
    'scripts': [],
    'name': 'framework template'
}

setup(**config,
    setup_requires = ['pytest-runner'],
    tests_require  = ['pytest']
)
