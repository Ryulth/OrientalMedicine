
# coding: utf-8

# In[1]:


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re
import os
import time
from multiprocessing import Pool , cpu_count
num_cores = cpu_count()


# In[2]:


import platform
file_path='./datas/'
file_name=file_path+'chromedriver_'+platform.system().lower()


# In[3]:


result=pd.DataFrame(columns=['생년월일','목','화','토','금','수'])
result1=pd.DataFrame(columns=['생년월일','목','화','토','금','수'])
result2=pd.DataFrame(columns=['생년월일','목','화','토','금','수'])
result3=pd.DataFrame(columns=['생년월일','목','화','토','금','수'])
result4=pd.DataFrame(columns=['생년월일','목','화','토','금','수'])


# In[4]:


result.loc[len(result)]=[0,0,0,0,0,0]
result1.loc[len(result1)]=[0,0,0,0,0,0]
result2.loc[len(result2)]=[0,0,0,0,0,0]
result3.loc[len(result3)]=[0,0,0,0,0,0]
result4.loc[len(result4)]=[0,0,0,0,0,0]


# In[5]:


num_cores


# In[6]:


def get_data(y):
    temp=pd.DataFrame(columns=['생년월일','목','화','토','금','수'])
    temp.loc[len(temp)]=[0,0,0,0,0,0]
    try :
        options = webdriver.ChromeOptions ()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        chrome_driver=webdriver.Chrome(file_name,chrome_options=options)
        chrome_driver.implicitly_wait(3)
        chrome_driver.get('http://manse.sajuplus.net')
#for y in range(1,106):
        print ('PID:',os.getpid(),"  YEAR:" ,y+1917)
        try:
            chrome_driver.find_element_by_xpath('//*[@id="jb-content"]/table/tbody/tr[2]/td/form/table[3]/tbody/tr[3]/td[2]/select[2]/option[{0}]'.format(y)).click()#년도 1918~2022 option 1~ 105
            for m in range(2,14):#14):
                chrome_driver.find_element_by_xpath('//*[@id="jb-content"]/table/tbody/tr[2]/td/form/table[3]/tbody/tr[3]/td[2]/select[3]/option[{0}]'.format(m)).click()#월 option 2~13
                for d in range(2,32):#32):
                    chrome_driver.find_element_by_xpath('//*[@id="jb-content"]/table/tbody/tr[2]/td/form/table[3]/tbody/tr[3]/td[2]/select[1]/option[2]').click()#양력
                    chrome_driver.find_element_by_xpath('//*[@id="jb-content"]/table/tbody/tr[2]/td/form/table[3]/tbody/tr[3]/td[2]/select[4]/option[{0}]'.format(d)).click()#일 option2~32
                    chrome_driver.find_element_by_xpath('//*[@id="jb-content"]/table/tbody/tr[2]/td/form/table[3]/tbody/tr[4]/td[2]/select/option[1]').click()# 생시 모름
                    chrome_driver.find_element_by_xpath('//*[@id="jb-content"]/table/tbody/tr[2]/td/form/table[3]/tbody/tr[5]/td/div').click()# 클릭
                    html = chrome_driver.page_source
                    soup = BeautifulSoup(html,'html.parser')
                    try :
                        my_manse=soup.select_one('table > tbody > tr:nth-of-type(1) > td > table:nth-of-type(1) > tbody > tr:nth-of-type(13)')#nth child 는 오류가 많다 nth-of-type 로 변동
                        manse=my_manse.text
                        try :
                            hua1=re.compile(r'화\d').search(manse).group()[1]
                        except :
                            hua1='0'
                        try :    
                            su1 = re.compile(r'수\d').search(manse).group()[1]
                        except :
                            su1='0'
                        try :    
                            mok1 = re.compile(r'목\d').search(manse).group()[1]
                        except :
                            mok1='0'
                        try:
                            kim1 = re.compile(r'금\d').search(manse).group()[1]
                        except:
                            kim1='0'
                        try:   
                            to1 = re.compile(r'토\d').search(manse).group()[1]
                        except:
                            to1='0'
                        my_birth=soup.select_one('table > tbody > tr:nth-of-type(1) > td > table:nth-of-type(1) > tbody > tr:nth-of-type(2) > td > span:nth-of-type(1)')
                        birth=re.compile(r'\d+년 \d+월 \d+일').search(my_birth.text).group()
                        birth=birth.replace('년','')
                        birth=birth.replace('월','')
                        birth=birth.replace('일','')
                        birth=birth.replace(' ','')
                        if temp.tail(1)['생년월일'].values[0]!=str(birth):
                            temp.loc[len(temp)]=[birth,mok1,hua1,to1,kim1,su1]    
                    except Exception as e:
                        print(y+1917,"년 에러",e)
        except Exception as e:
            print(y+1917,"년 에러",e)
        chrome_driver.quit()
    except Exception as e:
            print(y+1917,"년 에러",e)
    temp=temp.drop(0)
    return temp


# In[7]:


if __name__=='__main__':
    start_time = time.time()
    pool = Pool(processes=num_cores-4) #갯수조정
    result1=pd.concat(pool.map(get_data,range(1,33)))
    print('1st--------------------------')
    result2=pd.concat(pool.map(get_data,range(33,65)))
    print('2st--------------------------')
    result3=pd.concat(pool.map(get_data,range(65,97)))
    print('3st--------------------------')
    result4=pd.concat(pool.map(get_data,range(97,106)))
    print('4st--------------------------')
    print("--- %s seconds ---" % (time.time() - start_time))


# In[16]:


error_year=[1998,2016,2017,2018,2020,2021]
error_y=[81,99,100,101,103,104]


# In[12]:


result5=pd.DataFrame(columns=['생년월일','목','화','토','금','수'])
result5.loc[len(result4)]=[0,0,0,0,0,0]


# In[17]:


result5=pd.concat(pool.map(get_data,error_y))


# In[23]:


result5.head()


# In[24]:


result=pd.concat([result1,result2,result3,result4,result5],ignore_index=True)


# In[25]:


result


# In[28]:


result.drop_duplicates()


# In[34]:


writer=pd.ExcelWriter('./datas/manseDB_.xlsx')
result.to_excel(writer,index=False,encoding='utf8')
writer.save()


# In[35]:


result.to_csv('./datas/manseDB_.csv',index=False,encoding='utf8')

