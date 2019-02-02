# -*- coding: utf-8 -*-
from openpyxl import load_workbook
specification = open("result.csv", 'wb')
specification.write('Order No.,Gas,Max Inlet Pressure(Bar),Max Outlet Pressure(Bar),Inlet Connection,Outlet Connection,Features,Type\n')
feature = open("feature.csv", 'wb')
wb = load_workbook('regulator.xlsx')
sheet_names = wb.get_sheet_names()
feaDict = dict()
feaCount = 1
for name in sheet_names:
    print name
    ws = wb.get_sheet_by_name(name)
    line = []
    for row in ws.iter_rows(min_row = ws.max_row, min_col = 5, max_col = 10, max_row = ws.max_row):
        for cell in row:
            line.append(str(cell.value))
    fea = []
    for row in ws.iter_rows(min_row = 4, min_col = 5, max_col = 5, max_row = ws.max_row - 3):
        for cell in row:
            if cell.value in feaDict:
                fea.append(str(feaDict[cell.value]))
            else:
                feaDict[cell.value] = feaCount
                fea.append(str(feaCount))
                feature.write(str(feaCount))
                feature.write(',')
                feaCount = feaCount + 1
                feature.write(cell.value[2:-1])
                feature.write('\n')
    line.append('_'.join(fea))
    line.append(ws['E2'].value)
    specification.write(','.join(line))
    specification.write('\n')
specification.close()
feature.close()