from pathlib import Path
import csv

def filepath(path):
    path = Path(__file__).parent/"data"/path
    return path

file_name = input("What is the file name? ")
stocks = filepath(file_name)

def readcsv(filepath):
    with open(filepath, mode="r", encoding="utf-8-sig") as file:
        first_line = list(csv.DictReader(file))
    return first_line

read_stocks = readcsv(stocks)
print(read_stocks)
