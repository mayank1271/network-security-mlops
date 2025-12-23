"""
the setup.py is an essential part of packaging and
distributing python projects. it is used by setuptools
(for distuils in older py versions) to define the configuration
of your projet, such as its metadata, dependencies, and more.

"""

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    requirement_lst:list[str]=[]
    """This function will return the list of requirements""" 
    try:
        with open(r"requirements.txt","r") as file:
            ##read line from file
            lines= file.readlines()
            ##process each line
            for line in lines:
               requirement=line.strip()
               ##ignore empty line and -e .
               if requirement and requirement!="-e .":
                   requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_lst

print(get_requirements())

         