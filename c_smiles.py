import os
import bs4
import requests
from urllib import request
import re
from selenium import webdriver
from time import sleep
import csv
from lxml import etree
import urllib.parse
import urllib.request
import ssl
from urllib.error import URLError, HTTPError, ContentTooShortError


def tcmspsmilenum(compoundnum):
    browsertcmsp = webdriver.Firefox()
    browsertcmsp.get('http://lsp.nwu.edu.cn/molecule.php?qn=' + compoundnum)
    scompoudnum = browsertcmsp.find_element_by_xpath('//*[@id="container_lsp"]/div[2]/table/thead/tr[1]/td')
    print(scompoudnum.text)
    scompoudname = browsertcmsp.find_element_by_xpath('//*[@id="container_lsp"]/div[2]/table/thead/tr[2]/td')
    print(scompoudname.text)
    pubchemid = browsertcmsp.find_element_by_xpath('//*[@id="container_lsp"]/div[2]/table/thead/tr[6]/td')
    print(pubchemid.text)
    casid = browsertcmsp.find_element_by_xpath('//*[@id="container_lsp"]/div[2]/table/thead/tr[7]/td')
    print(casid.text)

    tcmsppubmed = open('tcmsppubmed.txt','a+')
    tcmsppubmed.write(compoundnum + '$' + scompoudnum.text + '$' + scompoudname.text + '$' + pubchemid.text + '\n')
    tcmsppubmed.close()
    tcmspccas = open('tcmspcas.txt','a+')
    tcmspccas.write(compoundnum + '$' + scompoudnum.text + '$' + scompoudname.text + '$' + casid.text + '\n')
    tcmspccas.close()
    browsertcmsp.quit()
    pass

def tcmspsmilesnumzong(pathway):
    inputtcmspfile = csv.reader(open('tcmspcn.csv'))
    for row in inputtcmspfile:
        compoundnum = str(row).replace('[','').replace(']','').replace("'","")
        browsertcmsp = webdriver.Firefox()
        browsertcmsp.get('http://lsp.nwu.edu.cn/molecule.php?qn=' + compoundnum)
        scompoudnum = browsertcmsp.find_element_by_xpath('//*[@id="container_lsp"]/div[2]/table/thead/tr[1]/td')
        print(scompoudnum.text)
        scompoudname = browsertcmsp.find_element_by_xpath('//*[@id="container_lsp"]/div[2]/table/thead/tr[2]/td')
        print(scompoudname.text)
        pubchemid = browsertcmsp.find_element_by_xpath('//*[@id="container_lsp"]/div[2]/table/thead/tr[6]/td')
        print(pubchemid.text)
        casid = browsertcmsp.find_element_by_xpath('//*[@id="container_lsp"]/div[2]/table/thead/tr[7]/td')
        print(casid.text)
        tcmsppubmed = open('tcmsppubmed.txt','a+')
        tcmsppubmed.write(compoundnum + '$' + scompoudnum.text + '$' + scompoudname.text + '$' + pubchemid.text + '\n')
        tcmsppubmed.close()
        tcmspccas = open('tcmspcas.txt','a+')
        tcmspccas.write(compoundnum + '$' + scompoudnum.text + '$' + scompoudname.text + '$' + casid.text + '\n')
        tcmspccas.close()
        tcmspccasonly = open('tcmspcasonly.txt','a+')
        tcmspccasonly.write(casid.text + '\n')
        tcmspccasonly.close()
        browsertcmsp.quit()
        pass
    pass

def pubchem(num):
    context = ssl._create_unverified_context()
    pubchemnameurl = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/' + num + '/property/IUPACName/json'
    htmltpubchemname = request.urlopen(pubchemnameurl,context=context).read().decode('utf-8')
    iupacname = re.findall(r'"IUPACName": ".*?"',htmltpubchemname)
    print(iupacname)
    pubchemsmilesurl = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/' + num + '/property/CanonicalSMILES/json'
    htmltpubchemsmile = request.urlopen(pubchemsmilesurl,context=context).read().decode('utf-8')
    smile = re.findall(r'"CanonicalSMILES": ".*?"',htmltpubchemsmile)
    print(smile)
    count = len(iupacname)
    i = 0
    while i < count:
        print(iupacname[i])
        print(smile[i])
        spubchem = open('pubchemns.txt','a+')
        spubchem.write(num + '$' + iupacname[i] + '$'  + smile[i] + '$' + '\n')
        spubchem.close()
        i = i + 1
        print(i)
        pass
    pass

def pubchemzong(pathway):
    context = ssl._create_unverified_context()
    inputpubchemfile = csv.reader(open('pubchemnum.csv'))
    for row in inputpubchemfile:
        num = str(row).replace('[','').replace(']','').replace("'","")
        pubchemnameurl = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/' + num + '/property/IUPACName/json'
        print(pubchemnameurl)
        htmltpubchemname = request.urlopen(pubchemnameurl,context=context).read().decode('utf-8')
        iupacname = re.findall(r'"IUPACName": ".*?"',htmltpubchemname)
        print(iupacname)
        print(len(iupacname))
        pubchemsmilesurl = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/' + num + '/property/CanonicalSMILES/json'
        htmltpubchemsmile = request.urlopen(pubchemsmilesurl,context=context).read().decode('utf-8')
        smile = re.findall(r'"CanonicalSMILES": ".*?"',htmltpubchemsmile)
        print(smile)
        print(len(smile))
        count = len(iupacname)
        i = 0
        while i < count:
            print(iupacname[i])
            print(smile[i])
            spubchem = open('pubchemns.txt','a+')
            spubchem.write(num + '$' + iupacname[i] + '$'  + smile[i] + '$' + '\n')
            spubchem.close()
            i = i + 1
            print(i)
            pass  
        pass
    pass

def caspubchem(num):
    context = ssl._create_unverified_context()
    pubchemnameurl = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/' + num + '/property/IUPACName/json'
    htmltpubchemname = request.urlopen(pubchemnameurl,context=context).read().decode('utf-8')
    iupacname = re.findall(r'"IUPACName": ".*?"',htmltpubchemname)
    print(iupacname)
    pubchemsmilesurl = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/' + num + '/property/CanonicalSMILES/json'
    htmltpubchemsmile = request.urlopen(pubchemsmilesurl,context=context).read().decode('utf-8')
    smile = re.findall(r'"CanonicalSMILES": ".*?"',htmltpubchemsmile)
    print(smile)
    count = len(iupacname)
    i = 0
    while i < count:
        print(iupacname[i])
        print(smile[i])
        spubchem = open('caspubchemns.txt','a+')
        spubchem.write(num + '$' + iupacname[i] + '$'  + smile[i] + '$' + '\n')
        spubchem.close()
        i = i + 1
        print(i)
        pass  
    pass

def caspubchemzong(pathway):
    context = ssl._create_unverified_context()
    inputpubchemfile = csv.reader(open('caspubchemnum.csv'))
    for row in inputpubchemfile:
        num = str(row).replace('[','').replace(']','').replace("'","")
        try:
            pubchemnameurl = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/' + num + '/property/IUPACName/json'
            htmltpubchemname = request.urlopen(pubchemnameurl,context=context).read().decode('utf-8')
        except (URLError, HTTPError, ContentTooShortError) as e:
            print('Download error:', e)
            if hasattr(e, 'code') and 400 <= e.code < 500:
                continue
        else:
            iupacname = re.findall(r'"IUPACName": ".*?"',htmltpubchemname)
            print(iupacname)
            print(len(iupacname))
            pubchemsmilesurl = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/' + num + '/property/CanonicalSMILES/json'
            htmltpubchemsmile = request.urlopen(pubchemsmilesurl,context=context).read().decode('utf-8')
            smile = re.findall(r'"CanonicalSMILES": ".*?"',htmltpubchemsmile)
            print(smile)
            print(len(smile))
            count = len(iupacname)
            i = 0
            while i < count:
                print(iupacname[i])
                print(smile[i])
                spubchem = open('caspubchemns.txt','a+')
                spubchem.write(num + '$' + iupacname[i] + '$'  + smile[i] + '$' + '\n')
                spubchem.close()
                i = i + 1
                print(i)
                pass  
        pass
    pass

def pubchemwangyezong(pathway):
    inputpubchemfile = csv.reader(open('pubchemnum.csv'))
    for row in inputpubchemfile:
        num = str(row).replace('[','').replace(']','').replace("'","")
        try:
            try:
                pubchemnameurl = 'https://pubchem.ncbi.nlm.nih.gov/compound/' + num
                browserpubchem = webdriver.Firefox()
                browserpubchem.get('https://pubchem.ncbi.nlm.nih.gov/compound/' + num)
                sleep(10)
                outputname = browserpubchem.find_element_by_xpath('//*[@id="main-content"]/div/div/div[1]/div[2]')
                print(outputname.text)
                iupacname = browserpubchem.find_element_by_xpath('//*[@id="IUPAC-Name"]/div[2]/div[1]')
                print(iupacname.text)
                smile = browserpubchem.find_element_by_xpath('//*[@id="Canonical-SMILES"]/div[2]/div[1]')
                print(smile.text)
                spubchem = open('pubchemns.txt','a+')
                spubchem.write(outputname.text + '$' +num + '$' + iupacname.text + '$'  + smile.text + '$' + '\n')
                spubchem.close()
            except:
                browserpubchem.refresh()
                sleep(10)
                try:
                    outputname = browserpubchem.find_element_by_xpath('//*[@id="main-content"]/div/div/div[1]/div[2]')
                    print(outputname.text)
                    iupacname = browserpubchem.find_element_by_xpath('//*[@id="IUPAC-Name"]/div[2]/div[1]')
                    print(iupacname.text)
                    smile = browserpubchem.find_element_by_xpath('//*[@id="Canonical-SMILES"]/div[2]/div[1]')
                    print(smile.text)
                    spubchem = open('pubchemns.txt','a+')
                    spubchem.write(outputname.text + '$' +num + '$' + iupacname.text + '$'  + smile.text + '$' + '\n')
                    spubchem.close()
                except:
                    print(num)
                    pubchemerror = open('pubchemerror.txt','a+')
                    pubchemerror.write(num + '\n')
                    pubchemerror.close()
                    browserpubchem.close()
                    continue
                else:
                    browserpubchem.close()
            else:
                browserpubchem.close()
            pass
        except:
            print(num)
            pubchemerror = open('pubchemerror.txt','a+')
            pubchemerror.write(num + '\n')
            pubchemerror.close()
            browserpubchem.close()
            pass
        else:
            print('OK')
            pass
            
    pass

def caspubchemwangyezong(pathway):
    context = ssl._create_unverified_context()
    inputpubchemfile = csv.reader(open('caspubchemnum.csv'))
    for row in inputpubchemfile:
        try:
            num = str(row).replace('[','').replace(']','').replace("'","")
            browserpubchem = webdriver.Firefox()
            browserpubchem.get('https://pubchem.ncbi.nlm.nih.gov/#query=' + num)
            sleep(15)
            cascompoundurl =browserpubchem.find_element_by_xpath('//*[@id="collection-results-container"]/div/div/div[2]/ul/li/div/div/div[1]/div[2]/div[2]/div/span/a/span').text
            print(cascompoundurl)                                       
            scasurlpubchem = open('pubchemnscasurl.txt','a+')
            scasurlpubchem.write(num + '$' + cascompoundurl + '\n')
            scasurlpubchem.close()
        except:
            browserpubchem.refresh()
            sleep(15)
            try:
                cascompoundurl =browserpubchem.find_element_by_xpath('//*[@id="collection-results-container"]/div/div/div[2]/ul/li/div/div/div[1]/div[2]/div[2]/div/span/a/span').text
                scasurlpubchem = open('pubchemnscasurl.txt','a+')     
                scasurlpubchem.write(num + '$' + cascompoundurl + '\n')
                scasurlpubchem.close()
            except:
                print(num)
                pubchemerror = open('caspubchemerror.txt','a+')
                pubchemerror.write(num + '\n')
                pubchemerror.close()
                browserpubchem.close()
                continue
            else:
                browserpubchem.close()
        else:
            browserpubchem.close()
        
        
    pass


def caspubchemwangyezongzong(pathway):
    context = ssl._create_unverified_context()
    inputpubchemfile = csv.reader(open('caspubchemnum.csv'))
    for row in inputpubchemfile:
        try:
            num = str(row).replace('[','').replace(']','').replace("'","")
            browserpubchem = webdriver.Firefox()
            browserpubchem.get('https://pubchem.ncbi.nlm.nih.gov/#query=' + num)
            sleep(15)
            cascompoundurl =browserpubchem.find_element_by_xpath('//*[@id="collection-results-container"]/div/div/div[2]/ul/li/div/div/div/div[2]/div[1]/a').get_attribute('href')
            print(cascompoundurl)
            scasurlpubchem = open('pubchemnscasurl.txt','a+')
            scasurlpubchem.write(num + '$' + cascompoundurl + '\n')
            spuburlchem.close()
            browserpubchem.get(cascompoundurl)
            sleep(10)
            outputname = browserpubchem.find_element_by_xpath('//*[@id="main-content"]/div/div/div[1]/div[2]')
            print(outputname.text)
            iupacname = browserpubchem.find_element_by_xpath('//*[@id="IUPAC-Name"]/div[2]/div[1]')
            print(iupacname.text)
            smile = browserpubchem.find_element_by_xpath('//*[@id="Canonical-SMILES"]/div[2]/div[1]')
            print(smile.text)
            spubchem = open('pubchemns.txt','a+')
            spubchem.write(outputname.text + '$' +num + '$' + iupacname.text + '$'  + smile.text + '\n')
            spubchem.close()
        except:
            browserpubchem.refresh()
            sleep(15)
            try:
                cascompoundurl =browserpubchem.find_element_by_xpath('//*[@id="collection-results-container"]/div/div/div[2]/ul/li/div/div/div/div[2]/div[1]/a').get_attribute('href')
                scasurlpubchem = open('pubchemnscasurl.txt','a+')
                scasurlpubchem.write(num + '$' + cascompoundurl + '\n')
                spuburlchem.close()
                browserpubchem.get(cascompoundurl)
                sleep(10)
                outputname = browserpubchem.find_element_by_xpath('//*[@id="main-content"]/div/div/div[1]/div[2]')
                print(outputname.text)
                iupacname = browserpubchem.find_element_by_xpath('//*[@id="IUPAC-Name"]/div[2]/div[1]')
                print(iupacname.text)
                smile = browserpubchem.find_element_by_xpath('//*[@id="Canonical-SMILES"]/div[2]/div[1]')
                print(smile.text)
                spubchem = open('pubchemns.txt','a+')
                spubchem.write(outputname.text + '$' +num + '$' + iupacname.text + '$'  + smile.text  + '\n')
                spubchem.close()
            except:
                print(num)
                pubchemerror = open('pubchemerror.txt','a+')
                pubchemerror.write(num + '\n')
                pubchemerror.close()
                browserpubchem.close()
                continue
            else:
                browserpubchem.close()
        else:
            browserpubchem.close()
        
        
    pass

def ceshi(num):
    browserpubchem = webdriver.Firefox()
    browserpubchem.get('https://pubchem.ncbi.nlm.nih.gov/#query=' + num)
    sleep(15)
    cascompoundurl =browserpubchem.find_element_by_xpath('//*[@id="collection-results-container"]/div/div/div[2]/ul/li[1]/div/div/div/div[2]/div[1]/a').get_attribute('href')
    print(cascompoundurl)

    browserpubchem.get(cascompoundurl)
    sleep(10)
    outputname = browserpubchem.find_element_by_xpath('//*[@id="main-content"]/div/div/div[1]/div[2]')
    print(outputname.text)
    iupacname = browserpubchem.find_element_by_xpath('//*[@id="IUPAC-Name"]/div[2]/div[1]')
    print(iupacname.text)
    smile = browserpubchem.find_element_by_xpath('//*[@id="Canonical-SMILES"]/div[2]/div[1]')
    print(smile.text)
    spubchem = open('pubchemns.txt','a+')
    spubchem.write(outputname.text + '$' +num + '$' + iupacname.text + '$'  + smile.text + '\n')
    spubchem.close()
    pass



#tcmspsmilesnumzong('hhhhh')
#pubchem('3084331')
#pubchemzong('jfjfj')
pubchemwangyezong('12592')

#caspubchem('87-44-5')
#caspubchemzong('hhh')
#caspubchemwangyezong('hhhh')
#caspubchemwangyezongzong('fsf')

#ceshi('75718-12-6')
