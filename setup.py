from setuptools import setup, find_packages

setup(
    name='microalerts',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['requests>=2.25.1'],
    author='Adarsh Malviya',
    description='Microservice notification library for sending alerts to Slack and other platforms.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)