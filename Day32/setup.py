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

#How to build distributions
'''
run these commands in the terminal

python setup.py sdist bdist_wheel
[
sdist = source distribution
bdist_wheel = wheel distribution
]

-Upload your distributions to PyPI

    twine upload dist/*

-Upload your distributions to TestPyPI

    twine upload -r testpypi dist/*

-To install package from PyPI

    pip install mysklearn

'''

#Writing Tests
def get_ends(x):
    """Get the first and last element in a list"""
    return x[0], x[-1]
def test_get_ends(x):
    assert get_ends([1,5,9,4,0]) == (1,0)

test_get_ends()