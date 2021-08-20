#!/usr/bin/env python
# coding: utf-8

# In[26]:


import time,os
import pickle
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from datetime import datetime
import requests
import re


# In[27]:


#儲存變數
def save_variable(v,filename):
  f=open(filename,'wb')
  pickle.dump(v,f)
  f.close()
  return filename
#讀取變數
def load_variavle(filename):
  f=open(filename,'rb')
  r=pickle.load(f)
  f.close()
  return r


# In[28]:


def lineNotifyMessage(token, msg):

    headers = {"Authorization": "Bearer " + token, }
    payload = {'message': msg,}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code


# In[46]:


path = 'C:/Users/momti/chromedriver.exe'
option = webdriver.ChromeOptions()
option.add_argument("headless")
browser = webdriver.Chrome(path, options=option)
url = 'https://store.steampowered.com/app/1366540/_/'
browser.get(url)
browser.implicitly_wait(1)
date = browser.find_element_by_class_name("localdateandtime_DateAndTime_2V6GL").text
browser.implicitly_wait(1)
href = browser.find_element_by_class_name("partnereventwebrowembed_EventsSummariesCtn_1snIw").find_element_by_tag_name('a')
href = href.get_attribute('href')
pattern = re.compile(r'(\d+年\d+月\d+日)')
nowdate = time.strptime(re.search(pattern, date).group(1), "%Y年%m月%d日")
pastdate = load_variavle('C:/Users/momti/results.txt')
filename = save_variable(nowdate,'C:/Users/momti/results.txt')
if nowdate > pastdate:
    message = "已更新，最近更新連結:\n"+href
else:
    message = "尚未更新，最近更新連結:\n"+href
token = 'S3LOaAwDcwbgFUnAkjQLGCl8LBaa5ArhwlTFM4n1e5M'
lineNotifyMessage(token, message)


# In[40]:





# In[22]:




