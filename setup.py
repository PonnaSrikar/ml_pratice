#this setup.py is responsible for making this applicaion mlproject as package
from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[rec.replace("\n","") for rec in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements



setup(

    name='mlproject',
    version='0.0.1',
    author='srikar',
    author_email='srikarponna123@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")#['pandas','numpy','seaborn']

)