"""
Author : Ghulam Mohiyuddin
What is this: This is a whatsapp group/indivisual chat analyser 
Note: This is not a final wait for more functionality
"""



import os
import re
import pandas as pd
import matplotlib.pyplot as plt
#link="C:\\Users\\asus\\Downloads\\WhatsApp Chat with GATE CS & IT - 2020.txt"
#link="C:\\Users\\asus\\Downloads\\WhatsApp Chat with Only information no emoji.txt"#250-
#link="C:\\Users\\asus\\Downloads\\WhatsApp Chat with CSE YR16-20.txt"#300+
link="C:\\Users\\asus\\Downloads\\WhatsApp Chat with Unemployed peeps.txt"
#link="C:\\Users\\asus\\Downloads\\WhatsApp Chat with Aise hi bas.txt"
tit=link.split("\\")
title=tit[-1]
title1=title[:len(title)-4:]
print(title1)
cht=open(link,encoding="utf8")
ar=[]
c=0
c1=0
ar1=[]
c2=0
f=0
def startsWithDate(s):
    #ReGex finding date and time
    pattern = "^([0-2][0-9]|(3)[0-1])(\/)(([0-9])|((0)[0-9])|((1)[0-2]))(\/)(\d{2}|\d{4}), ([0-9][0-9]|[0-9]):([0-9][0-9])"
    result = re.match(pattern, s)
    if result:
        return True
    return False
def findColon(s):
    n=len(s)
    c=0
    for i in range(n):
        if s[i]==":":
            c+=1
    return c
    
    
    
    
    
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



while 1:
    rd=cht.readline()
    if not rd:break
        
   # print(rd)
    c1+=1
    if startsWithDate(rd):
       # print(rd)
        splitLine=rd.split("-")
        dateTime=splitLine[0]
        #print(dateTime)
        date,time=dateTime.split(',')
        c+=1
    
        if findColon(splitLine[1])>0:
            c2+=1
            authorMsg=splitLine[1].split(":")
            
     
            author= authorMsg[0][:15]+".."
            msg=authorMsg[1::]
            
            ar.append([date,time,author,msg])
        
        else:
            ar1.append(splitLine[1])
            


        
        
print("Total msg-",c,"Total valid msg-",c2)

df=pd.DataFrame(ar,columns=["Date","Time","GroupMember","Message"])

l=dict(df['GroupMember'].value_counts())
xval=[]
yval=[]
for x,y in l.items():
    xval.append(x)
    yval.append(y)

def showAll():

    plt.figure(figsize=(len(l)*0.25,10))
    plt.bar(xval,yval,width=0.8)
    
    plt.title("Group: "+title1)
    plt.xlabel("Group Members")
    plt.ylabel("Number of messages")
    plt.xticks(xval,rotation=90)
    
    
showAll()
c3=0
def autolabel(x,y):
    global c3
    for i in range(len(x)):

        plt.text(x[i],y[i]+5,str(y[i]),ha='center',rotation=90,color='red')
        c3+=y[i]
autolabel(xval,yval)
plt.text(len(l)-len(l)//2,len(l), 'Total Active Members: '+str(len(l))+", Total Message-"+str(c3),color='red')

plt.show()
#plt.savefig('test.png')


"""
#print(ar[0])
def top10Author():
    l=df['GroupMember'].value_counts()
   
    
    
    #plt.title(title1)
    plt.ylabel('Number of messages')
    plt.xlabel('Group Members')
    top10auth=l.iloc[range(0,len(l))]
    #top10auth.plot.line()
    top10auth.plot.bar(legend=True,title="Group: "+title1,fontsize=8,figsize=(len(l)*0.3,5))
    #top10auth.plot.pie()
    
    top10auth.plot.bar()
   

#top10Author()
#print(len(ar1))
#df.loc[range(20,60)]
#df[["Date","groupMember"]]
#df.describe()
#sort_values(self, by, axis=0, ascending=True
#df.query('Date=="19/04/2019" ').sort_values("Time",ascending=True)
#print(df.to_html())
    
"""
