from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name = "systeminfo",
    version = "v1.0",
    url= "https://github.com/MichaelMoyles/systeminfo",
    author= "Michael Moyles"
)