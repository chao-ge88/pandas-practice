import xlwings as xw
app = xw.App(visible=True, add_book=False)
workbook = app.books.add()
worksheet = workbook.sheets.add('产品统计表')
worksheet.range('A1').value = '编号'
workbook.save(r'D:\pyCh\pythonProject1\北京.xlsx')
workbook.close()
app.quit()