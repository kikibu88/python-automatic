import xlrd, unittest
from ddt import ddt, data, unpack
from selenium import webdriver

def get_data(data.xlsx):
    rows = []
    book = xlrd.open_workbook(data.xlsx)
    sheet = book.sheet_by_index(0)
    for row_idx in range(1, sheet.nrows):
        rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
    return rows
