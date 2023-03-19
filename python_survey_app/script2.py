# The script named script2.py generates the output. The output contains the sanitized data which gets saved into a freshly created CSV file named "cleaned_output". It also displays the data on the terminal.
# Code opens the output file and reads each line, printing it to the console without the newline character. This allows us to see the cleaned data in a human-readable format.

from python_survey_app.csvhelper.modules import write_csv

# Set the output file path
output_file = "clean_results.csv"

# Write the cleaned data to the output file
write_csv(output_file, cleaned_data)

# Print out the cleaned data to the console
with open(output_file, "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
