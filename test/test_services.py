import unittest
import pandas as pd

from services import RegionsService


class TestRegionsService(unittest.TestCase):

    def test_create_data_frame(self):
        data = [
            {'region': 'Asia', 'country': 'Afghanistan', 'language': '3a7f90c6ef59f3002921b1295e3c8515dec70181', 'time': 0.35},
            {'region': 'Europe', 'country': 'Åland Islands', 'language': '0faa3ca7342a3742e96347c9d54d1e31084c8c66', 'time': 0.35},
            {'region': 'Africa', 'country': 'Algeria', 'language': '9070484c6833b8593fed70b865aff670db731721', 'time': 0.36},
            {'region': 'Oceania', 'country': 'American Samoa', 'language': 'a110cf41058a9ebc43f111581d39026cccb05463', 'time': 0.31},
            {'region': 'Americas', 'country': 'Anguilla', 'language': '7e07abe18d02075431aa1af84c0818a4ac030296', 'time': 0.31},
            {'region': 'Polar', 'country': 'Antarctica', 'language': '127d9d8fe6819cf80c59ac23190d6b1fcc877ce3', 'time': 0.37}
        ]
        data_frame = RegionsService.create_data_frame(data=data)
        self.assertEqual(type(data_frame), pd.DataFrame)


if __name__ == '__main__':
    unittest.main()
