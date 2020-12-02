import xlwings as xw
app = xw.App(visible=True, add_book=False)
workbook = app.books.open(r'd:\example.xlsx')
worksheet = workbook.sheets['Sheet1']  # 选中工作表“Sheet1”
worksheet.range('A1').value = '编号'  # 在单元格A1中输入内容