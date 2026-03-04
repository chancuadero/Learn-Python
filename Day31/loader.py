from pathlib import Path
import csv

def filepath(path):
    path = Path(__file__).parent/"data"/path
    return path

def readcsv(filepath):
    with open(filepath, mode="r", encoding="utf-8-sig") as file:
        first_line = list(csv.DictReader(file))
    return first_line
