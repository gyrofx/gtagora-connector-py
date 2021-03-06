from gtagora.exception import AgoraException
from gtagora.models.base import LinkToFolderMixin, BaseModel, DownloadDatasetMixin
from gtagora.models.dataset import Dataset


class Series(LinkToFolderMixin, DownloadDatasetMixin, BaseModel):
    BASE_URL = '/api/v1/serie/'

    def __init__(self, http_client):
        # if 'acquisition_number' not in model_dict:
        #     raise AgoraException('Could not initialize the Series: acquisition_number is missing')

        super().__init__(http_client)

    def get_datasets(self, filters=None):
        if filters and not isinstance(filters, dict):
            raise AgoraException('The filter must be a dict')

        url = f'{self.BASE_URL}{self.id}/datasets/?limit=10000000000'
        return self._get_object_list(url, filters, Dataset)

    def upload(self, input_files, target_files=None):
        if target_files and len(input_files) != len(target_files):
            raise AgoraException("The Inputfiles and TargetFiles must have the same length")

        if isinstance(input_files, str):
            files = [input_files]
        else:
            files = input_files

        datasets = []
        for index, curFile in enumerate(files):
            cur_target_file = None
            if target_files:
                cur_target_file = target_files[index]
            datasets.append(Dataset.upload_files(self.http_client, curFile, cur_target_file, series_id=self.id))
        return datasets

    def upload_dataset(self, input_files, dataset_type, target_files=None):
        # This function creates a dataset of a given type all files given as input will be added to one dataset.
        # Please note: At the moment there is no consistency check. We could create datasets with improper
        # files (e.g. a PAR/REC dataset without PAR/REC files)
        return self.http_client.upload_dataset(input_files, target_files, serie_id=self.id, dataset_type=dataset_type)

    def __str__(self):
        return f"Series: {self.name}"
