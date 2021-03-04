import re

import setuptools
from setuptools import setup

with open("requirements.txt", encoding="utf-8") as r:
    requires = [i.strip() for i in r]

with open("fnapi_io/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name='fnapi_io',
    author='MyNameIsDark01',
    version=version,
    packages=setuptools.find_packages(),
    license='MIT',
    description='A python wrapper for fortniteapi.io',
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=requires,
    python_requires='>=3.5.3'
)
