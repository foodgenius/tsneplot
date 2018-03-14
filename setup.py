import os.path as P
from setuptools import setup

with open(P.join(P.dirname(__file__), 'requirements.txt')) as f:
    requires = f.read().splitlines()

setup(
    name='tsneplot',
    install_requires=requires,
    version='0.0.1',
    packages=['tsneplot'],
    scripts=['scripts/tsneplot']
)

