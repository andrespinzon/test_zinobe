import unittest

from common import ExternalApi


class TestCommon(unittest.TestCase):
    def setUp(self) -> None:
        self.service = ExternalApi()

    def test_get_all_regions(self):
        regions = self.service.get_all_regions()
        self.assertEqual(len(regions), 6)
        self.assertEqual(type(regions), type([]))
        self.assertIn('Asia', regions)

    def test_get_first_country_by_region(self):
        regions = self.service.get_all_regions()
        self.assertEqual(len(regions), 6)
        self.assertTrue(isinstance(regions, list))
        self.assertIn('Asia', regions)

        collections = self.service.get_first_country_by_region(regions=regions)
        self.assertEqual(len(collections), 6)
        self.assertTrue(isinstance(collections, list))
        self.assertEqual('Asia', collections[0]['region'])


if __name__ == '__main__':
    unittest.main()
