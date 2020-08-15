from setuptools import setup
setup(
    name = 'sedpy',
    version = '0.1.0',
    packages = ['sedpy'],
    entry_points = {
        'console_scripts': [
            'sedpy = sedpy.__main__:main'
        ]
    })