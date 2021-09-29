#!/usr/bin/python3
import mysql.connector
# import xlrd
import openpyxl
from pathlib import Path

cnx = mysql.connector.connect(user='root', password='L1nd@//Q^^',host='localhost',database='adata')

cnx.close()
xlsx_file = Path('/Users/lindawong/Documents/VSCode/GitHub/python-excel','2018-01.xlsx')
wb_obj = openpyxl.load_workbook(xlsx_file)
# print(wb_obj)
sheet = wb_obj.active
# print(sheet)
for row in sheet.iter_rows():
    for cell in row:
        print(cell.value, end=" ")
    print()

# loc = ('/Users/lindawong/Documents/VSCode/GitHub/python-excel/2018-01.xlsx')
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)

# sheet.cell_value(0, 0)

# for i in range(sheet.ncols):
#     print(sheet.cell_value(0,i))