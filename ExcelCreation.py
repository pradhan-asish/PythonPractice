import openpyxl,os
wb = openpyxl.Workbook()
print(wb)
print(wb.sheetnames)
sheet1 = wb['Sheet']
print(sheet1['A1'].value)

sheet1['A1'].value = 10
sheet1['A2'].value = 12
sheet1['A3'].value = 13
sheet1['A4'].value = 14

wb.save('Example1.xlsx')

