import openpyxl, os
workbook = openpyxl.load_workbook('sample_data.xlsx')
print(type(workbook))
print(workbook.get_sheet_names())
