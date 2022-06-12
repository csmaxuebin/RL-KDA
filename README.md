# RL-KDA
一.	代码介绍

本篇代码将强化学习应用到动态社交图数据发布过程中。针对匿名度序列生成问题，在生成匿名度序列过程中发现信息损失最小的匿名度序列；在图修改算法中，则根据节点的度中心性对节点排序，对节点的边进行操作生成匿名图。（边操作源代码来源于2017 UMGA算法）

二.	运行环境及依赖包版本

运行环境： Python with Intel Core i5 CPU 1.8 GHz  and 8 GB RAM, running MacBook。

包                      版本

numpy                 1.19.2

collections              1.2.1

random                 1.1.1

pandas                 1.1.3

networkx                2.5

math                   1.1.0

三. 类的作用

GraphConstruct 是对边进行操作，生成匿名图

tree 根据原始度序列生成树

get_tree函数是生成树

ano_degreeSeq 通过DFS遍历确定最终的匿名度序列

probing函数加噪声

edgeDeletion 删除边

edgeAddition 添加边

edgeSwitch   交换边

RLKDA 在生成匿名度序列过程中发现信息损失最小的匿名度序列

GraphModification.py 根据节点的度中心性对节点排序，对节点的边进行操作生成匿名图。

degreechange.py 判断添加度还是减少度

四.	具体注释详见代码
