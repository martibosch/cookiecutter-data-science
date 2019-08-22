from setuptools import find_packages, setup

setup(
    name='{{ cookiecutter.repo_name }}',
    packages=['{{ cookiecutter.project_name }}'],
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    license='GPL-3.0',
)
