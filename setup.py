#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

setup_requirements = []

test_requirements = ["tox", "flake8", "coverage", "black", "mypy", "isort",]

doc_requirements = ["Sphinx>1.8"]

dev_requirements = ["bump2version", "twine"]

setup(
    author="Spencer Bliven",
    author_email='spencer.bliven@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="Convert pixel art to gem painting templates",
    entry_points={
        'console_scripts': [
            'gem_painting=gem_painting.cli:main',
        ],
    },
    install_requires=requirements,
    extras_require={
        "tests": test_requirements,
        "docs": doc_requirements,
        "dev": dev_requirements + test_requirements + doc_requirements,
    },
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='gem_painting',
    name='gem_painting',
    packages=find_packages(include=['gem_painting', 'gem_painting.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/sbliven/gem_painting',
    version='0.1.0',
    zip_safe=False,
)
