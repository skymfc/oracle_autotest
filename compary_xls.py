#!/usr/bin/python
import xlwt
import xlrd
"""
compare the actually result and excepted result
label red if the result isn't same
"""

#step1: open file and get the value
#def read_xls(filepath,nRow):
   
#    return [nrows,table.cell(nRow,1).value]
def insert_excel(testcase_name,suc_count,dif_count,nRow):
    sheet.write(nRow,0,testcase_name)
    sheet.write(nRow,1,suc_count)
    sheet.write(nROw,2,dif_count)
def main():
    pattern=xlwt.Pattern()
    pattern.pattern=xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour=5
    style0=xlwt.XFStyle()
    style0.pattern=pattern
    #new file result
    book=xlwt.Workbook()
    sheet=book.add_sheet("sft_result",cell_overwrite_ok=True)
    sheet.write(0,0,"TESTNAME")
    sheet.write(0,1,"SUC")
    sheet.write(0,2,"DIF")   
    nRow=1
    #end
    filepath1="/home/oracle/sft_result/actuall_result.xls"
    filepath2="/home/oracle/sft_result/except_result.xls"
    data1=xlrd.open_workbook(filepath1)
    table1=data1.sheets()[0]
    data2=xlrd.open_workbook(filepath2)
    table2=data2.sheets()[0]
    N = table1.nrows
    for i in range(1,N):
        testcase_name=table1.cell(i,0).value
        count_suc1=int(table1.cell(i,1).value)
        count_suc2=int(table2.cell(i,1).value)
        count_dif=int(table1.cell(i,2).value)
        if count_suc1==count_suc2:
            insert_excel(testcase_name,count_suc1,count_dif)
        else:
            sheet.write(i,0,testcase_name,style0)
            sheet.write(i,1,count_suc1,style0)
            sheet.write(i,2,count_dif,style0)
    book.save("/home/oracle/sft_result/result_compare.xls")
            
        


if __name__ == '__main__':
    main()
    
