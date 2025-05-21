import csv
import csv
import random

def generate_sample_csv(filename, num_students=10):
    # Skip Assignment 6 — we'll include 12 assignments total
    assignments = [f'Assignment {i}' for i in range(1, 14) if i != 6]

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name'] + assignments)

        for i in range(num_students):
            name = f'Student {i+1}'
            grades = [round(random.uniform(0, 5), 2) if random.random() > 0.1 else '' for _ in assignments]
            writer.writerow([name] + grades)

    print(f" Sample CSV '{filename}' generated with {num_students} students.")

# Run it:
generate_sample_csv("grades.csv", num_students=15)
def process_grades(input_filename, output_filename):
    try:
        with open(input_filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames + ["Total Points", "Average Points"]

            processed_rows = []

            for row in reader:
                grades = []
                for i in range(1, 13):
                    key = f'Assignment {i}'
                    try:
                        val = row.get(key, '').strip()
                        grade = float(val) if val else 0.0
                    except ValueError:
                        grade = 0.0
                    grades.append(grade)

                # Calculate Total Points using best 10 grades, capped at 30
                best_10 = sorted(grades, reverse=True)[:10]
                total_points = min(sum(best_10), 30.0)

                # Calculate Average Points from all submitted grades
                submitted_grades = [g for g in grades if g > 0]
                average_points = sum(submitted_grades) / len(submitted_grades) if submitted_grades else 0.0

                row["Total Points"] = round(total_points, 2)
                row["Average Points"] = round(average_points, 2)
                processed_rows.append(row)

        # Write processed data to new CSV
        with open(output_filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(processed_rows)

        print(f" Processed grades saved to: {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f" Unexpected error: {e}")

# ===== Run the function with your CSV file =====
if __name__ == "__main__":
    input_csv = 'grades.csv'               # Input CSV file with Assignment 1–12 columns
    output_csv = 'processed_grades.csv'    # Output CSV file with Total & Average Points
    process_grades(input_csv, output_csv)


