import openpyxl

wb = openpyxl.load_workbook("my_products.xlsx", data_only=True)

print(wb.sheetnames)

for sheet in wb:
    print(sheet.title)

sheet = wb["Products"]
sheet = wb.active
b2_cell = sheet["B2"]
c2_cell = sheet["c2"]
c3_cell = sheet["E8"]
print(b2_cell.value, c2_cell.value, c3_cell.value)
print(sheet["A1"].value)
print(sheet["B1"].value)
print(sheet["D1"].value)
print(sheet["E1"].value)
print(sheet.cell(row=4, column=2).value)
print(c2_cell.row, c2_cell.column)
print(sheet["A5"].data_type)
print(sheet["B5"].data_type)
print(sheet["A5"].encoding)
print(sheet["B5"].parent)

print(dir(c2_cell))

cell_range = sheet["B2:C11"]
for product, price in cell_range:
    print(f"product: {product.value} price: {price.value}")

print(f"sheet dimensions: {sheet.dimensions}")
print(sheet.max_row, sheet.max_column)

for a, b, c, d, e in sheet[sheet.dimensions]:
    print(a.value, b.value, c.value, d.value, e.value)

for row in sheet.rows:
    for cell in row:
        print(f"{cell.value} ", end="")
    print("\n")

for row in sheet.values:
    print(row)