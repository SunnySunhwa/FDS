
from pickle import *
'''
from openpyxl import *

wb = load_workbook('class_1.xlsx')
ws = wb.active

g = ws.rows

student_data = []

for c1, c2 in g:
    student_data.append({c1.value : c2.value})

f = open('class_1.dat', 'wb')

for dic in student_data:
    dump(dic, f)

f.close()
'''
f = open('class_1.dat', 'rb')

raw_data = {}

try:
    while True:
        data = load(f)
        raw_data.update(data)
except EOFError:
    pass

print(raw_data)
