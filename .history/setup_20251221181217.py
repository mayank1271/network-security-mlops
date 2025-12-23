from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """This function will return the list of requirements""" 
    with open(requirements.txt,"r") as file:
        ##read line from file
        lines= file.readlines()
        ##process each line
        for line in lines:
            requirement=line.strip()
            ##ignore empty line and -e .
            if requirement and requirement!="-e .":
                requirement_lst.append(requirement)

         