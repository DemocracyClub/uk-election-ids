import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

def _get_description():
    try:
        path = os.path.join(os.path.dirname(__file__), 'README.md')
        with open(path, encoding='utf-8') as f:
            return f.read()
    except IOError:
        return ''

setup(
    name='uk_election_ids',
    version='0.1.2',
    author="chris48s",
    license="MIT",
    url="https://github.com/DemocracyClub/uk-election-ids/",
    packages=['uk_election_ids'],
    description='Create Democracy Club Election Identifiers',
    long_description=_get_description(),
    long_description_content_type="text/markdown",
    extras_require={
        'testing': [
            'python-coveralls',
        ],
        'development': [
            'sphinx',
            'sphinx_rtd_theme',
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
