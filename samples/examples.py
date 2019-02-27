import tempfile

from gtagora.agora import Agora
from gtagora.models.dataset import DatasetType
# from gtAgoraPythonInterface import DatasetType
# from gtAgoraPythonInterface import AgoraException
# from gtAgoraPythonInterface import gtAgoraRequest
# import tempfile

try:
    agora_server = 'http://localhost:8000'
    user = 'martin'
    api_key = 'dd178259-b877-4cd6-95e0-1bd1109da864'

    # ping the Agora server
    # IsConnection, ErrorMessage = Client().Ping(agora_server)
    # if not IsConnection:
    #    raise AgoraException('Could not connect to Agora: ' + ErrorMessage)

    # Create the gtAgora class and connect via username/password
    # A = Agora.create(agora_server, user=user, password=password)

    # Create the gtAgora class and connect via API key
    # (to create an API key please go to your user profile within Agora and select the "API-Key" menu)
    agora = Agora.create(agora_server, api_key=api_key)
    ping = agora.ping()
    print(f"Ping: {ping}")
    # --------------------------- Users ---------------------------
    users = agora.get_users()
    print(f"Users found: {len(users)}")

    groups = agora.get_groups()
    print(f"Groups found: {len(groups)}")

    # --------------------------- Folders ---------------------------
    # Get the root folder
    root_folder = agora.get_root_folder()
    print(f"Root folder ID: {root_folder.id}")

    # Get a folder by ID
    folder = agora.get_folder(root_folder.id)
    print(f"Folder with ID {root_folder.id}: {folder.name}")

    # # Get all subfolders of the root folder
    subfolders = root_folder.get_folders()
    print(f"Folder {root_folder.id} has {len(subfolders)} subfolders")
    for s in subfolders:
        print(f" - {s.name}")
    
    # # Get all items in the first subfolder
    # items = subfolders[0].get_items()
    # print(f"Folder {subfolders[0].name} has {len(items)} items")
    # for item in items:
    #     print(f" - {item}")

    # # Get all Exams in the first subfolder
    # exams = subfolders[0].get_exams()
    # print(f"Folder {subfolders[0].name} has {len(exams)} exams")
    # for exam in exams:
    #     print(f" - {exam}")

    # # Recursively get all Exams in the current folder and all subfolders
    # exams = subfolders[0].get_exams(recursive=True)
    # print(f"Folder {subfolders[0].name} has {len(exams)} exams")
    # for exam in exams:
    #     print(f" - {exam}")

    # # Get all series in the first subfolder
    # series = subfolders[0].get_series()
    # print(f"Folder {subfolders[0].name} has {len(series)} series")
    # for s in series:
    #     print(f" - {s}")

    # # Recursively get all series in the current folder all subfolders
    # series = subfolders[0].get_series(recursive=True)
    # print(f"Folder {subfolders[0].name} has {len(series)} series")
    # for s in series:
    #     print(f" - {s}")

    # # Get all datasets in the first subfolder
    # datasets = subfolders[0].get_datasets()
    # print(f"Folder {subfolders[0].name} has {len(datasets)} datasets")
    # for d in datasets:
    #     print(f" - {d}")

    # # Recursively get all datasets in the current folder all subfolders
    # datasets = subfolders[0].get_datasets(recursive=True)
    # print(f"Folder {subfolders[0].name} has {len(datasets)} datasets")
    # for s in datasets:
    #     print(f" - {d}")

    # # Create a new folder in the root folder (the new folder object is returned)
    # new_folder = root_folder.create_folder('TestFolder')
    # print(f"New folder ID: {new_folder.id}")

    # exams = agora.get_exams()

    # # Link the first Exam to the newly created folder
    # exam_item = exams[0].link_to_folder(new_folder.id)
    # print(f"New Link ID: {exam_item.id}")

    # # Delete the link again
    # items = new_folder.get_items()
    # items[0].delete()

    # # Delete the newly created folder again
    # new_folder.delete()

    # # Download all files from the current folder to the temp directory
    # downloaded_files = subfolders[0].download(tempfile.gettempdir())
    # print(f"Downloaded files: ")
    # for f in downloaded_files:
    #     print(f'  - {f}')

    # # Download all files in the current folder and all subfolders
    # downloaded_files = subfolders[0].download(tempfile.gettempdir(), True)
    # print(f"Downloaded files: ")
    # for f in downloaded_files:
    #     print(f'  - {f}')

    # # Upload a file to the root folder
    # file = __file__
    # datasets = root_folder.upload(file)
    # print(f"Uploaded dataset: {', '.join([str(d) for d in datasets])}")

    # for d in datasets:
    #     d.delete()
    
    # # Upload a file to the parent folder of an item
    # #parent_folder = agora.get_folder(items[0].folder)
    # #parent_folder.upload(file)

    # # --------------------------- Patients ---------------------------
    # # Get a list of all patients
    # patient_list = agora.get_patients()
    # print(f"Patients len: {len(patient_list)}")

    # # Get all the patients born between 1970 and 1990 and are over 80kg
    # patient_list = agora.get_patients({
    #     'birth_date_gte': '1970-01-01', 
    #     'birth_date_lte': '1990-01-01', 
    #     'weight_min': 80
    # })
    # print(f"Patients len: {len(patient_list)}")

    # # Get a patient by ID
    # patient_0 = agora.get_patient(patient_list[0].id)
    # print(f"Patients id {patient_list[0].id}: {patient_0}")

    # # Get all the Exams of the first Patient
    # exams = patient_0.get_exams()

    # # Get all the Exams which have DTI in the name
    # exam = patient_0.get_exams({'name': 'DTI'})

    # # Download all the files of the first patient to the temporay folder
    # downloaded_files = patient_0.download(tempfile.gettempdir())
    # print(f"Downloaded files: ")
    # for f in downloaded_files:
    #     print(f'  - {f}')

    # --------------------------- Exams ---------------------------
    # Get a list of all Exams
    exams = agora.get_exams()
    # Get all Exams with DTI in the name
    e = agora.get_exams({'name': 'DTI'})
    # Get all Exams which where measured in 2017
    e = agora.get_exams({
        'start_time_gte': '2017-01-01', 
        'start_time_lt': '2017-12-31'
    })
    # Get an Exam by ID
    e1 = agora.get_exam(exams[0].id)
    # Get all the Series of the first Exam
    s = exams[0].get_series()
    # Get all the raw/lab datasets of the first Exam
    d = exams[0].get_datasets()
    raw_datasets = []
    for dataset in d:
        if dataset.type == DatasetType.PHILIPS_RAW:
            raw_datasets.append(dataset)
    # # Get all the Series which have DTI in the name
    # s = exams[0].get_series({'name': 'DTI'})
    # # Download all the files of the first exam to the temporay folder
    # downloaded_files = exams[0].download(tempfile.gettempdir())
    # print(f"Downloaded files: ")
    # for f in downloaded_files:
    #     print(f'  - {f}')

    # # --------------------------- Series ---------------------------
    # # Get a list of all series with DTI in the name
    # series = agora.get_series({'name': 'DTI'})

    # # Get a series by ID
    # s = agora.get_serie(series[0].id)
    # print(f"Series {series[0].id}: {s}")

    # # Get all the Datasets of the first Series
    # d = series[0].get_datasets()
    # print(f"Datasets of series {series[0].id}: {len(d)}")

    # # Add the first series to the root folder
    # series_link = series[0].link_to_folder(root_folder.id)
    # print(f"New Link ID: {series_link.id}")

    # # # Add the first dataset to the root folder
    # # dataset_link = d[0].link_to_folder(root_folder.id)
    # # print(f"New Link ID: {dataset_link.id}")

    # # Delete the link again
    # series_link.delete()
    # # dataset_link.delete()

    # # Download all the files of the first series to the temporay folder
    # downloaded_files = series[0].download(tempfile.gettempdir())
    # print(f"Downloaded files: ")
    # for f in downloaded_files:
    #     print(f'  - {f}')

    # # Upload a file to the series
    # file = __file__
    # datasets = series[0].upload(file)
    # print(f"Uploaded dataset: {', '.join([str(d) for d in datasets])}")

    # for d in datasets:
    #     d.delete()

    # --------------------------- Parameter ---------------------------
    # Get the parameter of a dataset with EX_CARD in the name
    parameter = raw_datasets[0].get_parameter('description__name=EX_CARD')

    # --------------------------- Search ---------------------------
    # Find all series with cardiac synchronization and a resulution higher than 2mm
    series = agora.search('parameter.EX_CARD_sync > 0 AND parameter.EX_GEO_voxel_size_m < 2')
    # Import a .raw/.lab dataset
    data_path = Path(__file__).parent / 'tests/data/philips'  # the .raw file to import
    series = agora.import_data(data_path.glob("*.*"))  # Returns the just imported series

    print('Successfully completed')
except Exception as e:
    print(str(e))

