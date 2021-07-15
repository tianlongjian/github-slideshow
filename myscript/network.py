#!/usr/bin/python

import os
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
import xlrd

projectname="TINNO_SH_R0MP1_K65V1_64_BSP"
project="U536AF"
titleTMP="[TINNO]"+"[U536AF]"
discription="None"
swVersion="alps-mp-r0.mp1-V8.107.1"
modemProject="TK_MD_BASIC"
MDversion="MOLY.LR12A.R3.MP.V166"
finder="shaowei.wang"
phone="15201849368"
mail="shaowei.wang@tinno.com"
 

def getNetworkURL():
   
    inputnum=input("please input jira number")
    work =xlrd.open_workbook('mybug.xlsx')
    name=work.sheet_names()[0]
    print(name)
    sheet=work.sheet_by_name(name)
    print(sheet)
    nrows=sheet.nrows
    ncols=sheet.ncols
    print(ncols)
    print(nrows)
    #column=sheet.max_column
    #print(column)
    project1=0
    for i in range(nrows):
        print(i)
        
        if i==0:
            for j in range(ncols):
                if sheet.row_values(i)[j] == "项目":
                    project1=j
                    
                if sheet.row_values(i)[j] == "关键字":
                    keyword=j
                    print(keyword)
                    print(sheet.row_values(i)[keyword])  
                if sheet.row_values(i)[j] == "概要":
                    summ=j
                    print(summ)
                    print(sheet.row_values(i)[summ])
                if sheet.row_values(i)[j] == "状态":
                    status=j
                    print(status)
                    print(sheet.row_values(i)[status])
                if sheet.row_values(i)[j] == "已解决":
                    resovedtime=j
                    print(resovedtime)
                    print(sheet.row_values(i)[resovedtime])
                if sheet.row_values(i)[j] == "描述":
                    discription1=j
                    print(discription1)
                    print(sheet.row_values(i)[discription1])
        else:
            if sheet.row_values(i)[keyword]==inputnum:
                
                if sheet.row_values(i)[project1]=="U316AT":
                    projectname=r"TINNO_SH_R0MP1_K39TV1_BSP" 
                    project="U316AT"
                    titleTMP="[TINNO]"+"[U316AT]"
                    HWproject="80034"
                if sheet.row_values(i)[project1]=="U536AF":
                    projectname=r"TINNO_SH_R0MP1_K65V1_64_BSP"
                    project="U536AF"
                    titleTMP="[TINNO]"+"[U536AF]"   
                    HWproject="83437"
                title=titleTMP+sheet.row_values(i)[summ]
                print("title",title)
                discription=sheet.row_values(i)[discription1]
    #chromedriver = "C:\Program Files\Google\Chrome\Application"
    #os.environ["webdriver.ie.driver"] = chromedriver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches",["enable-logging"])
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options)
    #browser = webdriver.Chrome()
    
    browser.get("https://eservice.mediatek.com/eservice-portal/login")
    browser.maximize_window()
    browser.find_element_by_name('username').click() 
    browser.find_element_by_name('username').clear() 
    browser.find_element_by_name('username').send_keys('bin.liu@tinno.com') 

    browser.find_element_by_name('password').click() 
    browser.find_element_by_name('password').clear() 
    browser.find_element_by_name('password').send_keys('tinno222') 

    browser.find_element_by_id('submit_button').click() 
    time.sleep(4)
    
    browser.find_element_by_id('main_menu_issue_manager').click()
    browser.find_element_by_id('sub_menu_issue_manager').click()
    
    a=browser.find_element_by_class_name('btn.btn-sm.green').click()
    time.sleep(1)
    #browser.find_element_by_id('project_table_filter').click()
    browser.find_element_by_xpath("//div[@id='project_table_filter']/label[text()=\"Search:\"]").click()
    browser.find_element_by_xpath("//div[@id='project_table_filter']/label[text()=\"Search:\"]").send_keys(projectname)
    #browser.find_element_by_id('project_table_filter').send_keys('TINNO_SH_R0MP1_K65V1_64_BSP')
    time.sleep(2)
    browser.find_element_by_link_text(projectname).click()
    time.sleep(2)
    for one in  browser.window_handles:
        browser.switch_to.window(one)
        try:
            browser.find_element_by_id(r'306_2')
            newflag=True
        except:
            newflag=False
        
        if newflag:
            
            #title
            browser.find_element_by_id(r'306_2').click()
            browser.find_element_by_id('306_2').send_keys(title) 
            #HW Project             
            Select(browser.find_element_by_id('59305_221')).select_by_value(HWproject)
            #class
            Select(browser.find_element_by_id('273_4')).select_by_value('Bug')
            #prority
            Select(browser.find_element_by_id('177979_6')).select_by_value('1.High')
            #discription
            browser.find_element_by_id('280_3').click()
            browser.find_element_by_id('280_3').clear()
            browser.find_element_by_id('280_3').send_keys(discription)
            #browser.find_element_by_id('59305_221').send_keys(project) 
            #feature type
            Select(browser.find_element_by_id('18490_17')).select_by_value('SW')
            #feature 60170_176
            Select(browser.find_element_by_id('60170_176')).select_by_value('Network')
            #SW version
            browser.find_element_by_name('swVersion').click()
            browser.find_element_by_name('swVersion').send_keys(swVersion)
            #MD Project
            browser.find_element_by_name('modemProject').click()
            browser.find_element_by_name('modemProject').send_keys(modemProject)
            #MD version 33370_81
            browser.find_element_by_id('33370_81').click()
            browser.find_element_by_id('33370_81').send_keys(MDversion)
            #Country 20912_188
            Select(browser.find_element_by_id('20912_188')).select_by_value('American Samoa')
            #City 
            browser.find_element_by_id('20913_189').click()
            browser.find_element_by_id('20913_189').send_keys(r"N/A")
            #finder 
            browser.find_element_by_id('54010_32').click()
            browser.find_element_by_id('54010_32').send_keys(finder)
            #phone 
            browser.find_element_by_id('54011_33').click()
            browser.find_element_by_id('54011_33').send_keys(phone)
            #mail 
            browser.find_element_by_id('31690_34').click()
            browser.find_element_by_id('31690_34').send_keys(mail)
            
    print(a)