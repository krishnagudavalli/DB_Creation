from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='postgres_db_creation',
    version='0.1.0',
    description='cloudFormation template, validating and creating a cloudFormation stack.',
    long_description=readme,
    author='Quadyster_dev_team',
    author_email='mmunnalluri'@quadyster.com',
    url='https://github.com/mmunnaluri/DB_Creation.git',
    packages=find_packages(exclude=('tests', 'docs'))
)
