import xlrd

workbook = xlrd.open_workbook("datos.xlsx")
worksheet = workbook.sheet_by_index(0)
nrows = worksheet.nrows
print(nrows)
