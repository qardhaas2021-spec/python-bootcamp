import openpyxl

wb = openpyxl.load_workbook("my_products.xlsx")
sheet = wb.active

for c, d, e in sheet["c2:e11"]:
    e.value = f"={c.value}*{d.value}"


wb.save("my_products.xlsx")