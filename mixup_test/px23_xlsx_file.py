import openpyxl

file = ("C:\\Users\\정성환\\Desktop\\pythonworkspace\\Pygame\\pygame_info\\numbers.xlsx")
a = openpyxl.load_workbook(file)

sheet = a.active
valuse = sheet.cell(row = 1, column = 1).value
print(valuse)