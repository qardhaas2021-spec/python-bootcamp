import openpyxl
from openpyxl.styles import Font, PatternFill, colors

wb = openpyxl.load_workbook("my_products.xlsx")
sheet = wb.active

my_cell = sheet["B4"]

font = Font(name="Tahoma", size=16, color=colors.BLACK, bold=True, italic=True, strike=False)
my_cell.font = font

fill = PatternFill(fill_type="solid", fgColor="FFFF00")
my_cell.fill = fill

# print(dir(openpyxl.styles))

wb.save("my_products.xlsx")

