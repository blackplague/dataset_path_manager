from datasetpathmanager import DatasetPathManager
import pytest
import os

@pytest.fixture
def dpm_instance():
    return DatasetPathManager(
        dataset_target='cat_vs_dog',
        dataset_base_path='/home/user/datasets',
        train_dir='my_training_dir',
        validation_dir='my_validation_dir',
        test_dir='my_test_dir')

def test_dataset_base_path(dpm_instance):
    assert dpm_instance.dataset_base_path == '/home/user/datasets'

def test_dataset_target(dpm_instance):
    assert dpm_instance.dataset_target == 'cat_vs_dog'

def test_dataset_base_path_and_target(dpm_instance):
    assert dpm_instance.dataset_path == os.path.join('/home/user/datasets', 'cat_vs_dog')

def test_dataset_training_path(dpm_instance):
    assert dpm_instance.training_path == os.path.join(
        '/home/user/datasets',
        'cat_vs_dog',
        'my_training_dir')

def test_dataset_validation_path(dpm_instance):
    assert dpm_instance.validation_path == os.path.join(
        '/home/user/datasets',
        'cat_vs_dog',
        'my_validation_dir')

def test_dataset_test_path(dpm_instance):
    assert dpm_instance.test_path == os.path.join(
        '/home/user/datasets',
        'cat_vs_dog',
        'my_test_dir')
