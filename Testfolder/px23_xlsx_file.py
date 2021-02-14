import openpyxl

file = ("numbers.xlsx")
a = openpyxl.load_workbook(file)

sheet = a.active
valuse = sheet.cell(column = 1, row = 1).value
print(valuse)