

import os
from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()
with open('requirements.txt', 'r') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
    name='environment-setup',
    version='0.0.1',
    description='Easy environment setup',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Kashish Srivastava',
    author_email='kashish.srivastava014@gmail.com',
    url='http://github.com/cannibalcheeseburger/environment-setup',

    packages=find_packages(), # provides same list, looks for __init__.py file in dir
    include_package_data=True,
    install_requires=requirements, #external packages as dependencies

    entry_points={
        'console_scripts': ['envpy=environment_setup.
        :main']
    },

    classifiers=[
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    license='MIT License',
)

