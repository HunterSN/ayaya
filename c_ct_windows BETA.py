import os
import bs4
import requests
from urllib import request
import re
from selenium import webdriver
from time import sleep
import csv
from lxml import etree



def tcmsp(herb):
    browsertcmsp = webdriver.Firefox()
    browsertcmsp.get('http://lsp.nwu.edu.cn/tcmsp.php')
    name = browsertcmsp.find_element_by_id('inputVarTcm')
    name.send_keys(herb)
    buttons = browsertcmsp.find_element_by_id('searchBtTcm')
    buttons.click()
    herbname = browsertcmsp.find_element_by_tag_name('td')
    sherbname = herbname.text
    xpath_url = '//*[@id="grid"]/div[2]/table/tbody/tr/td[3]/a'
    tcmspurl = browsertcmsp.find_element_by_xpath(xpath_url).get_attribute('href')
    browsertcmsp.quit()
    outct = sherbname +' '+ 'tcmspct.txt'
    outc = sherbname +' ' + 'tcmspc.txt'
    htmltcmsp = request.urlopen(tcmspurl).read().decode('utf-8')
    #print(htmltcmsp)
    co = re.findall(r'"molecule_name":".*?","ob"',htmltcmsp)
    ct = re.findall(r'"MOL_ID":".*?","molecule_name":".*?","target_name":".*?","target_ID":".*?"',htmltcmsp)
    ctc = str(len(ct))
    coc = str(len(co))
    print(herb + ':' + sherbname + ':' + coc)
    print(herb + ':' + sherbname + ':' + ctc)

    tcmspct = open(outct,'w+')
    for temptcmsp in ct:
        tcmspct.write(herb + ':' + sherbname + ':' + 'tcmsp' + ':' + str(temptcmsp)+'\n')
        pass
    tcmspct.close()

    tcmspc = open(outc,'w+')
    for temptcmspc in co:
        tcmspc.write(herb + ':' + sherbname + ':'  + 'tcmsp' + ':' + str(temptcmspc)+'\n')
        pass
    tcmspc.close()
    pass

def tcmsplianjie(herb,tcmspurl):
    htmltcmsp = request.urlopen(tcmspurl).read().decode('utf-8')
    #print(htmltcmsp)
    co = re.findall(r'"molecule_name":".*?","ob"',htmltcmsp)
    ct = re.findall(r'"MOL_ID":".*?","molecule_name":".*?","target_name":".*?","target_ID":".*?"',htmltcmsp)
    ctc = str(len(ct))
    coc = str(len(co))
    print(herb + ':' + ':' + coc)
    print(herb + ':' + ':' + ctc)
    outct = herb +' '+ 'tcmspct.txt'
    outc = herb +' ' + 'tcmspc.txt'
    tcmspct = open(outct,'w+')
    for temptcmsp in ct:
        tcmspct.write(herb + ':' + 'tcmsp' + ':' + str(temptcmsp)+'\n')
        pass
    tcmspct.close()

    tcmspc = open(outc,'w+')
    for temptcmspc in co:
        tcmspc.write(herb + ':' + 'tcmsp' + ':' + str(temptcmspc)+'\n')
        pass
    tcmspc.close()
    pass

def tcmspzong(herbs):
    for herb in herbs:
        browsertcmsp = webdriver.Firefox()
        browsertcmsp.get('http://lsp.nwu.edu.cn/tcmsp.php')
        name = browsertcmsp.find_element_by_id('inputVarTcm')
        name.send_keys(herb)
        buttons = browsertcmsp.find_element_by_id('searchBtTcm')
        buttons.click()
        herbname = browsertcmsp.find_element_by_tag_name('td')
        sherbname = herbname.text
        xpath_url = '//*[@id="grid"]/div[2]/table/tbody/tr/td[3]/a'
        tcmspurl = browsertcmsp.find_element_by_xpath(xpath_url).get_attribute('href')
        browsertcmsp.quit()
        htmltcmsp = request.urlopen(tcmspurl).read().decode('utf-8')
        #print(htmltcmsp)
        co = re.findall(r'"molecule_name":".*?","ob"',htmltcmsp)
        ct = re.findall(r'"MOL_ID":".*?","molecule_name":".*?","target_name":".*?","target_ID":".*?"',htmltcmsp)
        ctc = str(len(ct))
        coc = str(len(co))
        print(herb + ':' + sherbname + ':' + coc)
        print(herb + ':' + sherbname + ':' + ctc)
        
        outtcmsp = open('outsearchtcmsp.txt','a+')
        outtcmsp.write(herb + ',' + sherbname + ',' + "compounds" + coc + ',' + "compound-targets" + ctc + '\n')
        outtcmsp.close()


        tcmspct = open('tcmspct.txt','a+')
        for temptcmsp in ct:
            tcmspct.write(herb + ':' + sherbname + ':' + 'tcmsp' + ':' + str(temptcmsp)+'\n')
            pass
        tcmspct.close()

        tcmspc = open('tcmspc.txt','a+')
        for temptcmspc in co:
            tcmspc.write(herb + ':' + sherbname + ':' + 'tcmsp' + ':' + str(temptcmspc)+'\n')
            pass
        tcmspc.close()
        pass


    pass
    
def symmap(herb,pathway,pathway2):
    profile = webdriver.FirefoxProfile()
    profile.set_preference('browser.download.dir', pathway2)
    profile.set_preference('browser.download.folderList', 2)
    profile.set_preference('browser.download.manager.showWhenStarting', False)
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
    browsersymmap = webdriver.Firefox(firefox_profile=profile)

    browsersymmap.get('http://www.symmap.org/search/')
    name = browsersymmap.find_element_by_id('herb_ipt')
    name.send_keys(herb)
    buttons = browsersymmap.find_element_by_id('herb_search')
    #buttons = browsersymmap.find_element_by_xpath('//*[@id="herb_ser_box"]/span')
    buttons.click()
    compoundnum = browsersymmap.find_element_by_tag_name('td')
    compoundnumsymmap = compoundnum.text
    symmapurl = 'http://www.symmap.org/detail/' + compoundnumsymmap
    browsersymmap.get(symmapurl)
    herbname = browsersymmap.find_element_by_xpath('/html/body/div/section/div/div/div/div[1]/table/tbody/tr[1]/td[2]')
    sherbname = herbname.text
    print(sherbname)
    xiala = browsersymmap.find_element_by_xpath('/html/body/div/section/div/div/div/div[3]/div[2]/form/div/div[1]/div/button/span[2]/span').click()
    ingredientbuttonurl = '/html/body/div/section/div/div/div/div[3]/div[2]/form/div/div[1]/div/div/ul/li[3]/a'
    ingredientbuttonurlcilck = browsersymmap.find_element_by_xpath(ingredientbuttonurl).click()
    downloadcompoudbutton = browsersymmap.find_element_by_id('dl-btn').click()
    oldname=pathway + '/data.csv'  
    newname=pathway + '/' + 'A' + sherbname + ' ' + 'symmap.csv'
    os.rename(oldname,newname)   
    
    herbfile = open('A' + sherbname + ' ' + 'symmap.csv')
    herbreader = csv.reader(herbfile)
    for row in herbreader:
        if herbreader.line_num == 1:
            continue
        compoundnum = row[0]
        compoundname = row[1]
        compoundssurl = 'http://www.symmap.org/detail/' + compoundnum
        browsersymmap.get(compoundssurl)
        compoundssearchname = browsersymmap.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div[1]/table/tbody/tr[1]/td[2]')
        compoundsname = compoundssearchname.text
        comoundxiala = browsersymmap.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div[3]/div[2]/form/div/div[1]/div/button').click()
        targesbuttonurlclick = '/html/body/div[1]/section/div/div/div/div[3]/div[2]/form/div/div[1]/div/div/ul/li[4]/a'
        targetsbutton = browsersymmap.find_element_by_xpath(targesbuttonurlclick).click()
        targetdownloadbutton = browsersymmap.find_element_by_id('dl-btn').click()
        compoundoldname=pathway + '/data.csv' 
        compoundnewname=pathway + '/' + sherbname + ' ' + compoundname  + ' ' + 'symmap.csv'
        os.rename(compoundoldname,compoundnewname) 
        targetfile = open(sherbname + ' ' + compoundname  + ' ' + 'symmap.csv')
        targetreader = csv.reader(targetfile)
        for targetrow in targetreader:
            if targetreader.line_num == 1:
                continue
            symmapct = open('symmapct.txt','a+')
            symmapct.write(herb + ':' + sherbname + ':' + 'symmap' + ':' + compoundname + ':' + targetrow[1] + ':' + targetrow[3] + ':' + targetrow[6]+'\n')
            symmapct.close()
            pass
        pass
    browsersymmap.quit()
    pass

def symmapzong(herbs,pathway,pathway2):
    for herb in herbs:
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.dir', pathway2)
        profile.set_preference('browser.download.folderList', 2)
        #profile.set_preference('browser.download.dir', pathway + '/')
        #profile.set_preference('browser.download.dir', 'E:/wlylxxx')
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
        browsersymmap = webdriver.Firefox(firefox_profile=profile)

        browsersymmap.get('http://www.symmap.org/search/')
        name = browsersymmap.find_element_by_id('herb_ipt')
        name.send_keys(herb)
        buttons = browsersymmap.find_element_by_id('herb_search')
        #buttons = browsersymmap.find_element_by_xpath('//*[@id="herb_ser_box"]/span')
        buttons.click()
        compoundnum = browsersymmap.find_element_by_tag_name('td')
        compoundnumsymmap = compoundnum.text
        symmapurl = 'http://www.symmap.org/detail/' + compoundnumsymmap
        browsersymmap.get(symmapurl)
        herbname = browsersymmap.find_element_by_xpath('/html/body/div/section/div/div/div/div[1]/table/tbody/tr[1]/td[2]')
        sherbname = herbname.text
        print(sherbname)
        xiala = browsersymmap.find_element_by_xpath('/html/body/div/section/div/div/div/div[3]/div[2]/form/div/div[1]/div/button/span[2]/span').click()
        ingredientbuttonurl = '/html/body/div/section/div/div/div/div[3]/div[2]/form/div/div[1]/div/div/ul/li[3]/a'
        ingredientbuttonurlcilck = browsersymmap.find_element_by_xpath(ingredientbuttonurl).click()
        downloadcompoudbutton = browsersymmap.find_element_by_id('dl-btn').click()
        oldname=pathway + '/data.csv'
        newname=pathway + '/' + 'A' + sherbname + ' ' + 'symmap.csv'
        os.rename(oldname,newname)   
    
        herbfile = open('A' + sherbname + ' ' + 'symmap.csv')
        herbreader = csv.reader(herbfile)
        for row in herbreader:
            if herbreader.line_num == 1:
                continue
            compoundnum = row[0]
            compoundname = row[1]
            compoundssurl = 'http://www.symmap.org/detail/' + compoundnum
            browsersymmap.get(compoundssurl)
            compoundssearchname = browsersymmap.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div[1]/table/tbody/tr[1]/td[2]')
            compoundsname = compoundssearchname.text
            comoundxiala = browsersymmap.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div[3]/div[2]/form/div/div[1]/div/button').click()
            targesbuttonurlclick = '/html/body/div[1]/section/div/div/div/div[3]/div[2]/form/div/div[1]/div/div/ul/li[4]/a'
            targetsbutton = browsersymmap.find_element_by_xpath(targesbuttonurlclick).click()
            targetdownloadbutton = browsersymmap.find_element_by_id('dl-btn').click()
            compoundoldname=pathway + '/data.csv'  
            compoundnewname=pathway + '/' + sherbname + ' ' + compoundname  + ' ' + 'symmap.csv'
            os.rename(compoundoldname,compoundnewname) 
            targetfile = open(sherbname + ' ' + compoundname  + ' ' + 'symmap.csv')
            targetreader = csv.reader(targetfile)
            for targetrow in targetreader:
                if targetreader.line_num == 1:
                    continue
                symmapct = open('symmapct.txt','a+')
                symmapct.write(herb + ':' + sherbname + ':' + 'symmap' + ':' + compoundname + ':' + targetrow[1] + ':' + targetrow[3] + ':' + targetrow[6]+'\n')
                symmapct.close()
                
                pass
            pass
        browsersymmap.quit()
    pass

def etcm(herb):
    etcmurl = 'http://www.nrc.ac.cn:9090/ETCM/index.php/Home/Index/Prescriptions_All/getType/yc/searchTerm/' + herb +'.html'
    browseretcm = webdriver.Firefox()
    browseretcm.get(etcmurl)
    compoundclick = browseretcm.find_element_by_xpath('//*[@id="reportTable"]/tbody/tr[1]/td[2]/a').get_attribute('href')
    browseretcm.get(compoundclick)
    setcmherb =  browseretcm.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]/div').text
    print(setcmherb)
    compoundsurl = browseretcm.find_elements_by_xpath('//*[@id="table"]/tbody/tr[12]/td[2]/div/a')
    for url in compoundsurl:
        writeurl = open(herb + 'compoundsurl ectm.csv','a+')
        writeurl.write(url.get_attribute('href') + '\n')
        writeurl.close()
        pass
    
    compoundurlectmfile = open(herb + 'compoundsurl ectm.csv')
    compoundurlectm  = csv.reader(compoundurlectmfile)
    for compound in compoundurlectm:
        browseretcm.get(str(compound).replace('[','').replace(']','').replace("'",""))
        compoundname = browseretcm.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]/div').text
        print(compoundname)
        compoundetcm = open(setcmherb + ' ' + 'etcmc.txt','a+')
        compoundetcm.write(herb + ':' + setcmherb + ':' + 'etcm' + ':' + compoundname + '\n')
        compoundetcm.close()

        targetsname = browseretcm.find_elements_by_xpath('//*[@id="table"]/tbody/tr[26]/td[2]/div/a')
        for target in targetsname:
            targetname = target.text
            print(targetname)
            targetetcm = open(setcmherb + ' ' + 'etcmct.txt','a+')
            targetetcm.write(herb + ':' + setcmherb + ':' + 'etcm' + ':' + compoundname + ':' + targetname + '\n')
            targetetcm.close()
            pass
        pass
    browseretcm.quit()

def etcmzong(herbs):
    for herb in herbs:
        etcmurl = 'http://www.nrc.ac.cn:9090/ETCM/index.php/Home/Index/Prescriptions_All/getType/yc/searchTerm/' + herb +'.html'
        browseretcm = webdriver.Firefox()
        browseretcm.get(etcmurl)
        compoundclick = browseretcm.find_element_by_xpath('//*[@id="reportTable"]/tbody/tr[1]/td[2]/a').get_attribute('href')
        browseretcm.get(compoundclick)
        setcmherb =  browseretcm.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]/div').text
        print(setcmherb)
        compoundsurl = browseretcm.find_elements_by_xpath('//*[@id="table"]/tbody/tr[12]/td[2]/div/a')
        for url in compoundsurl:
            writeurl = open(herb + 'compoundsurl ectm.csv','a+')
            writeurl.write(url.get_attribute('href') + '\n')
            writeurl.close()
            pass
    
        compoundurlectmfile = open(herb + 'compoundsurl ectm.csv')
        compoundurlectm  = csv.reader(compoundurlectmfile)
        for compound in compoundurlectm:
            browseretcm.get(str(compound).replace('[','').replace(']','').replace("'",""))
            compoundname = browseretcm.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]/div').text
            print(compoundname)
            compoundetcm = open(setcmherb + ' ' + 'etcmc.txt','a+')
            compoundetcm.write(herb + ':' + setcmherb + ':' + 'etcm' + ':' + compoundname + '\n')
            compoundetcm.close()
            compoundzongetcm = open('etcmc.txt','a+')
            compoundzongetcm.write(herb + ':' + setcmherb + ':' + 'etcm' + ':' + compoundname + '\n')
            compoundzongetcm.close()

            targetsname = browseretcm.find_elements_by_xpath('//*[@id="table"]/tbody/tr[26]/td[2]/div/a')
            for target in targetsname:
                targetname = target.text
                print(targetname)
                targetetcm = open(setcmherb + ' ' + 'etcmct.txt','a+')
                targetetcm.write(herb + ':' + setcmherb + ':' + 'etcm' + ':' + compoundname + ':' + targetname + '\n')
                targetetcm.close()
                targetezongtcm = open('etcmct.txt','a+')
                targetezongtcm.write(herb + ':' + setcmherb + ':' + 'etcm' + ':' + compoundname + ':' + targetname + '\n')
                targetezongtcm.close()
                pass
            pass
        browseretcm.quit()
        pass
    pass

def etcmlianjie(herb,herburl):
    browseretcm = webdriver.Firefox()
    browseretcm.get(herburl)
    setcmherb =  browseretcm.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]/div').text
    print(setcmherb)
    compoundsurl = browseretcm.find_elements_by_xpath('//*[@id="table"]/tbody/tr[12]/td[2]/div/a')
    for url in compoundsurl:
        writeurl = open(herb + 'compoundsurl ectm.csv','a+')
        writeurl.write(url.get_attribute('href') + '\n')
        writeurl.close()
        pass
    
    compoundurlectmfile = open(herb + 'compoundsurl ectm.csv')
    compoundurlectm  = csv.reader(compoundurlectmfile)
    for compound in compoundurlectm:
        browseretcm.get(str(compound).replace('[','').replace(']','').replace("'",""))
        compoundname = browseretcm.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]/div').text
        print(compoundname)
        compoundetcm = open(setcmherb + ' ' + 'etcmc.txt','a+')
        compoundetcm.write(herb + ':' + setcmherb + ':' + 'etcm' + ':' + compoundname + '\n')
        compoundetcm.close()

        targetsname = browseretcm.find_elements_by_xpath('//*[@id="table"]/tbody/tr[26]/td[2]/div/a')
        for target in targetsname:
            targetname = target.text
            print(targetname)
            targetetcm = open(setcmherb + ' ' + 'etcmct.txt','a+')
            targetetcm.write(herb + ':' + setcmherb + ':' + 'etcm' + ':' + compoundname + ':' + targetname + '\n')
            targetetcm.close()
            pass
        pass
    browseretcm.quit()
    pass

shuzu = 'zexie','huzhang'

etcmshuzu ='ZE+XIE','HU+ZHANG'


tcmspzong(shuzu)

etcmzong(etcmshuzu)


symmapzong(shuzu,'E:/wlylxxx','e:\\wlylxxx') #前一个是文件所在位置，后一个是下载位置，只有格式不同

