from app.csvhelper.modules import write_csv

# Set the output file path
output_file = "clean_results.csv"

# Write the cleaned data to the output file
write_csv(output_file, cleaned_data)

# Print out the cleaned data to the console
with open(output_file, "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
