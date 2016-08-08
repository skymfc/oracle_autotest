#!/usr/bin/python
'''
SFT test
'''
import xlwt
import os
list1=['sdbck','cssck']
list2=['lrgdbconsrto',  'lrgdbconsrtt', 'lrgdbcon7joo', 'lrgdbcon7jto', 'lrgnsglsn2',   'lrgnfps',  'lrg11a',   'lrg2b2',   'lrg2b3',   'lrgdbcon3a']
list3=['lrgdbcon3a1',   'lrg462',       'lrg463',       'lrg464',       'lrg4b3d',      'lrg4c7',   'lrg4d2',   'lrgdbcon4d3','lrgdbcon4d5','lrg4i2']
list4=['lrgdbcon61a5',  'lrg61b',   'lrgdbcon61f',  'lrgdbconb1',   'lrgdbconbc4',  'lrgdbconbc5',  'lrgdbcond1',   'lrgdbcond2',   'lrgdbcondie2','lrgdbcondie3']
list5=['lrgdig1','lrgdig2','lrgdbconfg1','lrgdbconfg1a','lrgdbconfg2','lrgdbconfg2a','lrgdbconfgb3','lrgdbconfgd3','lrgdbconfgd3a','lrgdbcong17']
list6=['lrgdbcong25','lrgimc','lrgimcscan','lrgimcsm','lrgimcspc01','lrgimctxn03','lrgdbconimccompft2','lrgdbconimcparam','lrgdbconimcsc','lrgdbconji2']
list7=['lrgdbconmm','lrgdbconnqma2','lrgnqmb','lrgdbcono1','lrgdbcono8','lrgdbconpd4','lrgdbconpkt1','lrgdbconpkt2','lrgdbconpkt3', 'lrgdbconpkt5']
list8=[ 'lrgdbconpq2', 'lrgdbconqs', 'lrgsm1', 'lrgsm1a' ,'lrgdbconsms' ,'lrgdbconsmsa' ,'lrgdbconsmsb','lrgsrg1' ,'lrgsrg2' 
,'lrgsrg3' ,'lrgsrg5' ,'lrgsrg6' ,'lrgstxm','lrgdbconzg2a',
 'lrgdbconzg2b' ,'lrgdbconzg4']

sft_bin_path="/ocedb/oce/bin/"
sft_logs="/home/oracle/sft_logs/"
sft_work="/ocedb/oce/work/"

def execute_command(testcase_name):
    command=sft_bin_path+"oceftcldriv.sh "+testcase_name+" > "+sft_logs+testcase_name+".log 2>&1"
#insert the result into new file
def insert_excel(testcase_name,suc_count,dif_count,nRow):
    sheet.write(nRow,0,testcase_name)
    sheet.write(nRow,1,suc_count)
    sheet.write(nROw,2,dif_count)
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
        if endWith(s,'.suc'):   
            suc_count=suc_count+1
        if endWith(s,'dif'):
            dif_count=dif_count+1
    return [suc_count,dif_count]   
        
    

if __name__ == '__main__':
    i=1
    book=xlwt.Workbook()
    sheet=book.add_sheet("sft_result")
    sheet.write(0,0,"TESTNAME")
    sheet.write(0,1,"SUC")
    sheet.write(0,2,"DIF")
    for test  in list1:
        print "This is the %d case %s"%(i,test) 
        execute_command(test)
    nRow=1
    for file in os.listdir(sft_work):
        if not file.startswith('.'):
            count=getcount(file)
            insert_excel(file,count[0],count[1],nRow)
            nRow=nRow+1
    
    print "insert finish"
    book.save("/home/oracle/sft_result/result.xls")
    


