# The input script is script1.py which reads the survey data from a file named results.csv located in the same directory.

from python_survey_app.csvhelper.modules import read_csv, remove_duplicates

# Set the input file path
input_file = "python_survey_app\\results.csv"

# Read in the data from the input file
data = read_csv(input_file)

# Remove duplicates from the data
unique_data = remove_duplicates(data)