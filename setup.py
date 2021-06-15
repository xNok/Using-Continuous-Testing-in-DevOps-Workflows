from setuptools import setup

setup(
    name='phonebook',
    packages=['phonebook'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)