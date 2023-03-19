# The Pytests for the functions defined in the modules.py file can be found in the tests.py file.

from csvhelper.modules import read_csv


def test_read_csv_file():
    # Define the expected number of rows in the CSV file
    expected = 17
    # Call the read_csv function to read the CSV file
    actual = read_csv("clean_results.csv")
    # Check that the actual number of rows matches the expected number of rows
    assert len(actual) == expected
