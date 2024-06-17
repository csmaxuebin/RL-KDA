# This code is the source code implementation for the paper "RL-KDA: A K-degree Anonymity Algorithm Based on Reinforcement Learning."



## Abstract
K-degree anonymity is one of the privacy-preserving techniques and has gained attention in academia, industry, and government. Many social network data publishing algorithms based on K-anonymity techniques have been proposed,but most studies focus on static social networks. To address the existing problem of dynamic social networks, we propose a K-degree anonymity dynamic data publishing algorithm based on reinforcement learning. The algorithm ends with two phases: anonymization sequence and graph modification. In the anonymous sequence phase, this paper combines the idea of reinforcement learning and the characteristics of dynamic data change to build a reinforcement learning model for anonymous sequences. In this way, an ideal anonymous sequence can be created. We also propose a new strategy for graph modification, which selects edges according to degree centrality to generate anonymous graphs.Finally,experiments on real datasets show that this algorithm can reduce information loss and improve data utility.Paper access: [10.1109/COMPSAC57700.2023.00100](https://ieeexplore.ieee.org/document/10196930)

# References
```
@inproceedings{ma2023rl,
  title={RL-KDA: A K-degree Anonymity Algorithm Based on Reinforcement Learning},
  author={Ma, Xuebin and Xiang, Nan and Gao, Yulan},
  booktitle={2023 IEEE 47th Annual Computers, Software, and Applications Conference (COMPSAC)},
  pages={729--734},
  year={2023},
  organization={IEEE}
}
```
# Experimental Environment

```
Operating Environment: Python with Intel Core i5 CPU 1.8 GHz and 8 GB RAM, running MacBook.
-numpy 1.19.2
-collections 1.2.1
-random 1.1.1
-pandas 1.1.3
-networkx 2.5
-math 1.1.0
-Python 3.9
-torch==2.0.0
-torchvision~=0.15.1+cu117
```

# Datasets

`Polbooks,Ca-AstroPh,Ca-CondMat`

# Experimental Setup

### **Data Sets Used:**
   - Four real data sets were used in the experiments:
     - **NLTCS:** Long-term care research data from the United States.
     - **ACS:** Data from IPUMS-USA 2013 and 2014 ACS sampling.
     - **Adult:** 1994 US Adult Census data.
     - **BR2000:** Data from the 2000 Brazilian Census.

### **Evaluation Metrics:**
   - **α-way Query Accuracy:** Measures the accuracy and availability of the algorithm on high-dimensional data using α-way edge queries with α set to 2 and 3.
   - **SVM Classifier Accuracy:** Classification accuracy of results from synthetic data using SVM classifiers, predicting attributes relevant to each dataset.

### **Performance Metrics:**
   - **Run Time:** Comparison of running time between FAPrivBayes and JTFAPB algorithms on the four datasets to highlight efficiency improvements.

### Datasets Used:
1. **Polbooks**: A network of American political books.
2. **Ca-AstroPh**: An Arxiv dataset.
3. **Ca-CondMat**: Another Arxiv dataset.

### Algorithms Compared:
- **FKDA**: A representative algorithm for K-degree anonymous social graphs.
- **UMGA**: Another algorithm compared, details not specified in the excerpt.
- **Vertexadd**: A vertex addition method for graph anonymization.
- **KDVEM**: Details not specified.
- **TSRAM**: Uses a tree structure to generate a sequence of anonymity degrees and achieves privacy protection through node partitioning.
- **GA-KDA**: Combines community detection and genetic algorithms for graph anonymization.

# Experimental Analysis:
- The algorithms were compared on the basis of how well they preserve the graph structure and minimize the distortion compared to the original graph.
- The effectiveness of RL-KDA was particularly highlighted, showing better performance in retaining the original graph metrics (ACC, APL, T) compared to the other methods.
- The results are averaged over 10 experiments to ensure accuracy.

# Python Files

1. **ano_degreeSeq.py**:
   - This script could be involved in analyzing or modifying the degree sequence of nodes in a graph. "Degree sequence" refers to a list of degrees of the nodes in the graph, which anonymized or altered in some way by this script. Anonymization can involve making the sequence less identifiable to protect privacy.

2. **degreechange.py**:
   - This script deals with changes to the degree of nodes within a network or graph over time or under certain conditions. It is calculating the degree changes or implementing changes to study the effects on the graph's properties.

3. **GraphModification.py**:
   - This script modifies a graph structure. Modifications include adding or removing nodes or edges, altering weights of edges, or other transformations aimed at analyzing the impact on graph metrics or preparing data for further analysis.

4. **RLKDA.py**:
   -  The name suggests it is involve a specific algorithm or method, possibly related to machine learning or data analysis, where "RL" could refer to Reinforcement Learning and "KDA" could denote some form of Kernel Discriminant Analysis or another algorithmic approach. The script can implement or utilize this methodology for processing data.

5. **tree.py**:
   - This script is involve operations related to tree data structures. Common functionalities could include building trees, traversing trees, modifying tree nodes, or performing calculations such as finding the height, depth, or other properties of trees.

#  Experimental Results
**Figures 1(a), (b), and (c)**:
   - These sub-figures display the error evaluations of three algorithms—GA-KDA, TSRAM, and RL-KDA—across different metrics. Error evaluations are calculated by comparing the metrics of the anonymized graph to those of the original graph.

**Figure 1(d)**:
   - This plot primarily compares the edge differences between the UMGA and RL-KDA algorithms under varying values of the privacy parameter K. Edge difference is determined by calculating the difference in the number of edges between the original and the anonymized graphs.
![输入图片说明](https://github.com/csmaxuebin/RL-KDA/blob/main/pic/fig1.jpg)

Figure 2 from the experiment visually demonstrates how different graph anonymization algorithms perform in terms of maintaining structural characteristics of the Ca-AstroPh graph network as the privacy parameter K changes. The figure evaluates three algorithms: RL-KDA, FKDA, and a method labeled as VertexAdd,(ACC), (T), (APL).
![输入图片说明](https://github.com/csmaxuebin/RL-KDA/blob/main/pic/fig2.jpg)

Figure 3 provides an evaluation of how the privacy parameter K affects different graph metrics on the Ca-CondMat graph, examining algorithms such as RL-KDA, FKDA, and VertexAdd. Each sub-figure measures a different aspect of graph structure after anonymization processes.
![输入图片说明](https://github.com/csmaxuebin/RL-KDA/blob/main/pic/fig3.jpg)

# Update log
```
- {24.06.15} Uploaded overall framework code and readme file
```
