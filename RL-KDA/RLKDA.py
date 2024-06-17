
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import pandas as pds
import networkx as nx
 
import random
import numpy as np
from random import choice
import degreechange
import math
from collections import deque
import networkx as nx
 
import copy
import collections
import pandas as pds
import time
# import kdegree as kd
import tree as T
import ano_degreeSeq as ano_dSeq 

#K=t时刻的匿名情况

c=degreechange.changedegree()
N_STATES=['larger','smaller','no change']#状态分为三种
ACTIONS=['add','sub']#执行动作
REWARD=[]#奖励
ALPHA=0.1
GAMA=0.9
a=[]
S=[]
EPSILON=[]
A=np.random.choice(ACTIONS)
class RL:
   def __init__(self,learning_rate=0.01, reward_decay=0.9):
       
       self.ALPHA= learning_rate
       self.GAMA = reward_decay

   # s=N_STATES
# 第一个发布数据时间点
     
 
   def train(self,dk,d0,k1):
    s=N_STATES
    if(sum(dk)<sum(d0)):
        
       if A=='add':
           d1=c.adddegree(k1,dk)
           dis_2=abs(sum(d1)-sum(d0))
           s='smaller'
           R=1
       else:
           d1=c.deletedegree(k1,dk)
           dis_2=abs(sum(d1)-sum(d0))
           s='larger'
           R=-1
    if(sum(dk)>sum(d0)):
       if A=='add':
           d1=c.adddegree(k1,dk)
           dis_2=abs(sum(d1)-sum(d0))
           s='larger'
           R=-1
       else:
           d1=c.deletedegree(k1,dk)
           dis_2=abs(sum(d1)-sum(d0))
           s='smaller'
           R=1

    a.append(A)
    S.append(s)
    REWARD.append(R)#奖励数组
    EPSILON.append(dis_2)
    return d1

def chooseaction(s,dis_1,d4,k1,d0,dk):
       
        if(sum(dk)>sum(d0)):#若dk>原始度序列
            if s=='larger':
                A='sub'
                d2=c.deletedegree(k1,d4)
                dis_2=abs(sum(d2)-sum(d0))
                s='smaller'
                R=1
            elif s=='smaller':
                A='add'
                d2=c.adddegree(k1,d4)
            
                dis_2=abs(sum(d2)-sum(d0))
                
                s='larger'
                R=-1
            else:
                    R=0
                    s='no change'
        if(sum(dk)<sum(d0)):#若dk>原始度序列
            if s=='larger':
                A='add'
                d2=c.adddegree(k1,d4)
                # print("add**",sum(d2))
                dis_2=abs(sum(d2)-sum(d0))
                s='smaller'
                R=1
                # else:
                     
                #     s='larger'
                #     R=-1
            elif s=='smaller':
                A='sub'
                d2=c.deletedegree(k1,d4)
            # print("add**",sum(d1))
            # print("d122222",d1)
                dis_2=abs(sum(d2)-sum(d0))
                # print("**",sum(d1))
        # print("dict2=",dis_2)
                # if dis_1>dis_2:
                s='larger'
                R=-1
                # else:
                    # s='smaller'
                    # R=1
            else:
                    R=0
                    s='no change'
    
        S.append(s)
        a.append(A)
        REWARD.append(R)
        EPSILON.append(dis_2)
       
        return d2
def run(f,k1,d0,dk):#dk为第一次匿名，d0为原始序列，d1为第一随机加减度
    r1=RL()
    d3=[]
    dis_1=abs(sum(dk)-sum(d0))
    d1=r1.train(dk,d0,k1)
 
    for j in range(10):
 
        if f==0:
            print("新的度序列完成")
        elif(f!=0):
         
      
            d3=chooseaction(S[j],dis_1,d1,k1,d0,dk)
          
            degreeC=collections.Counter(d3)
            degreeC=degreeC.items()
            degreeC=list(degreeC)
      
            m2, n2 = zip(*degreeC)
            f=sum(x<k1 for x in n2)
    
    return d3
q=np.zeros(len(REWARD))
def learn(self):
    for i in range(len(REWARD)-1):
      
         r=REWARD[i]
    
         r_1=REWARD[i+1]
      
         q[i+1]=r+ALPHA*(r_1+GAMA*max(q)-q[i])
     
    return max(q)
 