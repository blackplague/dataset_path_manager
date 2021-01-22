from setuptools import setup, find_packages

setup(
    name='DatasetPathManager',
    version='0.0.1',
    description='Small class to handle a image dataset',
    author='Michael Andersen',
    author_email='gosuckadeadcow+github@gmail.com',
    url='https://github.com/blackplague/dataset_path_manager',
    packages=find_packages(include=['datasetpathmanager', 'datasetpathmanager.*'])
)