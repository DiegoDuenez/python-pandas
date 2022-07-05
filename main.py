
# PRIMER EJEMPLO 

import xlsxwriter
 
workbook = xlsxwriter.Workbook('Ejemplo1.xlsx')
 
worksheet = workbook.add_worksheet()
 
worksheet.write('A1', 'Hello..')
worksheet.write('B1', 'Geeks')
worksheet.write('C1', 'For')
worksheet.write('D1', 'Geeks')
 
workbook.close()


##################################################################################################################################################################



# SEGUNDO EJEMPLO
# Usar la notación fila-columna (valor de indexación) para escribir datos en las celdas específicas.

'''import xlsxwriter
 
workbook = xlsxwriter.Workbook('Ejemplo2.xlsx')
worksheet = workbook.add_worksheet()
 
row = 0
column = 0
 
content = ["ankit", "rahul", "priya", "harshita",
                    "sumit", "neeraj", "shivam"]
 
for item in content :
 
    worksheet.write(row, column, item)
 
    row += 1
     
workbook.close()'''




##################################################################################################################################################################


# TERCER EJEMPLO
# Creando una nueva hoja con el nombre específico

'''import xlsxwriter
 
workbook = xlsxwriter.Workbook('Ejemplo3.xlsx')
 
worksheet = workbook.add_worksheet("My sheet")
 
scores = (
    ['Diego', 1000],
    ['Brayan',   100],
    ['Francisco',  300],
    ['Andres',    50],
    ['Luis',   100],
)
 
row = 0
col = 0
 
for name, score in (scores):
    worksheet.write(row, col, name)
    worksheet.write(row, col + 1, score)
    row += 1
 
workbook.close()'''
