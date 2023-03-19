# The Pytests for the functions defined in the modules.py file can be found in the tests.py file.

from csvhelper.modules import read_csv, remove_duplicates


def test_read_csv_file():
    # Define the expected number of rows in the CSV file
    expected = 26
    # Call the read_csv function to read the CSV file
    actual = read_csv("results.csv")
    # Check that the actual number of rows matches the expected number of rows
    assert len(actual) == expected


def test_remove_duplicates():
    # Read the contents of a CSV file using the read_csv function
    data = read_csv("results.csv")
    # Call the remove_duplicates function to remove duplicate rows from the data
    unique_data = remove_duplicates(data)
    # Create a set of unique IDs from the unique_data list to check that all rows are unique
    unique = set(row[0] for row in unique_data)
    # Check that the number of unique rows in the unique_data list matches the number of unique IDs
    assert len(unique_data) == len(unique)
