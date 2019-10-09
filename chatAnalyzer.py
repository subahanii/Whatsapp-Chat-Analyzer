"""
Author : Ghulam Mohiyuddin
What is this: This is a whatsapp group/indivisual chat analyser 
Message: This is not a final wait for more functionality
"""

import os
import re
import pandas as pd
import matplotlib as plt
link="C:\\Users\\asus\\Downloads\\WhatsApp Chat with EE Batch 2019.txt"# FILE LOCATION
tit=link.split("\\")
title=tit[-1]
title1=title[:len(title)-4:]
print(title1)
cht=open(link,encoding="utf8")
ar=[]
c=0
c1=0
def startsWithDate(s):
    pattern = "^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)(\d{2}|\d{4}), ([0-9][0-9]|[0-9]):([0-9][0-9])"
    result = re.match(pattern, s)
    if result:
        return True
    return False

def startsWithAuthor(s):

    cout=0
    l=0
    st=s.index("-")
  
    for i in range(len(s)):
        if s[i]==':':
            cout+=1
        if cout==2:
            l=i
            break
    
    return s[st+2:l] 
c2=0
f=0
while  cht.readline():
    rd=cht.readline()
    #print(rd)
    c1+=1
    if startsWithDate(str(rd)):
        splitLine=rd.split("-")
        dateTime=splitLine[0]
        #print(dateTime)
        date,time=dateTime.split(',')
        authorMsg=splitLine[1].split(":")
        #print(authorMsg)
     
        author= authorMsg[0]
        msg=authorMsg[1::]
        #print("-->",time,date,author,msg)
        ar.append([date,time,author,msg])
        c+=1


        
        
print(c,c1,c2)
#print(ar)
df=pd.DataFrame(ar,columns=["Date","Time","Author","Message"])


def top10Author():
    l=df['Author'].value_counts()
    
    
    plt.pyplot.title(title1)
    plt.pyplot.xlabel('Number of messages')
    plt.pyplot.ylabel('Group Members')
    top10auth=l.tail(15)
    top10auth.plot.barh()
    plt.pyplot.figure(figsize=(100,150))
    #mng=plt.pyplot.get_current_fig_manager()
    #mng.window.showMaximized()
    

top10Author()
df
