# Automated Marksheet Generator

**PS No.:** 90  
**Course:** B.Tech Computer Science and Engineering  
**Language:** Python 3

## Project description
This program reads student marks from a CSV file using Pandas. It calculates the total out of 300, percentage, grade, and pass/fail result for one student selected by roll number.

## Features
- Reads student records from `marks.csv` using Pandas.
- Provides a single-marksheet menu.
- Checks that all required CSV columns are present.
- Skips rows containing marks outside 0–100 and prints a warning.
- Calculates percentage to two decimal places.
- A student fails if any subject mark is below 40.
- Handles a missing CSV file and an unknown roll number.

## Grade scale
| Percentage | Grade |
|---|---|
| 90 and above | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| 40–49.99 | E |
| Below 40 | F |

## Requirements
- Python 3
- pandas

Install Pandas:
```bash
python -m pip install pandas
```

## How to run
Keep `one.py` and `marks.csv` in the same folder, then run:
```bash
python one.py
```
Choose `1` and enter the student's roll number when prompted.

To test the invalid-row case:
```bash
python one.py marks_invalid.csv
```

## CSV format
The CSV must contain these columns:
`RollNo, Name, Maths, Physics, Programming`

Each subject mark must be a whole number from 0 to 100.

## Files in this repository
- `one.py` — Python source code
- `marks.csv` — sample student data
- `marks_invalid.csv` — extra test data containing one invalid row
- `Test_cases_passed.pdf` — test-case output report
- `screenshots/` — project allocation screenshot and test output screenshots

## Test cases
See `Test_cases_passed.pdf` for the four test cases and expected outputs.
