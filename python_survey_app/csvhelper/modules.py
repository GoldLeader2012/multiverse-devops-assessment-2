# This file contains all the functions for the app to use in scipt1 and script2


def read_csv(file_path):
    data = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() != "":
                data.append(line.strip().split(","))
    return data
