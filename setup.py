from setuptools import setup

setup(
    name='cmirror',
    version='0.0.1',
    packages=['package'],
    url='',
    license='',
    author='v',
    author_email='',
    description='alias like feature for windows based on python',
    entry_points={
        'console_scripts': ['mirror=package:mirror'],
    }
)
