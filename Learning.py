#!/usr/bin/env python
# coding: utf-8

# In[2]:


af1=5.23124254
print(af1)


# In[3]:


f1=5.12e2
print(f1)


# In[4]:


f2=5e3
print(f2)


# In[5]:


ac1=3+0.2j
print(ac1)


# In[6]:


st="hello"
print(str(st))
print(repr(st))


# In[8]:


msg=input("hello:")
print(msg)


# In[9]:


s='crazyit.org is very good'
print('very' in s)


# In[10]:


a= 'our domain is crazyit.org'
print(a.title())
print(a.lower())
print(a.upper())


# In[13]:


s='crazyit.org is a good site'
print(s.split())
mylist=s.split()
print('/'.join(mylist))


# In[14]:


print('27的开3次方：',27**(1/3))


# In[16]:


import time
a=time.gmtime()
print(a)


# In[17]:


a=5
b=3
st="a大于b" if a>b else "a不大于b"
print(st)


# In[18]:


first,*middle,last=range(10)
print (first)
print (middle)
print (last)


# In[19]:


b_list=['Python','Swift','Ruby','Go','Kotlin','Erlang']
b_list.sort(key=len,reverse=True)
print(b_list)


# In[20]:


scores={'语文':89,'数学':92,'英语':93}
print(scores)


# In[23]:


# 元组可以作为dict的key，但是列表不能，因为列表是可变类型，而dict要求key必须是不可变类型
cars=[['BMW',8.5],['BENS',8.3],['AUDI',7.9]]
dict4=dict(cars)
print(dict4)
dict4['ABC']=7.8
print(dict4)
print(dict4.get('BMW'))


# In[26]:


# 使用字典格式化字符串
temp = '书名：%(name)s,价格：%(price)0.2f,出版社：%(publish)s'
book = {'name':'疯狂','price':88.9,'publish':'电子'}
print(temp%book)
book = {'name':'讲义','price':99.9,'publish':'电子'}
print(temp%book)


# In[ ]:




