# File handling and string cleaning

# importing required tool
import os
import random
from datetime import datetime


# intentionally messy set of student names
student_names = ["jack", " Lisa", "JOHN", "sam ", "mosa", "UWAIZ  ", "  Kuhle", "SANDISIWE", " akira", "remo"]


# making sure data/ folder exists before writing into it
def ensure_data_dir():
    os.makedirs("data", exist_ok=True)


# create a messy sample data file
def generate_data_file(num_records=10):
    ensure_data_dir()
    lines = []
    for n in range(num_records):
        name = random.choice(student_names)
        score = random.randint(0, 100)
        lines.append(f"{name}, {score}")

    with open("data/students.txt", "w") as f:
        for line in lines:
            f.write(line + "\n")

    return "Sample data file generated"


# load students and return a clean list of (name, score) tuples
def load_students(): 
    clean_records = []

    if not os.path.exists("data/students.txt"):
        return clean_records

    with open("data/students.txt", "r") as f:
        for messy_line in f:
            line = messy_line.strip()
            if not line:
                continue

            parts = line.split(",")
            if len(parts) != 2:
                continue

            name_part, score_part = parts
            name = name_part.strip().title()

            try:
                score = int(score_part.strip())
            except ValueError:
                continue

            clean_records.append((name, score))

    return clean_records


def export_report(text):
    ensure_data_dir()
    with open("data/report.txt", "w") as f:
        f.write(text)
    return (f"Exported report to {"data/report.txt"}")

def log_event(message):
    ensure_data_dir()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("data/activity.txt", "a") as f:
        f.write(f"[{timestamp}] {message}\n")