from csvhelper.modules import read_csv, remove_duplicates, clean_data, write_csv

# Set the input file path
input_file = "results.csv"

# Read in the data from the input file
data = read_csv(input_file)

# Remove duplicates from the data
unique_data = remove_duplicates(data)

# Clean the data by capitalizing names and filtering answer 3 to be between 1 and 10
cleaned_data = clean_data(unique_data)

# Set the output file path
output_file = "clean_results.csv"

# Write the cleaned data to the output file
write_csv(output_file, cleaned_data)