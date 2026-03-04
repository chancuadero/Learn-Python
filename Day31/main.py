from loader import readcsv,filepath
from processor import cleanData


file_name = input("What is the file name? ")
stocks = filepath(file_name)

read_stocks = readcsv(stocks)
final_data = cleanData(read_stocks)
print(final_data)

