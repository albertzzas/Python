#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/21 12:30
# @Author  : Albert
# @Site    : 
# @File    : textsplit.py
# @Software: PyCharm Community Edition
# @Import lib

# @Declare   :
# @Class Body  :
# @Execute   :


#############
#20170921

#powershell  export AD infor  OU CN DC


import re
import Txt_Data

##############
lastlist=[]
ADinforlist=[]




def readfile():

    Data_Path=r"C:\Albert_zz\KB_automation\Regex\ArlaRegex\Data_ADinfor.txt"


    F=Txt_Data.Get_F(Data_Path)
    lines = F.readlines()
    return lines

# print(lines[0])
# print(lines[1])
# one row for AD information
def oneADrowinfor():
    # 1 split ADfor by condition """
    #$results += get-adgroup -Identity  $groupsamaccountname -Properties  ManagedBy, samaccountname
    a=lines[1].split('"')
    # print(a)
    # print()
    # print(a[7])

    b=a[7]
    # print(b)

    c=b.split(",")
    # print(c)

    print(c[0])

    #regex the min article particle

    search=r'CN=(.*)'
    text=c[0]
    managedbyregex=re.compile(search)
    mo=managedbyregex.search(text)
    print(mo)
    print(mo.group(1))
    return mo.group(1)
# oneADrowinfor()
#!!!need to modify index very time, if change the powershell command perperoties

j=0
#todo
def onewordispose(onetext):
 #!! 写的有问题
    global j #要使用全局变量前 要声明下！！！！！！！！！
    try:
        a=onetext.split('"')
        b = a[7]
        c = b.split(",")
        # print(c[0])
        search = r'CN=(.*)'
        text = c[0]
        managedbyregex = re.compile(search)
        mo = managedbyregex.search(text)
        # print(mo)
        # print(mo.group(1))
        lastlist.append(mo.group(1))
        # print(lastlist)
    except:
        lastlist.append('item %d'% j)
        j+=1
        pass

    return lastlist

####################

def realADfile_way1(lines):
    #split to the mininum particle
    i=0
    for line in lines:
        i+=1
        ADinforlist=onewordispose(line)
        print(ADinforlist)
        # print(i)
    return ADinforlist


def  list_writefile(result):
    fp = open("result.txt", 'w')

    for result in result:
        fp.write(str(result)+'\n')
        # print(result)


lines=readfile()
# realADfile_way1(lines)

result=realADfile_way1(lines)
list_writefile(result)
