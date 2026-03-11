This is Day 32 of learning Python

Topic: Installing your own package
Summary: To install your own package, you used setup.py that contains metadata on the package. Once completing the setup script, you can install the package by going to the directory containing the setup file and then use pip install -e .
(-e(means editable) .(means package in current directory))

Topic: Adding dependencies to setup.py
Summary: You may add install*requires=['pandas','scipy','matplotlib'] and/or python_requires = '>=2.7, !=3.0.*, !=3.1.\*' inside the setup function

Topic: License and writing READMEs.
Summary: License is used to give permission to use your code. Open source licenses allow users to use, modify, and distribute versions of your package. README is the "front page" of your package, a good README has title, description and features, installation, usage examples, contribution, and license. MANIFEST.in file lists all the extra files to include in your package distribution.

Topic: Distributions
Summary: Distribution package - a bundled version of your package which is ready to install. Source distribution - a distribution package which is mostly your source code. Wheel distribution - a distribution package which has been processed to make it faster to install.

Topic: Testing package
Summary: Writing test will help you track on bugs and signals to users that your package can be trusted to perform as intended. Each function in your package should have a test function.
