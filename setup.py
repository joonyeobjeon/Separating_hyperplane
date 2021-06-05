from setuptools import setup, find_packages

# Get version number
about = {}
with open('opt_hyperplane/version.py') as f:
    exec(f.read(), about)
version = about['__version__']


setup(
    name="opt_hyperplane",
    setup_requires=['matplotlib', 'numpy', 'json'],
)