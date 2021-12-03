import sys
import unittest
from most_active_cookie import *
import io
from contextlib import redirect_stdout



class Test(unittest.TestCase):

    def test_invalid_amount_of_arguments(self):


        capture_stdout = io.StringIO()

        with redirect_stdout(capture_stdout):
            main(['most_active_cookie.py', 'test.csv', '-d', '2018-12-08', 'f'])
        self.assertEqual(capture_stdout.getvalue(),
                         "Invalid number of arguments. Usage Example: python3 most_active_cookie.py filename -d date\n")

    def test_invalid_date_in_command_line(self):
        capture_stdout = io.StringIO()
        with redirect_stdout(capture_stdout):
            main(['most_active_cookie.py', 'test.csv', '-d', '2018-12-089'])

        self.assertEqual(capture_stdout.getvalue(),
                         "Invalid Date. Example Format: YYYY-MM-DD\n")

    def test_with_file_that_does_not_exist(self):
        capture_stdout = io.StringIO()
        args_list = ['most_active_cookie.py', 'DNE.csv', '-d', '2018-12-08']
        csv_file_name = args_list[1]
        with redirect_stdout(capture_stdout):
            main(args_list)



        self.assertEqual(capture_stdout.getvalue(),
                         f"No such file or directory: {csv_file_name}.\n")

    '''def test_with_file_w_no_permissions(self):
        capture_stdout = io.StringIO()
        args_list = ['most_active_cookie.py', 'no_permission.csv', '-d', '2018-12-08']
        csv_file_name = args_list[1]
        with redirect_stdout(capture_stdout):
            main(args_list)

        self.assertEqual(capture_stdout.getvalue(),
                         f"Permission Error: Cannot access {csv_file_name}\n") '''

    def test_with_empty_file(self):
        capture_stdout = io.StringIO()
        args_list = ['most_active_cookie.py', 'empty_file.csv', '-d', '2018-12-08']
        csv_file_name = args_list[1]
        with redirect_stdout(capture_stdout):
            main(args_list)

        self.assertEqual(capture_stdout.getvalue(), "Empty File. No most active cooke\n")

    def test_one_most_active_cookie(self):
        capture_stdout = io.StringIO()
        args_list = ['most_active_cookie.py', 'test.csv', '-d', '2018-12-09']
        csv_file_name = args_list[1]
        with redirect_stdout(capture_stdout):
            main(args_list)

        self.assertEqual(capture_stdout.getvalue(), "AtY0laUfhglK3lC7\n")

    def test_multiple_active_cookies(self):
        capture_stdout = io.StringIO()
        args_list = ['most_active_cookie.py', 'test.csv', '-d', '2018-12-08']
        csv_file_name = args_list[1]
        with redirect_stdout(capture_stdout):
            main(args_list)

        self.assertEqual(capture_stdout.getvalue(), "SAZuXPGUrfbcn5UA\n4sMM2LxV07bPJzwf\nfbcn5UAVanZf6UtG\n")

    def test_if_date_is_not_in_csv(self):
        capture_stdout = io.StringIO()
        args_list = ['most_active_cookie.py', 'test.csv', '-d', '2018-12-01']
        date = args_list[3]
        with redirect_stdout(capture_stdout):
            main(args_list)

        self.assertEqual(capture_stdout.getvalue(), f"No cookies on {date}\n")

    def test_one_element_csv(self):
        capture_stdout = io.StringIO()
        args_list = ['most_active_cookie.py', 'one_element.csv', '-d', '2018-12-09']

        with redirect_stdout(capture_stdout):
            main(args_list)

        self.assertEqual(capture_stdout.getvalue(), "AtY0laUfhglK3lC7\n")






if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()


