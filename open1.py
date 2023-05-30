from openpyxl import load_workbook

wb = load_workbook('teste.xlsx')
plan = wb.active
plan['A1'] = 'Nº'
plan['B1'] = 'Nome'

wb.save('teste.xlsx')