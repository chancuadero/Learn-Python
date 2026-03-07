This is Day 32 of learning Python

Topic: Installing your own package
Summary: To install your own package, you used setup.py that contains metadata on the package. Once completing the setup script, you can install the package by going to the directory containing the setup file and then use pip install -e .
(-e(means editable) .(means package in current directory))

Topic: Adding dependencies to setup.py
Summary: You may add install*requires=['pandas','scipy','matplotlib'] and/or python_requires = '>=2.7, !=3.0.*, !=3.1.\*' inside the setup function
