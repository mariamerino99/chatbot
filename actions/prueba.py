
import csv
archivo = []
f = open('datos.csv')
csv_f = csv.reader(f)
for row in csv_f:
    archivo.append(row)
name = "Maria"
archivo.append([name])
#print(last_row)
#last_row.append(', 5')
#archivo = archivo[:-1]
#archivo.append(last_row)
#print(archivo[-1])
print(archivo)
#archivo.append(["Maria","21","Mujer","si"])
with open('datos.csv','w', newline='\n') as file:
    writer = csv.writer(file)
    writer = csv.writer(file, delimiter=',')
    writer.writerows(archivo)


#csv_f = csv.reader(f)
#for row in csv_f:
#    print(row[2])
#workbook = openpyxl.load_workbook(filename='datos.xlsx')
#worksheet = workbook['Hoja1']
#nrows = len(worksheet['A'])
#worksheet.cell(row=nrows+1, column=1, value = 'Maria')
#worksheet.cell(row=nrows+1, column=2, value = '21')
#worksheet.cell(row=nrows+1, column=3, value = 'No')
#workbook.save('datos.xlsx')

#print(nrows)
