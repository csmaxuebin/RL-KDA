#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque
import networkx as nx
import math
import random as rn
import numpy as np
import copy
import collections
import pandas as pds

#节点类
class Node:
    def __init__(self,degree=None, degree_count=None):
        
        self.d=degree #节点度
        self.dc=degree_count#节点度的个数
        self.left = None #节点左孩子
        self.right = None #节点右孩子
        self.father = None # 节点父节点
        self.child=None
        
  
    def is_left_child(self):
        return self.father.left == self

#创建最初的叶子节点
 
class HuffmanTree(object):

    #根据Huffman树的思想：以叶子节点为基础，反向建立Huffman树
    def PrintTree(self,data_set):
        
        self.a=[Node(part[0],part[1]) for part in data_set] 
        m=[]
       
        for i,d in enumerate(self.a):
          m.append([self.a[i].d,self.a[i].dc])
        m.sort(key=lambda tup:tup[0],reverse=True)
        # print(m)
        b1=[]
        c=[]
        k=[]
        self.a.sort(key=lambda node:node.d,reverse=True)
        
        if(len(self.a)%2!=0):
        
          m.sort(key=lambda tup:tup[0],reverse=True)
          nn1=self.a.pop()
          k=self.get_tree(self.a)
          last=m.pop()
        
          m.extend(k)
        
        else:
        
           k=self.get_tree(self.a)
        
           m.extend(k)
        return m
    def get_tree(self,a):
        b1=[] 
        
        while len(self.a)!=1:
            
          
            if(self.a[0].dc>self.a[1].dc):#self.a[0]第一个数，self.a[1]第二个数
                       # degree=self.a[0].d
                      degree=int(math.ceil(((self.a[1].dc*self.a[1].d)+(self.a[0].dc*self.a[0].d))/(self.a[0].dc+self.a[1].dc)))
            elif(self.a[0].dc<self.a[1].dc):
                       degree=self.a[1].d
                      # degree=int(math.floor(((self.a[1].dc*self.a[1].d)+(self.a[0].dc*self.a[0].d))/(self.a[0].dc+self.a[1].dc)))
            elif(self.a[0].dc==self.a[1].dc):
                 degree=int((self.a[0].d+self.a[1].d)/2)
            degree_count=(self.a[1].dc+self.a[0].dc)
           
            degree=int(degree)
            
            c=Node(degree,degree_count)
            c.left=self.a.pop(0)#c.left为队列的（5，1） 
        
            c.right=self.a.pop(0)#c.right为队列的（4，2）
            
            b1.append([c.d,c.dc])
           
           
            self.a.append(c)
        if(len(self.a)%2!=0):
          self.a.sort(key=lambda node:node.d,reverse=True) 
          
        return b1
     