#!user/bin/python
#import requests
import random
import os
import re

list=["1","2","3","4","5","6","7","8","9","0"]
debuglog=1

def get_dir(logtag):
    #line = r'\'
    path =os.getcwd()
    #print (os.getcwd())
    a=os.listdir(path)
    if debuglog==1:
        print(a)
    
    #print(line)
    for word in a:
        if "AP" in word:
            current_logfile=word
            path2=os.path.join(path,current_logfile)
            #path+'\\'+current_logfile
            #print(word)
            #print("path,",path2)
            if current_logfile is not None: 
                a=os.listdir(path2)
                #print(a)
                for mainlog in a:
                    if logtag in mainlog:
                        mainlogfile=mainlog
                        mainlogfilepath=os.path.join(path2,mainlogfile)
                        print("----------------",logtag,"---------------")
                        #print(mainlogfile)
                        if debuglog==1:
                            print("mainlogfilepath,",mainlogfilepath)
                            
                        checklog(logtag,mainlogfilepath)
                        #print(file)


def checklog(logtag,logpath):
    file=open(logpath,encoding='utf-8',errors='ignore')
    pdnRej="MSG_ID_WRAP_IMSA_IMCB_PDN_ACT_REJ_RSP"
    VolteReg=r"VoLTE REG: *Reg"
    SipProcess=r"VoLTE SIPTX: [SIPTX-IO]"
    SIMplmn="[vendor.gsm.ril.uicc.mccmnc]"
    VilteSupport="[persist.vendor.mtk.vilte.enable]"
    VilteSupport2="[persist.vendor.vilte_support]"
    IsTestSim="[vendor.gsm.sim.ril.testsim]"
    sp2=None
    sp3=None
    for line in file.readlines():
        if logtag == "main":
            if pdnRej in line:
                #print(line)
                sm=re.findall("cause = (.*) ",line)
                print(pdnRej,"cause=",sm,"please check ims Apn")
            if VolteReg in line:
                #if "Registered" in line:
                sm2=re.findall("VoLTE REG:(.*), cause",line)
                if len(sm2) == 0:
                    sm2_1=re.findall("VoLTE REG:(.*)\(",line)
                    print("VoLTE REG",sm2_1)
                else:    
                    print("VoLTE REG",sm2)
            if SipProcess in line:
                #print(line)
                sm4=re.sub("\[\d+:\d+\]","",line)               
                sm3=re.findall("VoLTE SIPTX: \[SIPTX-IO\](.*)",sm4)
                #sm4=re.sub("\d+","",str(sm3))
                print("SIPProcess",sm3)
                #print(sm4)
        if logtag == "prop":  
            if SIMplmn in line:
                #print(line)
                sp1=re.findall(r"\[vendor.gsm.ril.uicc.mccmnc\]: \[(.*)\]",line)
                print("uicc_plmn",sp1)
            if VilteSupport in line:
                sp2=re.findall(r"\[persist.vendor.mtk.vilte.enable\]: \[(.)\]",line)
                print(VilteSupport,sp2)
            if VilteSupport2 in line:
                sp3=re.findall(r"\[persist.vendor.vilte_support\]: \[(.)\]",line)
                print(VilteSupport2,sp3)
            if IsTestSim in line:
                sp4=re.findall(r"\[vendor.gsm.sim.ril.testsim\]: \[(.)\]",line)
                print(IsTestSim,sp4)
    
    #print(logtag,sp2,sp3)
    if (logtag=="prop"):
        #print(logtag)
        #print(int(sp2[0]))
        if sp2 == ['0'] or sp3 ==['0']:
            print(sp2,sp3)
            print("vilte not support")
        else:
            print(VilteSupport,"is",sp2,VilteSupport2,"is",sp3)


if __name__ == '__main__':
   
    get_dir("prop")
    input("base infor list ,press entry key continue")
    get_dir("main")
    print("end")
    
    
   

     