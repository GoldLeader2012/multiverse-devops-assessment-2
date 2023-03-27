# Print out the cleaned data to the console
with open(output_file, "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
