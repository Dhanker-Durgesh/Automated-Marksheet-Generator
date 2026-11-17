"""
Automated Marksheet Generator
PS No. 90 | Python 3, Pandas, Functions, File Handling

Run:
    python one.py
    python one.py marks_invalid.csv   # optional alternate input file
"""

import importlib
import sys
from pathlib import Path

try:
    pd = importlib.import_module("pandas")
except ModuleNotFoundError:
    pd = None

REQUIRED_COLUMNS = ["RollNo", "Name", "Maths", "Physics", "Programming"]
SUBJECTS = ["Maths", "Physics", "Programming"]


def calculate_grade(percentage):
    """Return the grade based on the project grading scale."""
    if percentage >= 90:
        return "A+"
    if percentage >= 80:
        return "A"
    if percentage >= 70:
        return "B"
    if percentage >= 60:
        return "C"
    if percentage >= 50:
        return "D"
    if percentage >= 40:
        return "E"
    return "F"


def load_marks(file_name):
    """Read the CSV, validate rows, and skip invalid marks with a warning."""
    # FIX 2: clear message if Pandas is not installed
    if pd is None:
        print("Error: Pandas is not installed. Run: pip install pandas")
        return None

    file_path = Path(file_name)

    if not file_path.exists():
        print(f"Error: File '{file_name}' not found.")
        return None

    try:
        data = pd.read_csv(file_path)
    except Exception as error:
        print(f"Error reading CSV file: {error}")
        return None

    missing_columns = [column for column in REQUIRED_COLUMNS
                       if column not in data.columns]
    if missing_columns:
        print("Error: CSV is missing required column(s): "
              + ", ".join(missing_columns))
        return None

    valid_rows = []
    for _, row in data.iterrows():
        try:
            marks = [float(row[subject]) for subject in SUBJECTS]
            if any(mark < 0 or mark > 100 for mark in marks):
                raise ValueError
            if any(mark != int(mark) for mark in marks):
                raise ValueError
            valid_rows.append(row)
        except (TypeError, ValueError):
            # FIX 1: added the word "skipped" to match the expected output
            print(
                f"Warning: Row for roll {row.get('RollNo', 'unknown')} "
                "skipped - marks must be between 0 and 100."
            )

    if not valid_rows:
        return pd.DataFrame(columns=REQUIRED_COLUMNS)

    return pd.DataFrame(valid_rows).reset_index(drop=True)


def print_marksheet(student):
    """Calculate and print one student's marksheet."""
    marks = [int(student[subject]) for subject in SUBJECTS]
    total = sum(marks)
    percentage = total / 300 * 100
    grade = calculate_grade(percentage)

    failed_subjects = [
        subject for subject in SUBJECTS if int(student[subject]) < 40
    ]
    result = "FAIL" if failed_subjects else "PASS"

    print(f"\nRoll No: {student['RollNo']} | Name: {student['Name']}")
    print(
        f"Maths: {marks[0]} | Physics: {marks[1]} | "
        f"Programming: {marks[2]}"
    )
    print(f"Total: {total}/300 | Percentage: {percentage:.2f}%")
    if failed_subjects:
        print(f"Grade: {grade} | Result: {result} "
              f"({', '.join(failed_subjects)} below 40)")
    else:
        print(f"Grade: {grade} | Result: {result}")


def main():
    file_name = sys.argv[1] if len(sys.argv) > 1 else "marks.csv"
    print("===== AUTOMATED MARKSHEET GENERATOR =====")
    print("1. Single marksheet")

    choice = input("Enter your choice: ").strip()
    if choice != "1":
        print("Invalid menu choice.")
        return

    data = load_marks(file_name)
    if data is None:
        return

    roll_no = input("Enter roll number: ").strip()
    matching = data[data["RollNo"].astype(str).str.strip() == roll_no]

    if matching.empty:
        print(f"Roll number {roll_no} not found.")
        return

    print_marksheet(matching.iloc[0])


if __name__ == "__main__":
    main()