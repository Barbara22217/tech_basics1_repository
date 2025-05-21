import csv
import random

# initializing the rows list
rows = []

# reading csv file
#with open("Technical Basics I_2025 - Sheet1.csv", 'r') as csvfile:
    # creating a csv reader object
    #csvreader = csv.reader(csvfile)

with open('Technical Basics I_2025 - Sheet1.csv', mode='r', newline='') as infile:
    reader = list(csv.reader(infile))
    headers = reader[0]
    rows = reader[1:]

    headers = reader[0]
    headers.append('week8')
    headers.append('week9')
    headers.append('week10')
    headers.append('week11')
    headers.append('week12')
    headers.append('week13')
    headers.append('Total Points')
    headers.append('Average Points')

    if 'Total Points' not in headers:
        headers.append('Total Points')
    if 'Average Points' not in headers:
        headers.append('Average Points')

    # Define the full range of weeks (excluding week6)
    weeks = ['week1', 'week2', 'week3', 'week4', 'week5', 'week7', 'week8', 'week9', 'week10', 'week11', 'week12',
             'week13']

    # Read existing CSV
    with open('Technical Basics I_2025 - Sheet1.csv', mode='r', newline='') as infile:
        reader = list(csv.reader(infile))
        headers = reader[0]
        rows = reader[1:]

        # Add missing week headers if they're not already in the CSV
        for week in weeks:
            if week not in headers:
                headers.append(week)

        # Add random grades (1–3) for each week to each row
        updated_rows = []
        for row in rows:
            # Fill in missing values with random grades for each new week
            existing_len = len(row)
            # For each missing column, add a random grade
            for i in range(len(headers) - existing_len):
                row.append(str(random.choice([1, 2, 3])))
            updated_rows.append(row)

    weeks_values = rows[-len(weeks):]  # get the last N week columns
    int_scores = [int(val) for val in weeks_values if isinstance(val, str) and val.strip().isdigit()]
    total = sum(int_scores)
    average = round(total / len(week), 2)

    # Add total and average to the row
    rows.append(str(total))
    rows.append(str(average))

    updated_rows.append(rows)

    # Write back to CSV
    with open('Technical Basics I_2025 - Sheet1.csv', mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(headers)
        writer.writerows(updated_rows)
    # extracting field names through first row, notice that it removes the first row at the same time from csvreader

    # printing the field names
    #print('Field names are:', fields)

    # extracting each data row one by one, notice that the items are already splitted for you
    for row in reader:
        rows.append(row)
        print(row)
        with open('Technical Basics I_2025 - Sheet1.csv', mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(headers)
            writer.writerows(updated_rows)


        # get total number of rows
    #print("Total no. of rows:", csvreader.line_num)

    #df['week7'] = [random.choice(['1', '2', '3']) for _ in range(len(df))]




import csv
import random

# File path
filename = 'Technical Basics I_2025 - Sheet1.csv'

# Define the full set of week columns
week_columns = ['week1', 'week2', 'week3', 'week4', 'week5', 'week7',
                'week8', 'week9', 'week10', 'week11', 'week12', 'week13']

# Open and read the original CSV
with open(filename, mode='r', newline='', encoding='utf-8') as infile:
    reader = list(csv.reader(infile))
    headers = reader[0]
    rows = reader[1:]

# Add missing week columns
for week in week_columns:
    if week not in headers:
        headers.append(week)

# Add Total Points and Average Points columns if not present
if 'Total Points' not in headers:
    headers.append('Total Points')
if 'Average Points' not in headers:
    headers.append('Average Points')

# Indices of week columns in the updated headers
week_indices = [headers.index(week) for week in week_columns]

# Process each row
updated_rows = []
for row in rows:
    # Pad row to match the number of headers
    while len(row) < len(headers):
        row.append('')

    # Fill in missing week values with random grades
    for idx in week_indices:
        if not row[idx].strip() or row[idx].strip() == '-':
            row[idx] = str(random.choice([1, 2, 3]))

    # Compute total and average points
    scores = [int(row[idx]) for idx in week_indices if row[idx].isdigit()]
    total = sum(scores)
    average = round(total / len(week_columns), 2)

    row[headers.index('Total Points')] = str(total)
    row[headers.index('Average Points')] = str(average)

    updated_rows.append(row)

# Write the updated content back to the file
with open(filename, mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(headers)
    writer.writerows(updated_rows)

print("CSV updated successfully.")
