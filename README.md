# Dataset Path Manager

## Installation

The Dataset Path Manager can be installed directly from git using

```sh
#> python -m pip install git+https://github.com/blackplague/dataset_path_manager.git
```

## Usage

And can then be used in a program as follows

demo.py:

```python
from datasetpathmanager import DatasetPathManager

dpm = DatasetPathManager(dataset_target='cat_vs_dog', dataset_base_path='/home/user/datasets')

print(f'Dataset path: {dpm.dataset_path}')

training_path, validation_path, test_path = dpm.get_paths()

print(f'Training data path: {training_path}')
print(f'Validation data path: {validation_path}')
print(f'Test data path: {test_path}')
```

If ***dataset_base_path*** left to be **None** DatasetPathManager will read the environment
variable called **DATASET_BASE_PATH** from the system and use that instead. It also allows
for overwriting the "standard" location of training, validation and test directories.

Overwriting standard locations:

```python
dpm = DatasetPathManager(
    dataset_target='cat_vs_dog',
    train_dir='my_training_dir',
    validation_dir='my_validation_dir',
    test_dir='my_test_dir')
```

## Todo's

Split into multiple path managers, e.g:

* ImageDatasetPathManager
* CSVDatasetPathManager(?)
