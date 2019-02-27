from gtAgoraPythonInterface import gtAgora
from gtAgoraPythonInterface import DatasetType
from gtAgoraPythonInterface import AgoraException
from gtAgoraPythonInterface import gtAgoraRequest
import tempfile
import os.path

class TestAgoraInterface:
    #server = 'http://127.0.0.1:8000'
    #api_key = '0853ac53-7aca-4e26-afc6-2a58c8cf953e'

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

    def test_philips_import(self):
        try:
            A = gtAgora(TestAgoraInterface.server, api_key=TestAgoraInterface.api_key)

            # Import a .raw/.lab dataset
            Rawfile = './data/philips/re_29042015_0933476_3_2_wipnormalffeV4.raw'  # the .raw file to import
            Labfile = './data/philips/re_29042015_0933476_3_2_wipnormalffeV4.lab'  # the .labfile file to import
            Files2Import = []
            Files2Import.append(Rawfile)
            Files2Import.append(Labfile)
            series = A.import_data(Files2Import)
            assert (series)
            assert (series.name == 'WIP Normal FFE')
        except:
            assert False

    def test_bruker_import(self):
        try:
            A = gtAgora(TestAgoraInterface.server, api_key=TestAgoraInterface.api_key)

            # Import a .raw/.lab dataset
            Directory = './data/bruker/'
            series = A.import_data(Directory)
            assert (series)
            assert (series.name == '1_Localizer')
        except:
            assert False


