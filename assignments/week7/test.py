import csv
import random


grade_pool = [1,
              2,
              3]

add_grade = random.choice(grade_pool)

def read_table(filename="Technical Basics I_2025 - Sheet1.csv"):
    table_dict = {}

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row["Name"]
            stream = row["Stream"]
            email = row["Email"]
            link = row["Link to your GitHub"]
            week1 = row["week1"]
            #price = float(row["week1"])
            table_dict[name] = stream

    return table_dict