from setuptools import find_packages, setup
from typing import List

HYPHOM_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHOM_E_DOT in requirements:
            requirements.remove(HYPHOM_E_DOT)
    return requirements

setup(
    name='AI-Assistent',
    version='0.0.0',
    author='project_phase8',
    author_email='@iiitu.ac.in',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")

)