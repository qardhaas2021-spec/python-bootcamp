import openpyxl

wb = openpyxl.load_workbook('my_products.xlsx')

sheet = wb.active

# sheet['C5'] = 40
# sheet['D2'] = 400
# new_product = [11, 'taplet', 12, 600, 12 * 600]
# sheet.append(new_product)
# wb.save('my_products.xlsx')

for c, d, e in sheet["C2:E11"]:
    e.value = c.value * d.value

wb.save('my_products.xlsx')