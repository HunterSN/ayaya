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


def uniprot(compount):
    browseruniprot = webdriver.Firefox()
    uniproturl = 'https://www.uniprot.org/uniprot/?query=' + compount +'&fil=organism%3A%22Homo+sapiens+%28Human%29+%5B9606%5D%22&sort=score'
    browseruniprot.get(uniproturl)
    target = browseruniprot.find_element_by_xpath('//*[@class=" entry selected-row"]/td[2]/a')
    stargetnum = target.text
    targetname = browseruniprot.find_element_by_xpath('//*[@class=" entry selected-row"]/td[3]')
    stargetname = targetname.text
    proteinname = browseruniprot.find_element_by_xpath('//*[@class=" entry selected-row"]/td[5]/div/div[1]').get_attribute('title')
    sproteinname = proteinname
    genename = browseruniprot.find_element_by_xpath('//*[@class=" entry selected-row"]/td[6]/div')
    sgenename = genename.text
    print(stargetnum)
    print(stargetname)
    print(sproteinname)
    print(sgenename)
    
    uniprotfile = open('uniprotct.txt','a+')
    uniprotfile.write(stargetnum + '$' + stargetname + '$' + sproteinname + '$' + sgenename + '\n')
    uniprotfile.close()

    otarget = browseruniprot.find_elements_by_xpath('//*[@class=" entry"]/td[2]/a')
    sotargetnum = otarget
    otargetname = browseruniprot.find_elements_by_xpath('//*[@class=" entry"]/td[3]')
    sotargetname = otargetname
    oproteinname = browseruniprot.find_elements_by_xpath('//*[@class=" entry"]/td[5]/div/div[1]')
    soproteinname = oproteinname
    ogenename = browseruniprot.find_elements_by_xpath('//*[@class=" entry"]/td[6]/div')
    sogenename = ogenename
    count = len(otarget)
    print(count)
    i = 0
    while i < count:
        print(sotargetnum[i].text)
        print(sotargetname[i].text)
        print(soproteinname[i].get_attribute('title'))
        print(sogenename[i].text)
        uniprotfile = open('uniprotct.txt','a+')
        uniprotfile.write(sotargetnum[i].text + '$' + sotargetname[i].text + '$' + soproteinname[i].get_attribute('title') + '$' + sogenename[i].text + '\n')
        uniprotfile.close()
        i = i + 1
        pass
    browseruniprot.close()
    pass

def uniprotzong(csvfilepathway):
    inputuniportfile = csv.reader(open('proteinname.csv'))
    for row in inputuniportfile:
        compount = str(row).replace('[','').replace(']','').replace("'","").replace('"','')
        browseruniprot = webdriver.Firefox()
        uniproturl = 'https://www.uniprot.org/uniprot/?query=' + compount +'&fil=organism%3A%22Homo+sapiens+%28Human%29+%5B9606%5D%22&sort=score'
        browseruniprot.get(uniproturl)
        try:
            target = browseruniprot.find_element_by_xpath('//*[@class=" entry selected-row"]/td[2]/a')
            stargetnum = target.text
            targetname = browseruniprot.find_element_by_xpath('//*[@class=" entry selected-row"]/td[3]')
            stargetname = targetname.text
            proteinname = browseruniprot.find_element_by_xpath('//*[@class=" entry selected-row"]/td[5]/div/div[1]').get_attribute('title')
            sproteinname = proteinname
            genename = browseruniprot.find_element_by_xpath('//*[@class=" entry selected-row"]/td[6]/div')
            sgenename = genename.text
            print(stargetnum)
            print(stargetname)
            print(sproteinname)
            print(sgenename)
    
            uniprotfile = open('uniprotct.txt','a+')
            uniprotfile.write(stargetnum + '$' + stargetname + '$' + sproteinname + '$' + sgenename + '\n')
            uniprotfile.close()

            otarget = browseruniprot.find_elements_by_xpath('//*[@class=" entry"]/td[2]/a')
            sotargetnum = otarget
            otargetname = browseruniprot.find_elements_by_xpath('//*[@class=" entry"]/td[3]')
            sotargetname = otargetname
            oproteinname = browseruniprot.find_elements_by_xpath('//*[@class=" entry"]/td[5]/div/div[1]')
            soproteinname = oproteinname
            ogenename = browseruniprot.find_elements_by_xpath('//*[@class=" entry"]/td[6]/div')
            sogenename = ogenename
            count = len(ogenename)
            print(count)
            i = 0
            while i < count:
                print(sotargetnum[i].text)
                print(sotargetname[i].text)
                print(soproteinname[i].get_attribute('title'))
                print(sogenename[i].text)
                uniprotfile = open('uniprotct.txt','a+')
                uniprotfile.write(sotargetnum[i].text + '$' + sotargetname[i].text + '$' + soproteinname[i].get_attribute('title') + '$' + sogenename[i].text + '\n')
                uniprotfile.close()
                i = i + 1
                print(i)
                pass
        except:
            inputcom = browseruniprot.find_element_by_xpath('//*[@id="query"]').get_attribute('value')
            print(inputcom)
            uniproterror = open('uniprotcterror.txt','a+')
            uniproterror.write(compount + '$' + inputcom + '\n')
            uniproterror.close()
            browseruniprot.close()
            continue
        else:
            browseruniprot.close()
        pass
    pass



uniprotzong('jjjx')

#uniprot('Mediator of RNA polymerase II transcription subunit 17')