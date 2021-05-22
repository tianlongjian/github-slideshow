#!user/bin/python
#import requests
import random


def random_test(list,b,num):
    l=list
    a=random.sample(l,3)
    num=num-1
    print("-------\n",a)
    print(num)
    if num==0:
        return
    for i in a:
        l.remove(i)
        
    if len(b):
        print(len(b))
        l.extend(b)
    else:
        print(len(b))
        print("else b =0")
        
    print(l)
    
    try:
        random_test(l,a,num)
    except:
        print("out")
    #print("****"+str(l))
        


if __name__ == '__main__':
   
    #list.append(a)
    
    list=["1","2","3","4","5","6","7","8","9","0"]
    print(list)
    b=[]
    num=100
    random_test(list,b,num)
    print(1111111)
    print(list)

        
    
   

     