import openpyxl, os
workbook = openpyxl.load_workbook('sample_data.xlsx')
print(type(workbook))
print(workbook.sheetnames)
sheet = workbook['Sheet 1']
cell = sheet['A1']

print(sheet['A1'])
print(cell.value)
