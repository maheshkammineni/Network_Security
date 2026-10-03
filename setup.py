
from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    """
    Read dependencies from requirements.txt.
    """
    requirement_lst: List[str] = []

    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()

                # Ignore empty lines and editable-install directives
                if requirement and requirement != "-e." and requirement != "-e .":
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("REQUIREMENTS.TXT FILE WAS NOT FOUND")

    return requirement_lst


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Mahesh",
    packages=find_packages(),
    install_requires=get_requirements(),
)