from gtAgoraPythonInterface import gtAgora
from gtAgoraPythonInterface import DatasetType
from gtAgoraPythonInterface import AgoraException
from gtAgoraPythonInterface import gtAgoraRequest
import tempfile
import os.path

class TestAgoraInterface:
    #server = 'https://gauss4.ethz.ch'
    #user = 'martin'
    #password = 'martin'
    #api_key = '259eaddc-3515-4593-994e-2da16aab832c'

    server = 'http://127.0.0.1:8000'
    api_key = '0853ac53-7aca-4e26-afc6-2a58c8cf953e'
    gtAgora.mVerifyCertificate = False

    def test_ping_server(self):
        try:
            IsConnection, ErrorMessage = gtAgoraRequest.Ping(TestAgoraInterface.server)
            if not IsConnection:
                raise AgoraException('Could not connect to Agora: ' + ErrorMessage)

        except:
            assert False

    def test_connection_api_key(self):
        try:
            A = gtAgora(TestAgoraInterface.server, api_key=TestAgoraInterface.api_key)
        except:
            assert False

    def test_upload(self):
        A = gtAgora(TestAgoraInterface.server, api_key=TestAgoraInterface.api_key)
        item = A.get_folder(54)
        item.Upload(['C:\\Users\\martin\\Desktop\\temp\\Daten\\Constantin_DTI_Heart\\ha_03112017_203206_1000_11_wipsenserefscan.gve',
                       'C:\\Users\\martin\\Desktop\\temp\\Daten\\Constantin_DTI_Heart\\ha_03112017_1847552_2_2_wip_refV4.gve'])
        item.upload_dataset(
            ['C:\\Users\\martin\\Desktop\\temp\\Daten\\Constantin_DTI_Heart\\ha_03112017_1850551_3_1_wip_b-tfe_bh_vlaV4.rec',
             'C:\\Users\\martin\\Desktop\\temp\\Daten\\Constantin_DTI_Heart\\ha_03112017_1850551_3_1_wip_b-tfe_bh_vlaV4.par'], DatasetType.PHILIPS_REC)
        a = 1

    def test_folders_api_key(self):
        try:
            A = gtAgora(TestAgoraInterface.server, api_key=TestAgoraInterface.api_key)

            # Get the root folder
            RootFolder = A.get_root_folder()
            # Get a folder by ID
            Folder = A.get_folder(RootFolder.id)
            # Get all subfolders of the root folder
            Subfolders = RootFolder.get_folders()
            # Get all items in the first subfolder
            Items = Subfolders[0].GetItems()
            # Get all Exams in the first subfolder
            Exams = Subfolders[0].get_exams()
            # Recursively get all Exams in the current folder and all subfolders
            Exams = Subfolders[0].get_exams(True)
            # Get all series in the first subfolder
            Series = Subfolders[0].get_series()
            # Recursively get all series in the current folder all subfolders
            Series = Subfolders[0].get_series(True)
            # Get all datasets in the first subfolder
            Datasets = Subfolders[0].get_datasets()
            # Recursively get all datasets in the current folder all subfolders
            Datasets = Subfolders[0].get_datasets(True)
            # Create a new folder in the root folder (the new folder object is returned)
            NewFolder = RootFolder.NewFolder('TestFolder')
            # Check if the new folder exists
            Folder = A.get_folder(NewFolder.id)
            if(not Folder):
                raise("Folder does not exist")
            # Link the first Exam to the newly created folder
            Exams[0].link_to_folder(NewFolder.id)
            # Upload a file to the newly created folder
            File = '../samples/Examples.py'
            NewFolder.Upload(File)
            # Delete the link again
            Items = NewFolder.GetItems()
            Items[0].Delete()
            # Delete the newly created folder again
            NewFolder.Delete()
            # Check if the new folder is deleted
            try:
                Folder = A.get_folder(NewFolder.id)
                assert False
            except:
                pass
        except:
            assert False

    def test_patients_api_key(self):
        try:
            A = gtAgora(TestAgoraInterface.server, api_key=TestAgoraInterface.api_key)

            # Get a list of all patients
            Patients = A.get_patients()
            # Get all the patients born between 1970 and 1990 and are over 80kg
            P = A.get_patients('birth_date_gte=1970-01-01&birth_date_lte=1990-01-01&weight_min=80')
            # Get a patient by ID
            P0 = A.get_patient(Patients[0].id)
            # Get all the Exams of the first Patient
            E = Patients[0].get_exams()
            # Get all the Exams which have DTI in the name
            E = Patients[0].get_exams('name=DTI')
        except:
            assert False

    def test_exams_api_key(self):
        try:
            A = gtAgora(TestAgoraInterface.server, api_key=TestAgoraInterface.api_key)

            # Get a list of all Exams
            Exams = A.get_exams()
            # Get all Exams with DTI in the name
            E = A.get_exams('name=DTI')
            # Get all Exams which where measured in 2017
            E = A.get_exams('start_time_gte=2017-01-01&start_time_lt=2017-12-31')
            # Get an Exam by ID
            E1 = A.GetExam(Exams[0].id)
            # Get all the Series of the first Exam
            S = Exams[0].get_series()
            # Get all the raw/lab datasets of the first Exam
            D = Exams[0].get_datasets()
            RawDatasets = []
            for curDataset in D:
                if curDataset.type == DatasetType.PHILIPS_RAW:
                    RawDatasets.append(curDataset)
            # Get all the Series which have DTI in the name
            S = Exams[0].get_series('name=DTI')

            # get parameter of a rawfile
            Pars = RawDatasets[0].get_parameter('description__name=EX_CARD')
        except:
            assert False

    def test_series_api_key(self):
        try:
            A = gtAgora(TestAgoraInterface.server, api_key=TestAgoraInterface.api_key)

            # Get a list of all series with DTI in the name
            Series = A.get_series('name=DTI')
            # Get a series by ID
            S = A.get_serie(Series[0].id)
            # Get all the Datasets of the first Series
            D = Series[0].get_datasets()
            # Download all the files of the first series to the temporay folder
            DownloadedFiles = Series[0].download(tempfile.gettempdir())
            # check if downloaded files exist
            for cur_file in DownloadedFiles:
                if not os.path.isfile(cur_file.download_path):
                    raise("file does not exist")
        except:
            assert False

    def test_search_api_key(self):
        try:
            A = gtAgora(TestAgoraInterface.server, api_key=TestAgoraInterface.api_key)

            # Find all series with cardiac synchronization and a resulution higher than 2mm
            Series = A.Search('parameter.EX_CARD_sync > 0 AND parameter.EX_GEO_voxel_size_m < 2')
        except:
            assert False

    def test_connection_user_password(self):
        try:
            A = gtAgora(TestAgoraInterface.server, user=TestAgoraInterface.user, password=TestAgoraInterface.password)
        except:
            assert False

    def test_folders_user_password(self):
        try:
            A = gtAgora(TestAgoraInterface.server, user=TestAgoraInterface.user, password=TestAgoraInterface.password)

            # Get the root folder
            RootFolder = A.get_root_folder()
            # Get a folder by ID
            Folder = A.get_folder(RootFolder.id)
            # Get all subfolders of the root folder
            Subfolders = RootFolder.get_folders()
            # Get all items in the first subfolder
            Items = Subfolders[0].GetItems()
            # Get all Exams in the first subfolder
            Exams = Subfolders[0].get_exams()
            # Recursively get all Exams in the current folder and all subfolders
            Exams = Subfolders[0].get_exams(True)
            # Get all series in the first subfolder
            Series = Subfolders[0].get_series()
            # Recursively get all series in the current folder all subfolders
            Series = Subfolders[0].get_series(True)
            # Get all datasets in the first subfolder
            Datasets = Subfolders[0].get_datasets()
            # Recursively get all datasets in the current folder all subfolders
            Datasets = Subfolders[0].get_datasets(True)
            # Create a new folder in the root folder (the new folder object is returned)
            NewFolder = RootFolder.NewFolder('TestFolder')
            # Check if the new folder exists
            Folder = A.get_folder(NewFolder.id)
            if(not Folder):
                raise("Folder does not exist")
            # Link the first Exam to the newly created folder
            Exams[0].link_to_folder(NewFolder.id)
            # Upload a file to the newly created folder
            File = '../samples/Examples.py'
            NewFolder.Upload(File)
            # Delete the link again
            Items = NewFolder.GetItems()
            Items[0].Delete()
            # Delete the newly created folder again
            NewFolder.Delete()
            # Check if the new folder is deleted
            try:
                Folder = A.get_folder(NewFolder.id)
                assert False
            except:
                pass
        except:
            assert False

    def test_patients_user_password(self):
        try:
            A = gtAgora(TestAgoraInterface.server, user=TestAgoraInterface.user, password=TestAgoraInterface.password)

            # Get a list of all patients
            Patients = A.get_patients()
            # Get all the patients born between 1970 and 1990 and are over 80kg
            P = A.get_patients('birth_date_gte=1970-01-01&birth_date_lte=1990-01-01&weight_min=80')
            # Get a patient by ID
            P0 = A.get_patient(Patients[0].id)
            # Get all the Exams of the first Patient
            E = Patients[0].get_exams()
            # Get all the Exams which have DTI in the name
            E = Patients[0].get_exams('name=DTI')
        except:
            assert False

    def test_exams_user_password(self):
        try:
            A = gtAgora(TestAgoraInterface.server, user=TestAgoraInterface.user, password=TestAgoraInterface.password)

            # Get a list of all Exams
            Exams = A.get_exams()
            # Get all Exams with DTI in the name
            E = A.get_exams('name=DTI')
            # Get all Exams which where measured in 2017
            E = A.get_exams('start_time_gte=2017-01-01&start_time_lt=2017-12-31')
            # Get an Exam by ID
            E1 = A.GetExam(Exams[0].id)
            # Get all the Series of the first Exam
            S = Exams[0].get_series()
            # Get all the raw/lab datasets of the first Exam
            D = Exams[0].get_datasets()
            RawDatasets = []
            for curDataset in D:
                if curDataset.type == DatasetType.PHILIPS_RAW:
                    RawDatasets.append(curDataset)
            # Get all the Series which have DTI in the name
            S = Exams[0].get_series('name=DTI')

            # get parameter of a rawfile
            Pars = RawDatasets[0].get_parameter('description__name=EX_CARD')
        except:
            assert False

    def test_series_user_password(self):
        try:
            A = gtAgora(TestAgoraInterface.server, user=TestAgoraInterface.user, password=TestAgoraInterface.password)

            # Get a list of all series with DTI in the name
            Series = A.get_series('name=DTI')
            # Get a series by ID
            S = A.get_serie(Series[0].id)
            # Get all the Datasets of the first Series
            D = Series[0].get_datasets()
            # Download all the files of the first series to the temporay folder
            DownloadedFiles = Series[0].download(tempfile.gettempdir())
            # check if downloaded files exist
            for cur_file in DownloadedFiles:
                if not os.path.isfile(cur_file.download_path):
                    raise("file does not exist")
        except:
            assert False

    def test_search_user_password(self):
        try:
            A = gtAgora(TestAgoraInterface.server, user=TestAgoraInterface.user, password=TestAgoraInterface.password)

            # Find all series with cardiac synchronization and a resulution higher than 2mm
            Series = A.Search('parameter.EX_CARD_sync > 0 AND parameter.EX_GEO_voxel_size_m < 2')
        except:
            assert False
