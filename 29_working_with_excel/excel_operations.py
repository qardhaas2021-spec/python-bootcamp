from turtle import title
import openpyxl
wb = openpyxl.load_workbook("my_products.xlsx")
# print(wb.sheetnames)

# sheet = wb["Products for sale"]

# print(dir(sheet))

# # sheet.title = "Products for sale"

# print(sheet.title)

# print(sheet.sheet_format)

# print(sheet.sheet_properties)

# adding new sheet to the workbook

# wb.create_sheet("Turnover1", 0)

# Removing sheet from work book

# sheet1 = wb["Turnover1"]
# wb.remove(sheet1)

# copy sheet in the same work book

source = wb["Turnover"]
destination = wb.copy_worksheet(source)
print(destination.title)


wb.save("my_products.xlsx")