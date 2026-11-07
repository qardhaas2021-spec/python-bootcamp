# creating new excel files
# first importing openpyxl
# creating newworkbook object
# creating new sheet active
# writing sales as dict
# writing sheet header
# saving the workbook

import openpyxl
from openpyxl.styles import Font, PatternFill

wb = openpyxl.Workbook()

sheet = wb.active

sales = {2017: 70000, 2018: 80000, 2019: 90000, 2020: 95000}

sheet["A1"] = "Years"
sheet["B1"] = "sales"
sheet["C1"] = "Text"
sheet.column_dimensions["A"].width = 12
sheet["A1"].font = Font(bold=True)

green = PatternFill("solid", fgColor="92D050")
sheet["A1"].fill = green
sheet["B1"].fill = green
sheet["C1"].fill = green

for k, v in sales.items():

    sheet.append((k, v, v * 0.1))

wb.save("sales.xlsx")