import unittest
import mock
import my_functions as mf


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.test_data_empty = {
            'results': []
        }
        self.test_data = {
            'results': [{'translation': {'title': 'My title'}}]
        }

    @mock.patch('my_functions.fetch_url')
    def test_get_titles(self, my_fetch):
        my_fetch.return_value = self.test_data_empty
        self.assertEqual(list(mf.get_titles('random')), [])
        my_fetch.return_value = self.test_data
        self.assertEqual(list(mf.get_titles('random')), ['My title'])


if __name__ == '__main__':
    unittest.main()
