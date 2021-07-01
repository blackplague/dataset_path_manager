from itertools import combinations
from typing import List, Optional, Tuple
import os


class UnknownDatasetBasePath(Exception):
    pass


class DatasetPathManager:

    def __init__(
        self,
        dataset_target: str,
        dataset_base_path: Optional[str]=None,
        train_dir: str='train',
        validation_dir: str='validation',
        test_dir: str='test'
    ):

        self._dataset_target = dataset_target
        if dataset_base_path is not None:
            self._dataset_base_path = dataset_base_path
        elif os.environ.get('DATASET_BASE_PATH') is not None:
            self._dataset_base_path = os.environ['DATASET_BASE_PATH']
        else:
            raise UnknownDatasetBasePath(
                'No Dataset base path was provided, neither as argument or found in $DATASET_BASE_PATH')

        self._dataset_path = os.path.join(self._dataset_base_path, self._dataset_target)
        self._training_data_path = os.path.join(self._dataset_path, train_dir)
        self._validation_data_path = os.path.join(self._dataset_path, validation_dir)
        self._test_data_path = os.path.join(self.dataset_path, test_dir)

    def get_paths(self) -> Tuple[str, str, str]:
        """Return paths to training_data, validation_data and test_data in that order

        Example
        -------
        If you have a cats vs dogs dataset located at "/home/user/datasets/cats_vs_dogs" this will
        return:
           (
               '/home/user/datasets/cats_vs_dogs/train',
               '/home/user/datasets/cats_vs_dogs/validation',
               '/home/user/datasets/cats_vs_dogs/test'
           )
        in that specific order.

        Returns
        -------
        Tuple[str, str, str]
            Where t[0] is training_data_path, t[1] is validation_data_path and
            t[2] is test_data_path
        """
        return (self._training_data_path, self._validation_data_path, self._test_data_path)

    @property
    def dataset_target(self) -> str:
        """Returns the dataset target

        Example
        -------
        If you have a cats vs dogs dataset located at "/home/user/datasets/cats_vs_dogs" this will
        return just cats_vs_dogs

        Returns
        -------
        str
            The dataset target, see Example
        """
        return self._dataset_target

    @property
    def dataset_base_path(self) -> str:
        """Returns the dataset base path

        Example
        -------
        If you have a dataset located at "/home/user/datasets/dataset1" this will
        return "/home/user/datasets"

        Returns
        -------
        str
            The dataset base path, see Example
        """
        return self._dataset_base_path

    @property
    def dataset_path(self) -> str:
        """Returns the dataset path

        Example
        -------
        If you have a dataset located at "/home/user/datasets/dataset1" this will
        return "/home/user/datasets/dataset1"

        Returns
        -------
        str
            The dataset path, see Example
        """
        return self._dataset_path

    @property
    def training_path(self) -> str:
        """Returns the training dataset path

        Example
        -------
        If you have a dataset located at "/home/user/datasets/dataset1" this will
        return "/home/user/datasets/dataset1/train"

        Returns
        -------
        str
            The training dataset path, see Example
        """
        return self._training_data_path

    @property
    def validation_path(self) -> str:
        """Returns the validation dataset path

        Example
        -------
        If you have a dataset located at "/home/user/datasets/dataset1" this will
        return "/home/user/datasets/dataset1/validation"

        Returns
        -------
        str
            The validation dataset path, see Example
        """
        return self._validation_data_path

    @property
    def test_path(self) -> str:
        """Returns the test dataset path

        Example
        -------
        If you have a dataset located at "/home/user/datasets/dataset1" this will
        return "/home/user/datasets/dataset1/test"

        Returns
        -------
        str
            The test dataset path, see Example
        """
        return self._test_data_path

    @property
    def class_test_path(self) -> Optional[List[str]]:
        """Return the full path to every class found in the test directory

        Example
        -------
        If you have the following classes located at
        "/home/user/datasets/dataset1/test/{class1, class2}"
        This will return:
        ["/home/user/datasets/dataset1/test/class1",
         "/home/user/datasets/dataset1/test/class2"]

        Returns
        -------
        Optional[List[str]]
            If no inconsistencies where found, returns a list of paths to the test classes in
            sorted order in sorted order, otherwise None will be returned
        """
        classes = self.get_classes()
        if classes is None:
            return None
        return [os.path.join(self.test_path, c) for c in classes]

    def get_classes(self) -> List[str]:
        """Tries to infer the classes based on subfolders in test, train and validation directories

        It will ignore all files present in the directories test, train and validation directories,
        only considering subfolders.

        Example
        -------
        If you have a dataset located at "/home/user/datasets/dataset1" it will look for
        subdirectories in the follow places:
        /home/user/datasets/dataset1/{test,train,validation}

        Hence, if there are the follow classes:
        /home/user/datasets/dataset1/{test,train,validation}/{class1, class2}

        This will return ['class1', 'class2']

        Returns
        -------
        List[str]
            If no inconsistencies where found, returns a list of classes in sorted order, otherwise
            [] will be returned
        """
        potential_classes = []
        for p in self.get_paths():
            cs = [c for c in os.listdir(p) if os.path.isdir(os.path.join(p, c))]
            potential_classes.append((p, cs))

        inconsistent_classes = False
        for t1, t2 in combinations(potential_classes, 2):
            if not self._compare(t1[1], t2[1]):
                inconsistent_classes = True

        if inconsistent_classes:
            print('Class inconsistencies found:')
            for p, c in potential_classes:
                print(f'\tPath={p}, Classes={c}')
            return []
        return sorted(potential_classes[0][1])

    @staticmethod
    def _compare(l1: List[str], l2: List[str]) -> bool:
        for a, b in zip(sorted(l1), sorted(l2)):
            if a != b:
                return False
        return True
