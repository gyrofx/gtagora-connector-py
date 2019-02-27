import os

from gtAgoraPythonInterface import gtAgora


class TestAgoraInterface:
    # server = 'http://127.0.0.1:8000'
    # api_key = '0853ac53-7aca-4e26-afc6-2a58c8cf953e'

    server = 'http://127.0.0.1:8000'
    api_key = 'fc820160-e39b-4333-a587-c53b18ff70b6'
    gtAgora.mVerifyCertificate = False

    def test_philips_import(self):
        try:
            A = gtAgora(TestAgoraInterface.server, api_key=TestAgoraInterface.api_key)

            # Import a .raw/.lab dataset
            Files2Import = ['ma_21042016_1510063_6_2_wipt1wtseclearV4.raw',
                            'ma_21042016_1510063_6_2_wipt1wtseclearV4.lab',
                            'ma_21042016_1510063_6_1_wipt1wtseclearV4.par',
                            'ma_21042016_1510063_6_1_wipt1wtseclearV4.rec',
                            'log_ma_21042016_1510063_6_2_wipt1wtseclearV4.log',
                            'ma_21042016_1510063_6_2_wipt1wtseclearV4.gve',
                            'import1.json'
                            ]

            Files2Import = [os.path.join('D:/felix/Desktop/Wrist', file) for file in Files2Import]

            series = A.import_data(Files2Import, jsonImportFile='import1.json', shouldPrintProgress=True)
            assert (series)
            #assert (series.name == 'WIP Normal FFE')
        except:
            assert False

    def test_philips_import_2(self):
        try:
            A = gtAgora(TestAgoraInterface.server, api_key=TestAgoraInterface.api_key)

            # Import a .raw/.lab dataset
            Files2Import = ['ma_21042016_1510063_6_2_wipt1wtseclearV4.raw',
                            'ma_21042016_1510063_6_2_wipt1wtseclearV4.lab',
                            'ma_21042016_1510063_6_1_wipt1wtseclearV4.par',
                            'ma_21042016_1510063_6_1_wipt1wtseclearV4.rec',
                            'ma_21042016_1510063_6_2_wipt1wtseclearV4.par',
                            'ma_21042016_1510063_6_2_wipt1wtseclearV4.rec',
                            'log_ma_21042016_1510063_6_2_wipt1wtseclearV4.log',
                            'ma_21042016_1510063_6_2_wipt1wtseclearV4.gve',
                            'import2.json'
                            ]

            Files2Import = [os.path.join('D:/felix/Desktop/Wrist', file) for file in Files2Import]

            series = A.import_data(Files2Import, jsonImportFile='import2kwargs.json', shouldPrintProgress=True)
            assert (series)
            #assert (series.name == 'WIP Normal FFE')
        except:
            assert False


if __name__ == "__main__":
    TestAgoraInterface().test_philips_import_2()
