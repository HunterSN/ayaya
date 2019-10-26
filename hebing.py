import os
import csv
import pandas
import openpyxl
import xlwt


def txt_txt(name,pathway):
    
    for inputfile in os.listdir(pathway):
        
        inputread = open(pathway + '/' + inputfile)       
        for row in inputread:
            #if inputread.line_num == 1:
            #    continue
            out = open(name,'a+')
            rowoutput = str(row)
            out.write(inputfile + '$' + rowoutput)
            out.close()
        pass
    pass

def txt_txt_single(name,pathway):
    
    for inputfile in os.listdir(pathway):
        
        inputread = open(pathway + '/' + inputfile)       
        for row in inputread:
            #if inputread.line_num == 1:
            #    continue
            out = open(name,'a+')
            rowoutput = str(row)
            out.write(rowoutput)
            out.close()
        pass
    pass


def csv_csv(name,pathway):
    
    for inputfile in os.listdir(pathway):
        
        inputread = csv.reader(open(pathway + '/' + inputfile))        
        for row in inputread:
            if inputread.line_num == 1:
                continue
            out = open(name,'a+')
            csv.writer(out).writerow(row)
            out.close()
        pass
    pass

def csv_txt(name,pathway):
    
    for inputfile in os.listdir(pathway):
        
        inputread = csv.reader(open(pathway + '/' + inputfile))        
        for row in inputread:
            if inputread.line_num == 1:
                continue
            out = open(name,'a+')
            rowoutput = str(row).replace('[','').replace(']','').replace("'","")
            out.write(inputfile + '$' + rowoutput + '\n')
            out.close()
        pass
    pass

def csv_txtsymmap(name,pathway):
    
    for inputfile in os.listdir(pathway):
        
        inputread = csv.reader(open(pathway + '/' + inputfile))        
        for row in inputread:
            if inputread.line_num == 1:
                continue
            out = open(name,'a+')
            #rowoutput = str(row).replace('[','').replace(']','').replace("'","")
            out.write(inputfile + '$' + row[1] + '\n')
            out.close()
        pass
    pass


def csv_xlsx(pathway):
    
    for inputfile in os.listdir(pathway):
        inputread = csv.reader(open(pathway + '/' + inputfile , encoding='GBK'))
        #print('1111111111111111' + inputfile)
        #csv = pandas.read_csv(inputread,encoding='GBK')
        #csv.to_excel(inputfile.replace('.','') + '.xlsx',sheet_name = 'data')
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('data')
        l = 0
        for row in inputread:
            print(row)
            
            #print(rowoutput)
            r = 0
            for i in row:
                print(i)
                rowoutput = str(i).replace('[','').replace(']','').replace("'","")
                sheet.write(l,r,rowoutput)
                r = r + 1
                pass
            l = l + 1   
        pass
        workbook.save(inputfile.replace('.','') + '.xls')
    pass



#csv_txtsymmap('symmapc.txt','/Users/huanjiaming/0727temp/')


#csv_txt('symmapc.txt','/Users/huanjiaming/0727temp/')

#csv_csv('symmapc.csv','/Users/huanjiaming/0727temp/')


#txt_txt_single('quanzhong.txt','/Users/huanjiaming/1013/')

csv_xlsx('/Users/huanjiaming/1025temp/')