"""
The read_csv() function is called with the input file path, which returns the data as a list of lists. The remove_duplicates() function is then called with the data, which removes duplicate rows based on the first column. The resulting unique data is stored in a variable called unique_data.

The clean_data() function is called with the unique data, which performs data cleaning by capitalizing the names in the second and third columns and filtering answer 3 to be between 1 and 10. The resulting cleaned data is stored in a variable called cleaned_data.
"""

from python_survey_app.csvhelper.modules import read_csv, remove_duplicates, clean_data

# Set the input file path
input_file = "python_survey_app\\results.csv"

# Read in the data from the input file
data = read_csv(input_file)

# Remove duplicates from the data
unique_data = remove_duplicates(data)

# Clean the data by capitalizing names and filtering answer 3 to be between 1 and 10
cleaned_data = clean_data(unique_data)
