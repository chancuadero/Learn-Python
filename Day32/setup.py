from setuptools import setup, find_packages

setup(
    author = "James Fulton",
    description = "A complete package for linear regression.",
    name = "mysklearn",
    version = "0.1.0",
    packages = find_packages(include = ["mysklearn","mysklearn.*"]),
    install_requires=['pandas','scipy','matplotlib'],
    python_requires = '>=2.7, !=3.0.*, !=3.1.*'
)