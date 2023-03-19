# This file contains all the functions for the app to use in scipt1 and script2


def read_csv(file_path):
    data = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() != "":
                data.append(line.strip().split(","))
    return data


def remove_duplicates(data):
    unique_data = []
    user_ids = set()
    for row in data:
        if row[0] not in user_ids:
            unique_data.append(row)
            user_ids.add(row[0])
    return unique_data


def clean_data(data):
    cleaned_data = []
    for row in data:
        try:
            row[2] = row[2].capitalize()
            row[1] = row[1].capitalize()
            answer_3 = int(row[5])
            if answer_3 >= 1 and answer_3 <= 10:
                cleaned_data.append(row)
        except ValueError:
            continue
    return cleaned_data


def write_csv(file_path, data):
    with open(file_path, "w") as file:
        for row in data:
            file.write(",".join(row) + "\n")
