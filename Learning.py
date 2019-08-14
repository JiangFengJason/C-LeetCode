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


# In[36]:


s_max=input("请输入您想计算的阶乘：")
mx=int(s_max)
result=1
for num in range(1,mx+1):
    result*=num
print(result)


# In[38]:


number=1
if isinstance(number,int):
    print(True)
    


# In[39]:


src_list=[12,45,'crazy']
for item in src_list:
    if isinstance(item,int):
        print(item)


# In[41]:


a_list=[330,1.4,20,'fake']
for i in range(len(a_list)):
    print("第%d个元素是%s"%(i+1,a_list[i]))
    


# In[44]:


a= ['a','b','c']
b=[1,2,3]
c=[0.1,0.2]
for x in zip(a,b,c):
    print(x)


# In[3]:


SIZE=7
array=[[0]*SIZE]
j=0
k=0
for i in range(SIZE-1):
    array +=[[0]*SIZE]
orient=0
for i in range(1,SIZE*SIZE+1):
    array[j][k]=i
    if j+k==SIZE-1:
        if j>k:
            orient=1
        else :
            orient=2
    elif (k==j)and (k>SIZE/2):
        orient=3
    elif (j==k-1) and (k<=SIZE/2):
        orient=0
    
    if orient ==0:
        j+=1
    elif orient==1:
        k+=1
    elif orient==2:
        k-=1
    elif orient==3:
        j-=1
for i in range(SIZE):
    for j in range(SIZE):
        print('%02d '%array[i][j],end="")
    print("")


# In[1]:


def test(a,*books):
    for b in books:
        print(b)
    print(a)
test(5,"疯狂","讲义")


# In[2]:


def foo(name,*nums):
    print("name参数：",name)
    print("nums参数：",nums)
my_list=[1,2,3]
foo('kit',*my_list)


# In[3]:


def getmap(data,fn):
    result=[]
    for e in data:
        result.append(fn(e))
    return result
def square(n):
    return n*n
def cub(n):
    return n*n*n
def factorial(n):
    result=1
    for index in range(2,n+1):
        result*=index
    return result
data=[3,4,5,6]
print("原数据：",data)
print("计算数组元素的平方")
print(getmap(data,square))
print("计算数组元素的立方")
print(getmap(data,cub))
print("计算数组元素的阶乘")
print(getmap(data,factorial))


# In[5]:


class Person:
    hair='black'
    def __init__(self,name='Charlie',age=8):
        self.name=name
        self.age=age
    def say(self,content):
        print(content)
p=Person()
print(p.name,p.age)
p.name='jack'
print(p.name,p.age)


# In[6]:


class Bird:
    @classmethod
    def fly(cls):
        print('类方法fly:',cls)
    @staticmethod
    def info(p):
        print('静态方法info:',p)
Bird.fly()
Bird.info('crazy')
b=Bird()
b.fly()
b.info('fkit')


# In[8]:


class User:
    def __hide(self):
        print('示范隐藏的hide方法')
    def getname(self):
        return self.__name
    def setname(self,name):
        if len(name)<3 or len(name)>8:
            raise ValueError('用户名长度必须在3~8之间')
        self.__name=name
    name=property(getname,setname)
u=User()
u.name='fk'


# In[10]:


class Dog:
    # 只能动态添加slots里面定义好的函数或者变量名
    __slots__=('walk','age','name')
    def __init__(self,name):
        self.name=name
    def test():
        print('预先定义的test方法')
d=Dog('Snoopy')
from types import MethodType
d.walk=MethodType(lambda self: print('%s正在慢慢地走'%self.name),d)
d.age=5
d.walk()
#d.foo=30


# In[16]:


import numpy as np
a=np.arange(0,72)
a.reshape((4,3,3,2))
print(a)


# In[28]:


import enum
class Orientation(enum.Enum):
    EAST='东'
    SOUTH='南'
    WEST='西'
    NORTH='北'
print(Orientation.EAST.name)
print(Orientation.EAST.value)


# In[30]:


class Apple:
    def __init__(self,color,weight):
        self.color=color
        self.weight=weight
    def __repr__(self):
        return "Apple:color="+self.color+",weight="+str(self.weight)
a=Apple("红色",5.68)
print(a)


# In[ ]:




