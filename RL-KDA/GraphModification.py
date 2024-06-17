#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
from collections import deque
import networkx as nx
import random as rn
import numpy as np
import copy
import collections
import pandas as pds
import time
import tree as T
# import greedy as gd
import RLKDA as rl
import ano_degreeSeq as ano_dSeq 
 
nodesToAddEdge=[]
nodesToDeleteEdge=[]
 
edgeAdditionNumTries = 0
edgeSwitchNumTries = 0
 
dk=[]
 
 
# gk=g.copy()
# g 原图 gk 匿名图 d 度序列 dk 匿名度序列
class graphconstruct:
   def _init(self):
       self.dk=dk
def DCRegraphconstruct(g,dk,d0,a1):
    
    print("Starting graph reconstruction...")
 
    changesVector =[]
    permution=[]
    vd=zip(a1,dk)
    vd=list(vd)
    # print(len(vd)
    for i in range(len(dk)):
        
            s=dk[i]-d0[i]
            
            permution.append(vd[i][0])
             
            changesVector.append(s)
     
    for i in range(len(changesVector)):
   
    
    
            if (changesVector[i] < 0):
                
                nodesToDeleteEdge.append(permution[i])
               
            
            elif (changesVector[i] > 0):
                    nodesToAddEdge.append(permution[i])
                   
    print("addlen",len(nodesToAddEdge))
    print("deletelen",len(nodesToDeleteEdge))
    
    gk = graphconstruct()
    print("Original Graph  :",g.number_of_nodes(),"nodes,", g.number_of_edges(),"edges")
    print("Anonimized  Graph  :",gk.number_of_nodes(),"nodes,", gk.number_of_edges(),"edges")
    print("Graph reconstruction done!");

    return gk 
def graphconstruct():
        
    print("reconstructGraph: Starting graph reconstruction... [numEdges]=",g.number_of_edges(),"]")
    deleted = edgeDeletion()
    print("reconstructGraph: Deleted ", deleted,"edges [numEdges=",gk.number_of_edges(),"]" )
    added = edgeAddition()
    print("reconstructGraph: Added ", added,"edges [numEdges=",gk.number_of_edges(),"]" )
    changed = edgeSwitch()
    print("reconstructGraph: Changed ",changed ,"edges [numEdges=",gk.number_of_edges(),"]" )
    
    return gk
def  edgeDeletion():
    removed=0
   
    while(len(nodesToDeleteEdge)>len(nodesToAddEdge)):
   
        if(oneEdgeDeletion()!=True):
            print("edgeDeletion: NO EDGE HAS BEEN REMOVED!")
      
        else:
           removed=removed+1
           print("edgeDeletion: EDGE HAS BEEN REMOVED!")   
     
    return removed
def doEdgeDeletion(vi, vj, vk, vl,score):
        numEdgesBefore = gk.number_of_edges()
        gk.remove_edge(vi, vk)
        gk.remove_edge(vj, vl)
        gk.add_edge(vk, vl)
        nodesToDeleteEdge.remove(vi)
        nodesToDeleteEdge.remove(vj)
        numEdgesAfter=gk.number_of_edges()
        if((numEdgesBefore-1)!= numEdgesAfter):
          print("doEdgeDeletion: WRONG NUMBER OF EDGES!")
def  edgeAddition():
        added = 0
        
        print("edgeAddition: *** Starting edge addition...")

       
        while(len(nodesToDeleteEdge)<len(nodesToAddEdge)):
        
             if(oneEdgeAddition()!=True):
               
                  print("edgeAddition: NO EDGE HAS BEEN ADDED!")
               
             
             else:
              
                 added=added+1
              
        return added
    
def  doEdgeAddition(vi, vj,score):
       
        gk.add_edge(vi, vj)
        

        nodesToAddEdge.remove(vi)
        nodesToAddEdge.remove(vj)
 
 # Change edges to reduce/increase degree of nodes
 
def  edgeSwitch():
        
        changed = 0
        n = gk.number_of_edges()
        
        print("edgeSwitch: *** Starting edge switch...") 

       
        while (len(nodesToDeleteEdge)> 0):

            
            vi = nodesToDeleteEdge[0]
            

            # // edge switch on 'vi'
            if(oneEdgeSwitch(vi)!=False):
                print("edgeSwitch: NO EDGE HAS BEEN SWITCHED!")
            
            else: 
              
              nodesToDeleteEdge.remove(vi)  
                        
              changed =changed+1
            
            
           

        print("edgeSwitch  : number of tries", edgeSwitchNumTries)

        return changed
    
    
 
    
def  doEdgeSwitch(vi,vk, vj,score):
         
        
        gk.remove_edge(vi, vk)
        
        gk.add_edge(vk, vj)
        # gk.add_edge(vj, vk)
       
        d1 =[d for n, d in gk.degree()] 
      
        nodesToAddEdge.remove(vj)
 
def oneEdgeDeletion():
        edgeDeletionNumTries=0
        i = 0
        while (i < len(nodesToDeleteEdge)):
            vi = nodesToDeleteEdge[i]
         
            
            vks=list(gk[vi])
            
          
            j=i+1
            while (j <len(nodesToDeleteEdge)):
                
                vj = nodesToDeleteEdge[j] 
                
                for vk in vks:
                 
                    
                    vls = list(gk[vj])
                
                for vk in vks:
                  
                    for vl in vls:
                  
                        
                       
                        if (vk!=vl and (gk.has_edge(vk, vl)!=False)):
                       
                               doEdgeDeletion(vi, vj, vk, vl, -1)

                            # // number of tries
                               edgeDeletionNumTries+=1
                        
                        
                               
                            # print("edgeDeletionNumTries",edgeDeletionNumTries)
                               return True
                j = j + 1
                      
            i=i+1
        return False
    
 
    #  Edge Addition 
    
def  oneEdgeAddition():
        edgeAdditionNumTries=0
        i = 0;
        while (i<len(nodesToAddEdge)):
            
            vi = nodesToAddEdge[i]
            # print("vi",vi)
            j = i + 1
           
            while (j < len(nodesToAddEdge)):
                
                vj = nodesToAddEdge[j]
                # print("vj",vj)
                if ((vi != vj) and gk.has_edge(vi, vj)!=True):
                    doEdgeAddition(vi, vj, -1)

                    # // number of tries
                    edgeAdditionNumTries+=1
            
                    return True
                j=j+1
            
           
            i=i+1
        

        return False
    

 
def oneEdgeSwitch(vi):
       
        edgeSwitchNumTries=0
        vks = list(gk[vi])
       

        for vk in  vks:
            for vj in nodesToAddEdge:
               
                if (vi != vj and vk != vj and (vj in list(gk[vi]))!=True):
                    
                 
                    doEdgeSwitch(vi, vk, vj, -1)
                  
                    edgeSwitchNumTries+=1
                    
                    return True
                
            
        

        return False
 
    
    

 
        
if __name__=="__main__": 
    
    datafile = pds.read_csv("datasets/FB.csv", header=None)
    
    datafile=datafile.values
   
   
    g=nx.Graph()
    g.add_edges_from(datafile)
    s=[]
    m=nx.degree_centrality(g) 
    m1=sorted(m.items(),key = lambda x:x[1])
   
    a1=[n for n, d in m1]
     
    odered_degree_sequence=sorted([d for n, d in g.degree()],reverse=True)
    gk=g.copy()
  
    degreeCount = collections.Counter(odered_degree_sequence)
   
    degreeCount=degreeCount.items()
    degreeCount=list(degreeCount)
    attempt=1
    noise=1
    t=T.HuffmanTree()
    data=t.PrintTree(degreeCount)
    data.reverse()
    a=[x[1] for x in data]
    b=[y[0] for y in data]
    
    start=time.time()
    tree=ano_dSeq.Tree()
    for i in range(len(b)):
    
        tree.add(b[i],a[i])
     
    k=2
    n=tree.Seq(tree.root,k)
    
    anonymised_sequence=tree.partion(n)
  
    dv = [(d,v) for v, d in g.degree()]
   
    attempt = 1
    anonymised_sequence=tree.seq_partion(anonymised_sequence,g,k)
    if np.sum(anonymised_sequence) % 2 != 0:
        print("添加噪声")
        d1 = tree.probing(anonymised_sequence,noise)
    else:
        d1=anonymised_sequence
   
    degreeC = collections.Counter(d1)
    degreeC=degreeC.items()
    degreeC1=list(degreeC)
   
    m2,n2=zip(*degreeC)
    k1=k+1
    
    f=sum(x<k1 for x in n2)
     
     
    
    if(f==0):#上一时刻度的匿名要求满足这一时刻度的匿名要求
         s1=d1
    else:
        s1=rl.run(f, k1, odered_degree_sequence, d1)
    nn=[]
    nn1=[]
    
    vd = [(v,d) for v, d in g.degree()]
    
    vd.sort(key=lambda tup: tup[1], reverse=True)
    
    dk=[n for n, d in vd]#原始节点顺序
    d0=[d for n, d in vd]#
    
    start=time.time()
    tree=ano_dSeq.Tree()
   
    print("a===",len(a1)) #按度中心排序的节点顺序
     
    for k,element in enumerate(s1):
     
      for i in range(len(a1)):
        if a1[k]==dk[i]: 
            nn1.append(d0[i])
            nn.append(s1[i])
    
    
    
    gk=DCRegraphconstruct(g,nn,nn1,a1) 
    s=[]
    l=[]
    for C in (gk.subgraph(c).copy() for c in nx.connected_components(gk)):
        # print("最短平均路径",nx.average_shortest_path_length(C))
        l.append(nx.average_shortest_path_length(C))
    print("度中心方法-最短平均路径",max(l))
    # print("平均聚类系数(average clustering): ", nx.average_clustering(g))
    print("度中心方法-平均聚类系数(average clustering): ", nx.average_clustering(gk))
    print("度中心方法-网络传递性(transitivity): ", nx.transitivity(gk))
    # l1=[]
    print("k,k1",k,k1)
 