import openpyxl
wb = openpyxl.load_workbook("my_products.xlsx")
sheet = wb["Products for sale"]

new_wb = openpyxl.Workbook()
new_sheet = new_wb.active
new_sheet['A1'] = 'Product'
new_sheet['B1'] = 'Units'
new_sheet['C1'] = 'Price'
new_sheet['D1'] = 'Total'

for row in range(2, 12):
    new_sheet[f"A{row}"] = sheet[f"B{row}"].value
    new_sheet[f"B{row}"] = sheet[f"C{row}"].value
    new_sheet[f"C{row}"] = sheet[f"D{row}"].value
    new_sheet[f"D{row}"] = f"=B{row}*C{row}"

new_sheet.column_dimensions['A'].width = 18

new_wb.save("report.xlsx")


