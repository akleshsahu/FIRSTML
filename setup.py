from setuptools import setup, find_packages
from typing import List 
this='-e .'
requirements = []
def get_requirements(file_path: str) -> list:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    if this in requirements:
        requirements.remove(this)
    return requirements



setup(
    name='ete_project',
    version='0.1',
    packages=find_packages(),
    author='Aklesh Sahu',
    description='A project for ETE course',
    author_email='aklesh.sahu@example.com',
    install_requires=get_requirements('req.txt')
)