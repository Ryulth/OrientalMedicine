#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import openpyxl
 
# 엑셀파일 열기
#wb = openpyxl.load_workbook('DB.xlsx')

#ws = wb.active
#### ws = wb.get_sheet_by_name("Sheet1")
 
# 국영수 점수를 읽기
#for r in ws.rows:
#    year = r[0].value   # 행 인덱스
#    mont = r[1].value
#    day = r[2].value
#    hua = r[3].value
#    su = r[4].value
#    mok = r[5].value
#    kim = r[6].value
#    to = r[7].value

    #print(year, mont, day, hua, su, mok, kim, to)
    
#wb.save("score2.xlsx")
##wb.close()


# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc


# In[2]:


manseDB = pd.read_excel('manseDB.xlsx') ## 엑셀 데이터

manseDB

patientDB = pd.read_excel('patientDB.xlsx') ## 환자 정보 엑셀 읽기

yearinfo = patientDB['생년월일']# 환자 생년월일

IDinfo = patientDB['ID'] # 환자 아이디 정보



# In[3]:


ocsDWVDIS = pd.read_excel('ocsDWVDIS.xlsx') ## 질병 정보 엑셀 데이터

discode2 = ocsDWVDIS['Mcd'] ## 질병의 코드 discode1와 같은 것
disname = ocsDWVDIS['KorName'] ## 질병의 한글 표시


ocsDWWDATA = pd.read_excel('ocsDWWDATA.xlsx') ## 환자ID & 질병 코드 엑셀 데이터


disID = ocsDWWDATA['ID'] ## 질병을 가진 환자의 ID
discode1 = ocsDWWDATA['MCD'] # 질병의 코드


# In[4]:


year = manseDB['생년월일'] # 만세력 생년월일

hua = manseDB['화']
su = manseDB['수']
mok = manseDB['목']
kim = manseDB['금']
to = manseDB['토']


# In[5]:


yearinfo


# In[6]:


IDinfo


# In[7]:


manseDB


# In[ ]:





# In[8]:


hua1=[] # 화 숫자 리스트
su1 = [] # 수 숫자 리스트
mok1 = [] # 목 숫자 리스트
kim1 = [] #금 숫자 리스트
to1 = [] # 토 숫자 리스트



IDinfo1 = [] # 환자 ID 리스트

discode33 = [] #질병 코드 리스트

newdisname33 = [] # 질병 한글 이름 리스트

num1=0
for i in range(200): # 1~50번째까지의 환자 데이터
    num=0
    
    for i in year:
        if(yearinfo[num1]==i): ## 만약  생년월일이 맞으면 해당 생년월일의 음양오행을 삽입
            hua1.append(hua[num])
            su1.append(su[num])
            mok1.append(mok[num])
            kim1.append(kim[num])
            to1.append(to[num])
            break
        num=num+1
    
    num=0
    for i in yearinfo: ## 환자정보의 생년월일 리스트
        if(i==yearinfo[num1]): ## 만약  생년월일이 존재한다면 해당 생년월일을 데이터를 생성
            IDinfo1.append(IDinfo[num])
            break
        num=num+1
    
    num=0
    
    for i in disID:
        if (i==IDinfo1[num1]):  ## 그리고 질병 아이디가 존재하는 DB에서 해당 환자의 ID를 검색하여 해당 환자의 질병코드를 찾아낸다
            discode3=discode1[num]
            break
        num=num+1
    
    num=0
    for i in discode2: ## 그리고 해당 환자의 질병코드를 다시 한번 검색하여 한글로 된 환자의 한글질병으로 검색한다
        if(i==discode3):
            newdisname=disname[num]
            newdisname33.append(newdisname)
            break
        num=num+1
        
    num=0
    discode33.append(discode3)
    
    num1=num1+1
    


# In[9]:


rks = [] # 간

resultlist = []
num=0
mok2=0
hua2=0
kim2=0
to2=0
su2=0
len1=0
for s in newdisname33: # 총 필드중에서 간의 질병만 찾는다
    if "간" in s:
        resultlist.append(s)
        mok2=mok1[num]+mok2
        hua2=hua1[num]+hua2
        to2=to1[num]+to2
        kim2=kim1[num]+kim2
        su2=su1[num]+su2
        len1=len1+1
    num=num+1
    

#matching = [s for s in newdisname if "간" in s] 



resultlist = list(set(resultlist)) ##중복제거

mok2=mok2/len1
rks.append(mok2)
hua2=hua2/len1
rks.append(hua2)
to2=to2/len1
rks.append(to2)
kim2=kim2/len1
rks.append(kim2)
su2=su2/len1
rks.append(su2)

print("----간 환자들의 음양오행 평균 수치----\n")

print("목의 평균 수치 : %.2f"%mok2)
print("화의 평균 수치 : %.2f"%hua2)
print("토의 평균 수치 : %.2f"%to2)
print("금의 평균 수치 : %.2f"%kim2)
print("수의 평균 수치 : %.2f"%su2)


##시각화

print("\n")

industry = ['su', 'kim', 'to', 'hua', 'mok']
fluctuations = [su2, kim2, to2, hua2, mok2]

fig = plt.figure(figsize=(12, 5))
ax = fig.add_subplot(111)

ypos = np.arange(5)
rects = plt.barh(ypos, fluctuations, align='center', height=0.5)
plt.yticks(ypos, industry)

plt.xlabel('등락률')
plt.show()

#시각화


print("\n")
print("---필드 환자들의 간 질병----\n")
for i in resultlist:
    print(i)
    


# In[ ]:





# In[10]:


eowkd = [] #대장

resultlist = []
num=0
mok2=0
hua2=0
kim2=0
to2=0
su2=0
len1=0
for s in newdisname33: # 총 필드중에서 간의 질병만 찾는다
    if "대장" in s:
        resultlist.append(s)
        mok2=mok1[num]+mok2
        hua2=hua1[num]+hua2
        to2=to1[num]+to2
        kim2=kim1[num]+kim2
        su2=su1[num]+su2
        len1=len1+1
    num=num+1
    

#matching = [s for s in newdisname if "간" in s] 



resultlist = list(set(resultlist)) ##중복제거

mok2=mok2/len1
eowkd.append(mok2)
hua2=hua2/len1
eowkd.append(hua2)
to2=to2/len1
eowkd.append(to2)
kim2=kim2/len1
eowkd.append(kim2)
su2=su2/len1
eowkd.append(su2)

print("----대장 환자들의 음양오행 평균 수치----\n")

print("목의 평균 수치 : %.2f"%mok2)
print("화의 평균 수치 : %.2f"%hua2)
print("토의 평균 수치 : %.2f"%to2)
print("금의 평균 수치 : %.2f"%kim2)
print("수의 평균 수치 : %.2f"%su2)

print("\n")

##시각화

industry = ['su', 'kim', 'to', 'hua', 'mok']
fluctuations = [su2, kim2, to2, hua2, mok2]

fig = plt.figure(figsize=(12, 5))
ax = fig.add_subplot(111)

ypos = np.arange(5)
rects = plt.barh(ypos, fluctuations, align='center', height=0.5)
plt.yticks(ypos, industry)

plt.xlabel('등락률')
plt.show()

#시각화


print("\n")
print("---필드 환자들의 대장 질병----\n")
for i in resultlist:
    print(i)


# In[11]:


thwkd = [] #소장

resultlist = []
num=0
mok2=0
hua2=0
kim2=0
to2=0
su2=0
len1=0
for s in newdisname33: # 총 필드중에서 간의 질병만 찾는다
    if "소장" in s:
        resultlist.append(s)
        mok2=mok1[num]+mok2
        hua2=hua1[num]+hua2
        to2=to1[num]+to2
        kim2=kim1[num]+kim2
        su2=su1[num]+su2
        len1=len1+1
    num=num+1
    

#matching = [s for s in newdisname if "간" in s] 



resultlist = list(set(resultlist)) ##중복제거

mok2=mok2/len1
thwkd.append(mok2)
hua2=hua2/len1
thwkd.append(hua2)
su2=su2/len1
thwkd.append(su2)
kim2=kim2/len1
thwkd.append(kim2)
to2=to2/len1
thwkd.append(to2)

print("----소장 환자들의 음양오행 평균 수치----\n")

print("목의 평균 수치 : %.2f"%mok2)
print("화의 평균 수치 : %.2f"%hua2)
print("토의 평균 수치 : %.2f"%to2)
print("금의 평균 수치 : %.2f"%kim2)
print("수의 평균 수치 : %.2f"%su2)

##시각화

print("\n")

industry = ['su', 'kim', 'to', 'hua', 'mok']
fluctuations = [su2, kim2, to2, hua2, mok2]

fig = plt.figure(figsize=(12, 5))
ax = fig.add_subplot(111)

ypos = np.arange(5)
rects = plt.barh(ypos, fluctuations, align='center', height=0.5)
plt.yticks(ypos, industry)

plt.xlabel('등락률')
plt.show()

#시각화

print("\n")
print("---필드 환자들의 소장 질병----\n")
for i in resultlist:
    print(i)


# In[12]:


tlswkd = [] #신장

resultlist = []
num=0
mok2=0
hua2=0
kim2=0
to2=0
su2=0
len1=0
for s in newdisname33: # 총 필드중에서 간의 질병만 찾는다
    if "신장" in s:
        resultlist.append(s)
        mok2=mok1[num]+mok2
        hua2=hua1[num]+hua2
        to2=to1[num]+to2
        kim2=kim1[num]+kim2
        su2=su1[num]+su2
        len1=len1+1
    num=num+1
    

#matching = [s for s in newdisname if "간" in s] 



resultlist = list(set(resultlist)) ##중복제거

mok2=mok2/len1
tlswkd.append(mok2)
hua2=hua2/len1
tlswkd.append(hua2)
su2=su2/len1
tlswkd.append(su2)
kim2=kim2/len1
tlswkd.append(kim2)
to2=to2/len1
tlswkd.append(to2)

print("----신장 환자들의 음양오행 평균 수치----\n")

print("목의 평균 수치 : %.2f"%mok2)
print("화의 평균 수치 : %.2f"%hua2)
print("토의 평균 수치 : %.2f"%to2)
print("금의 평균 수치 : %.2f"%kim2)
print("수의 평균 수치 : %.2f"%su2)

##시각화

print("\n")

industry = ['su', 'kim', 'to', 'hua', 'mok']
fluctuations = [su2, kim2, to2, hua2, mok2]

fig = plt.figure(figsize=(12, 5))
ax = fig.add_subplot(111)

ypos = np.arange(5)
rects = plt.barh(ypos, fluctuations, align='center', height=0.5)
plt.yticks(ypos, industry)

plt.xlabel('등락률')
plt.show()

#시각화

print("\n")
print("---필드 환자들의 신장 질병----\n")
for i in resultlist:
    print(i)


# In[13]:


dnlwkd = [] #위장

resultlist = []
num=0
mok2=0
hua2=0
kim2=0
to2=0
su2=0
len1=0
for s in newdisname33: # 총 필드중에서 간의 질병만 찾는다
    if "위장" in s:
        resultlist.append(s)
        mok2=mok1[num]+mok2
        hua2=hua1[num]+hua2
        to2=to1[num]+to2
        kim2=kim1[num]+kim2
        su2=su1[num]+su2
        len1=len1+1
    num=num+1
    

#matching = [s for s in newdisname if "간" in s] 



resultlist = list(set(resultlist)) ##중복제거

mok2=mok2/len1
dnlwkd.append(mok2)
hua2=hua2/len1
dnlwkd.append(hua2)
su2=su2/len1
dnlwkd.append(su2)
kim2=kim2/len1
dnlwkd.append(kim2)
to2=to2/len1
dnlwkd.append(to2)

print("----위장 환자들의 음양오행 평균 수치----\n")

print("목의 평균 수치 : %.2f"%mok2)
print("화의 평균 수치 : %.2f"%hua2)
print("토의 평균 수치 : %.2f"%to2)
print("금의 평균 수치 : %.2f"%kim2)
print("수의 평균 수치 : %.2f"%su2)

##시각화

print("\n")

industry = ['su', 'kim', 'to', 'hua', 'mok']
fluctuations = [su2, kim2, to2, hua2, mok2]

fig = plt.figure(figsize=(12, 5))
ax = fig.add_subplot(111)

ypos = np.arange(5)
rects = plt.barh(ypos, fluctuations, align='center', height=0.5)
plt.yticks(ypos, industry)

plt.xlabel('등락률')
plt.show()

#시각화

print("\n")
print("---필드 환자들의 위장 질병----\n")
for i in resultlist:
    print(i)


# In[ ]:





# In[14]:


########################################## 여기부터는 돌리지 않아도돼요#############33


###### 이 아래는 사용자의 입력에 따라 생년월일/ 음양오행을 구하는 코드


# In[15]:


print('사용자의 생년월일을 입력해주십시오 : ')
inpo = int(input()) ## 사용자의 생년월일 입력


# In[ ]:





# In[16]:


num=0

newdisname1= []

for i in year: ## 만세력의 생년월일 리스트
    
    if(i==inpo): ## 만약 사용자가 입력한 생년월일이 맞으면 해당 생년월일의 음양오행을 삽입
        hua1 = hua[num]
        su1 = su[num]
        mok1 = mok[num]
        kim1= kim[num]
        to1 = to[num]
        #print(i)
        break
    num=num+1
    
num=0

for i in yearinfo: ## 환자정보의 생년월일 리스트
    if(i==inpo): ## 만약 사용자가 입력한 생년월일이 존재한다면 해당 생년월일을 데이터를 생성
        IDinfo1=IDinfo[num]
    num=num+1
    
num=0



for i in disID:
    if (i==IDinfo1):  ## 그리고 질병 아이디가 존재하는 DB에서 해당 환자의 ID를 검색하여 해당 환자의 질병코드를 찾아낸다
        discode3=discode1[num]
        
    num=num+1
    
num=0


for i in discode2: ## 그리고 해당 환자의 질병코드를 다시 한번 검색하여 한글로 된 환자의 한글질병으로 검색한다
    if(i==discode3):
        newdisname=disname[num]
        
    num=num+1
num=0





#print(hua1,su1,mok1,kim1,to1)
yearinfo_ = []

yearinfo__ = []

for i in yearinfo:
    yearinfo_.append(i)
    
for i in yearinfo:
    yearinfo__.append(i)
    
num_=0


count = []

a = yearinfo_.count(inpo)
    
if(yearinfo_.count(inpo)>=2):
    print("환자의 생년월일 : ",inpo)
    for i in yearinfo_:
        if(inpo==i):
            
            count.append(yearinfo_.index(inpo))
            
            yearinfo_[num_]=0
            
        num_=num_+1
        
        
        

    
     ###########################
    num_=0
    for ii in count:
        
        
     
        num=0

        #print(IDinfo[ii])
        for i in yearinfo__: ## 환자정보의 생년월일 리스트
            if(i==yearinfo__[count[num_]]): ## 만약 사용자가 입력한 생년월일이 존재한다면 해당 생년월일을 데이터를 생성
                IDinfo1=IDinfo[count[num_]]
                break
            num=num+1
        num=0



        for i in disID:
            if (i==IDinfo1):  ## 그리고 질병 아이디가 존재하는 DB에서 해당 환자의 ID를 검색하여 해당 환자의 질병코드를 찾아낸다
                discode3=discode1[num]
                break

            num=num+1
        num=0


        for i in discode2: ## 그리고 해당 환자의 질병코드를 다시 한번 검색하여 한글로 된 환자의 한글질병으로 검색한다
            if(i==discode3):
                newdisname=disname[num]
                

            num=num+1
        num=0
        
        num_=num_+1
        print("질병명 : ",newdisname)
        newdisname1.append(newdisname)
        
    
    
    
    ####################################3
        
        
    
    print("\n")
    print("목 : ",mok1)
    print("화 : ",hua1)
    print("토 : ",to1)
    print("금 : ",kim1)
    print("수 : ",su1)
    
    #시각화


    industry = ['su', 'kim', 'to', 'hua', 'mok']
    fluctuations = [su1, kim1, to1, hua1, mok1]

    fig = plt.figure(figsize=(12, 5))
    ax = fig.add_subplot(111)

    ypos = np.arange(5)
    rects = plt.barh(ypos, fluctuations, align='center', height=0.5)
    plt.yticks(ypos, industry)

    plt.xlabel('등락률')
    plt.show()

    print("\n")

#시각화
    
    
else:
    print("환자의 생년월일 : ",inpo)
    print("질병명 : ",newdisname)
    newdisname1.append(newdisname)
    print("\n")
    print("목 : ",mok1)
    print("화 : ",hua1)
    print("토 : ",to1)
    print("금 : ",kim1)
    print("수 : ",su1)
    
    
    industry = ['su', 'kim', 'to', 'hua', 'mok']
    fluctuations = [su1, kim1, to1, kim1, mok1]

    fig = plt.figure(figsize=(12, 5))
    ax = fig.add_subplot(111)

    ypos = np.arange(5)
    rects = plt.barh(ypos, fluctuations, align='center', height=0.5)
    plt.yticks(ypos, industry)

    plt.xlabel('등락률')
    plt.show()

    print("\n")

#시각화



#시각화
    
if(a==0):
    a=1
    
print("해당 생년월일 데이터 개수 : ",a)


# In[35]:


ghkrfbf=0
for i in newdisname1:
    if "소장" in i:
        print("----소장 질병 환자의 평균 음양오행---")
        print("목 : %.2f"%thwkd[0])
        print("화 : %.2f"%thwkd[1])
        print("토 : %.2f"%thwkd[2])
        print("금 : %.2f"%thwkd[3])
        print("수 : %.2f"%thwkd[4])
        
        print("\n")
        
        print("----환자의 음양오행----")
        print("목 : %.2f"%mok1)
        print("화 : %.2f"%hua1)
        print("토 : %.2f"%to1)
        print("금 : %.2f"%kim1)
        print("수 : %.2f"%su1)
        
        print("\n")
        
        if(mok1+0.5>=tlswkd[0]):
            ghkrfbf=ghkrfbf + 0.25
        if(hua1+1>=tlswkd[1]):
            ghkrfbf=ghkrfbf + 0.45
        if(to1+0.5>=tlswkd[2]):
            ghkrfbf=ghkrfbf + 0.10
        if(kim1+0.5>=tlswkd[3]):
            ghkrfbf=ghkrfbf + 0.10
        if(su1+0.5>=tlswkd[4]):
            ghkrfbf=ghkrfbf + 0.10
        
        if(ghkrfbf>=0.7):
            print("환자의 소장에 질병이 있을 가능성 : 높음")
        
        else:
            print("환자의 소장에 질병이 있을 가능성 : 낮음")

        break  
        
        
        
    elif "대장" in i:
        
        print("----대장 질병 환자의 평균 음양오행---")
        print("목 : %.2f"%eowkd[0])
        print("화 : %.2f"%eowkd[1])
        print("토 : %.2f"%eowkd[2])
        print("금 : %.2f"%eowkd[3])
        print("수 : %.2f"%eowkd[4])
        
        
        print("\n")
        
        if(mok1+0.5>=eowkd[0]):
            ghkrfbf=ghkrfbf + 0.10
        if(hua1+0.5>=eowkd[1]):
            ghkrfbf=ghkrfbf + 0.10
        if(to1+0.5>=eowkd[2]):
            ghkrfbf=ghkrfbf + 0.25
        if(kim1+1>=eowkd[3]):
            ghkrfbf=ghkrfbf + 0.45
        if(su1+0.5>=eowkd[4]):
            ghkrfbf=ghkrfbf + 0.10
        
        if(ghkrfbf>=0.7):
            print("환자의 대장에 질병이 있을 가능성 : 높음")
        
        else:
            print("환자의 대장에 질병이 있을 가능성 : 낮음")

        break
        
    elif "간" in i:
        
        print("----간 질병 환자의 평균 음양오행---")
        print("목 : %.2f"%rks[0])
        print("화 : %.2f"%rks[1])
        print("토 : %.2f"%rks[2])
        print("금 : %.2f"%rks[3])
        print("수 : %.2f"%rks[4])
        
        print("\n")
        
        print("----환자의 음양오행----")
        print("목 : %.2f"%mok1)
        print("화 : %.2f"%hua1)
        print("토 : %.2f"%to1)
        print("금 : %.2f"%kim1)
        print("수 : %.2f"%su1)
        
        print("\n")
        
        if(mok1+1>=rks[0]):
            ghkrfbf=ghkrfbf + 0.45
        if(hua1+0.5>=rks[1]):
            ghkrfbf=ghkrfbf + 0.25
        if(to1+0.5>=rks[2]):
            ghkrfbf=ghkrfbf + 0.10
        if(kim1+0.5>=rks[3]):
            ghkrfbf=ghkrfbf + 0.10
        if(su1+0.5>=rks[4]):
            ghkrfbf=ghkrfbf + 0.10
        
        if(ghkrfbf>=0.7):
            print("환자의 간에 질병이 있을 가능성 : 높음")
        
        else:
            print("환자의 간에 질병이 있을 가능성 : 낮음")
        
        
        break
        
    elif "신장" in i:
        
        print("----신장 질병 환자의 평균 음양오행---")
        print("목 : %.2f"%tlswkd[0])
        print("화 : %.2f"%tlswkd[1])
        print("토 : %.2f"%tlswkd[2])
        print("금 : %.2f"%tlswkd[3])
        print("수 : %.2f"%tlswkd[4])
        
        print("\n")
        
        print("----환자의 음양오행----")
        print("목 : %.2f"%mok1)
        print("화 : %.2f"%hua1)
        print("토 : %.2f"%to1)
        print("금 : %.2f"%kim1)
        print("수 : %.2f"%su1)
        
        print("\n")
        
        if(mok1+0.5>=tlswkd[0]):
            ghkrfbf=ghkrfbf + 0.10
        if(hua1+0.5>=tlswkd[1]):
            ghkrfbf=ghkrfbf + 0.25
        if(to1+0.5>=tlswkd[2]):
            ghkrfbf=ghkrfbf + 0.10
        if(kim1+0.5>=tlswkd[3]):
            ghkrfbf=ghkrfbf + 0.10
        if(su1+1>=tlswkd[4]):
            ghkrfbf=ghkrfbf + 0.45
        
        if(ghkrfbf>=0.7):
            print("환자의 신장에 질병이 있을 가능성 : 높음")
        
        else:
            print("환자의 신장에 질병이 있을 가능성 : 낮음")
        
        
        break
        
    elif "위장" in i:
        
        print("----위장 질병 환자의 평균 음양오행---")
        print("목 : %.2f"%dnlwkd[0])
        print("화 : %.2f"%dnlwkd[1])
        print("토 : %.2f"%dnlwkd[2])
        print("금 : %.2f"%dnlwkd[3])
        print("수 : %.2f"%dnlwkd[4])
        
        print("\n")
        
        print("----환자의 음양오행----")
        print("목 : %.2f"%mok1)
        print("화 : %.2f"%hua1)
        print("토 : %.2f"%to1)
        print("금 : %.2f"%kim1)
        print("수 : %.2f"%su1)
        
        print("\n")
        
        if(mok1+0.5>=dnlwkd[0]):
            ghkrfbf=ghkrfbf + 0.10
        if(hua1+0.5>=dnlwkd[1]):
            ghkrfbf=ghkrfbf + 0.10
        if(to1+1>=dnlwkd[2]):
            ghkrfbf=ghkrfbf + 0.45
        if(kim1+0.5>=dnlwkd[3]):
            ghkrfbf=ghkrfbf + 0.10
        if(su1+0.5>=dnlwkd[4]):
            ghkrfbf=ghkrfbf + 0.25
        
        if(ghkrfbf>=0.7):
            print("환자의 위장에 질병이 있을 가능성 : 높음")
        
        else:
            print("환자의 위장에 질병이 있을 가능성 : 낮음")
        
        
        break


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




