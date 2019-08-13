import os
import csv

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
            out.write(inputfile + ':' + rowoutput + '\n')
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
            out.write(inputfile + ':' + row[1] + '\n')
            out.close()
        pass
    pass
#csv_txtsymmap('symmapc.txt','/Users/huanjiaming/0727temp/')


#csv_txt('symmapc.txt','/Users/huanjiaming/0727temp/')

csv_csv('symmapc.csv','/Users/huanjiaming/0727temp/')