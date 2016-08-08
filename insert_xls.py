#!/usr/bin/python
import xlwt
import os
sft_work="/ocedb/oce/work/"
def insert_excel(testcase_name,suc_count,dif_count,nRow):
    sheet.write(nRow,0,testcase_name)
    sheet.write(nRow,1,suc_count)
    sheet.write(nRow,2,dif_count)
#get the suc and dif counts
def endWith(file_name,*endstring):
    array=map(file_name.endswith,endstring)
    if True in array:
        return True
    else:
        return False
    

def getcount(testcase_name):    
    current_path=sft_work+testcase_name+"/work/"   
    suc_count=0
    dif_count=0
    s=os.listdir(current_path)
    for i in s:
        if endWith(i,'.suc'):   
            suc_count=suc_count+1
        if endWith(i,'dif'):
            dif_count=dif_count+1
    return [suc_count,dif_count]   
if __name__ == '__main__':   
    book=xlwt.Workbook()
    sheet=book.add_sheet("sft_result",cell_overwrite_ok=True)
    sheet.write(0,0,"TESTNAME")
    sheet.write(0,1,"SUC")
    sheet.write(0,2,"DIF")   
    nRow=1
    for file in os.listdir(sft_work):
        if not file.startswith('.'):
            count=getcount(file)
            insert_excel(file,count[0],count[1],nRow)
            nRow=nRow+1
    
    print "insert finish"
    book.save("/home/oracle/sft_result/result_final.xls")
    