#!/usr/bin/python
import time
import datetime
import test
import re

#def getcurrectweek():
week=time.strftime("%W")
#test.IsResovedBefore()
name=re.findall("W(\d+)","W11")

name2= re.sub("W","","W11")#filter(str.isdigit,"W11")
print("W"+str(int(name2)-1))
print(week)
print(datetime.datetime.now().isocalendar())