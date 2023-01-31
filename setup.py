from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name = "systeminfo",
    version = "v1.0",
    packages=find_packages(include=['systeminfo', 'systeminfo.*']),
    url= "https://github.com/MichaelMoyles/systeminfo",
    author= "Michael Moyles"
)