from setuptools import find_packages, setup

def get_requirements(file_path: str):
    with open(file_path) as file_obj:
        requirements = [line.strip() for line in file_obj if not line.startswith("-e")]
    return requirements

setup(
    name='ML_Project',
    version='1.0.0',
    author='Adithya Kobbai',
    author_email='adityakobbai@gmail.com',
    description='An End to End Data Science Project using CI/CD Pipelines',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
