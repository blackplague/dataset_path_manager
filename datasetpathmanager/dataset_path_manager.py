from typing import Optional, Tuple
import os

class DatasetPathManager:

    def __init__(
        self,
        dataset_target: str,
        dataset_base_path: Optional[str]=None,
        train_dir: str='train',
        validation_dir: str='validation',
        test_dir: str='test'):

        self._dataset_target = dataset_target
        if dataset_base_path is None:
            self._dataset_base_path = os.environ['DATASET_BASE_PATH']
        else:
            self._dataset_base_path = dataset_base_path
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
        return self.dataset_base_path

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

"""
        Parameters
        ----------
        search_string : str
            Search string to search CVR for
        top_n : int
            The top number of results to return based on ElasticSearch _score
        only_active : bool
            The query should now only return companies that have sammensatStatus as
            'NORMAL' or 'Active'.
        search_params : Dict
            Specifies search_parameters for the underlying elastic search client, the
                default being:
                    search_params={
                        'method': 'query_string',
                        'proximity_search': True,
                        'maximum_edit_distance': 5
                    }
        format : str
            Specifies the format of the data, currently supporting: 'dict',
                'json' and 'dataframe'


        Raises
        ------
        UnknownSearchMethodException
            If called with an invalid search method in the search_params
        UnknownFormatException
            If called with an invalid format string


"""