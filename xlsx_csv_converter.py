import openpyxl
import csv


def csvWriter(*args):
    final_datasets = args[0] + '.csv'
    xlsxRead = openpyxl.load_workbook(args[0])
    active_sheet = xlsxRead.get_active_sheet()
    with open(final_datasets, 'w', newline='') as file:  # open('test.csv', 'w', newline="") for python 3
        c = csv.writer(file)
        for row in active_sheet.rows:
            c.writerow([cell.value for cell in row])