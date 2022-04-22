import csv
import pandas as pd

if __name__ == '__main__':
    csvFileName = input('csv filename?')
    file = open(csvFileName)
    type(file)

    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    header

    excelFileName = input("Excel File Name?")
    xl = pd.ExcelFile(excelFileName)
    xl.sheet_names
