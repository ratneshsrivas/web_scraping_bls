#!/usr/bin/env python
# coding: utf-8

# In[1]:


#installing beautifulsoup

get_ipython().system(' pip install beautifulsoup4')


# In[2]:


get_ipython().system(' pip install requests')


# In[3]:


#importing librarires

import sys
import time
from bs4 import BeautifulSoup
import requests


# In[4]:


#feeding the bereau of labor standard url for scraping

url = ("https://www.bea.gov/")


# In[5]:


response = requests.get(url)


# In[6]:


type(response)


# In[7]:


response.text


# In[8]:


filename = "temp.html"


# In[9]:


bs= BeautifulSoup(response.text,"html.parser")


# In[10]:


#to make the code readable use pretify

pretify = BeautifulSoup(bs.prettify(),"html.parser")
pretify


# In[11]:


formatted_text=bs.prettify()
formatted_text


# In[12]:


with open(filename,"w") as f:
  f.write(formatted_text)


# In[13]:


formatted_text


# In[14]:


#image

images=bs.find_all('img')


# In[15]:


#finding the total number of images in the url

total_num_images = len(images)
total_num_images


# In[16]:


# anchors on the website

list_of_anchors = bs.find_all('a')


# In[17]:


# counting number of anchors on the website

numb_of_anchors = len(list_of_anchors)
numb_of_anchors


# In[18]:


#assigning a name for title

title_name = bs.find_all('title')
title_name


# In[19]:


bs.title.string


# In[20]:


#finding parent name

bs.title.parent.name


# In[21]:


#creating a csv file

import csv
header = ['title_name','numb_of_anchors','total_num_images']
data = [title_name,numb_of_anchors,total_num_images]

with open('bereau_of_economic_analysis_web_scraping.csv','w',newline='', encoding='UTF8') as f:
  writer = csv.writer(f)
  writer.writerow(header)
  writer.writerow(data)


# In[ ]:




