import openpyxl as op #별칭
#워크북 만들기
wb = op.Workbook() 
print(wb)

#저장하기
wb.save("test.xlsx")

