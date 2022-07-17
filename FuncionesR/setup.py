from setuptools import setup
readme = open("./README.md", "r")
setup(
    name = 'funcionesR',
    version='1.0',
    long_description=readme.read(),
    license='MIT'
)