# Run's the requirements.txt file 
# Find's all packages from MACHINE_LEARNING_MLOPS_PROJECT (FOLDER)

from setuptools import setup, find_packages

with open("requirements.txt") as file:
    requirements = file.read().splitlines()

setup(
    name="CC_MLOPS_PROJECT_1",
    version="0.0.1",
    author="Abhishek",
    packages= find_packages(),
    install_requires=requirements,
)