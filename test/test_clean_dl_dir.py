import unittest
import clean_dl_dir as cdd


class Test_Clean_DL_dir(unittest.TestCase):

    def test_files_in_dl_dir(self):
        cdd.get_dl_files() = MagicMock(return_value=['file_1', 'file_2', 'file_3'])
        test_file_list= ('file_1', 'file_2', 'file_3')
        dl_files = cdd.get_dl_files()

        self.assertEqual(test_file_list, dl_files)