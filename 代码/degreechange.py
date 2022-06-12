#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pds
import networkx as nx
import random
import collections
import numpy as np
class changedegree:
    def deletedegree(self,k,d0):
        d0=list(d0)
         
        degreeC=collections.Counter(d0)
        degreeC=degreeC.items()
        degreeC=list(degreeC)
       
        m2, n2 = zip(*degreeC)
        m2=list(m2)
        n2=list(n2)
        s=[]
        v1=[]
      
      
        for i in range(len(m2)):
            if(n2[i]<k):#if 节点度的个数小于K，添加该节点度和度个数
                s.append(m2[i])
                v1.append(n2[i])
         
        t1=[]
        for i in range(len(s)):
              
                t=d0.index(m2[i])
                # print(t)
                t1.append(t)
                
      
        p=random.randint(0,len(t1)+1) 
       
        d0[p]=d0[p]-1
        return d0
    def adddegree(self,k,d):
        d=list(d)
        degreeC=collections.Counter(d)
        degreeC=degreeC.items()
        degreeC=list(degreeC)
        
        m3, n3 = zip(*degreeC)
        m3=list(m3)
        n3=list(n3)
        s1=[]
        s2=[]
        
      
        for i in range(len(m3)):
            if(n3[i]<k):#节点度的个数小于K，添加该节点度和度个数
                s1.append(m3[i])
                s2.append(n3[i])
        t1=[]
        for i in range(len(s1)):
              
                t=d.index(m3[i])
                t1.append(t)
        n3 = random.randint(0,len(d))
        d[n3]=d[n3]+1
        return d