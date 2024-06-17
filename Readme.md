# This code is the source code implementation for the paper "RL-KDA: A K-degree Anonymity Algorithm Based on Reinforcement Learning."



## Abstract
K-degree anonymity is one of the privacy-preserving techniques and has gained attention in academia, industry, and government. Many social network data publishing algorithms based on K-anonymity techniques have been proposed,but most studies focus on static social networks. To address the existing problem of dynamic social networks, we propose a K-degree anonymity dynamic data publishing algorithm based on reinforcement learning. The algorithm ends with two phases: anonymization sequence and graph modification. In the anonymous sequence phase, this paper combines the idea of reinforcement learning and the characteristics of dynamic data change to build a reinforcement learning model for anonymous sequences. In this way, an ideal anonymous sequence can be created. We also propose a new strategy for graph modification, which selects edges according to degree centrality to generate anonymous graphs.Finally,experiments on real datasets show that this algorithm can reduce information loss and improve data utility.Paper access: 10.1109/COMPSAC57700.2023.00100


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
- torchvision~=0.15.1+cu117
```

# Datasets

`Polbooks,Ca-AstroPh,Ca-CondMat`

# Experimental Setup
### 1. **Algorithm Description:**
   - **FAPrivBayes Algorithm:** Improves the speed of Bayesian network generation by determining the order of nodes based on node weighting, reducing the time and overhead required.
   - **JTFAPB Algorithm:** Uses the JTree algorithm to modify the Bayesian network structure created by FAPrivBayes, reducing the number of subnets and thus enhancing the privacy budget allocation across the network.

### 2. **Data Sets Used:**
   - Four real data sets were used in the experiments:
     - **NLTCS:** Long-term care research data from the United States.
     - **ACS:** Data from IPUMS-USA 2013 and 2014 ACS sampling.
     - **Adult:** 1994 US Adult Census data.
     - **BR2000:** Data from the 2000 Brazilian Census.

### 3. **Evaluation Metrics:**
   - **α-way Query Accuracy:** Measures the accuracy and availability of the algorithm on high-dimensional data using α-way edge queries with α set to 2 and 3.
   - **SVM Classifier Accuracy:** Classification accuracy of results from synthetic data using SVM classifiers, predicting attributes relevant to each dataset.

### 4. **Performance Metrics:**
   - **Run Time:** Comparison of running time between FAPrivBayes and JTFAPB algorithms on the four datasets to highlight efficiency improvements.

### 5. **Procedure:**
   - The experiments involved executing the above algorithms on the datasets, measuring α-way query accuracy, SVM classification accuracy, and running time. The results were averaged over multiple runs to ensure reliability.

### 6. **Outcome:**
   - The JTFAPB algorithm showed significant improvements in data usability and privacy over the FAPrivBayes and other previous algorithms. The privacy budget allocation per subnet was more efficient, leading to reduced noise levels in the data.

This experimental setup was crucial for validating the effectiveness and efficiency of the JTFAPB algorithm in maintaining differential privacy while handling high-dimensional datasets. Experimental Setup
The experimental setup includes using various datasets and algorithms to evaluate the effectiveness of RL-KDA. The following are the key components of the experimental setup:

### Datasets Used:
1. **Polbooks**: A network of American political books.
2. **Ca-AstroPh**: An Arxiv dataset.
3. **Ca-CondMat**: Another Arxiv dataset.

### Evaluation Metrics:
- **Transitivity (T)**: Measures the ratio of the triangles to triplets in the graph.
- **Average Clustering Coefficient (ACC)**: The average likelihood of nodes in a graph to cluster together.
- **Average Path Length (APL)**: The average shortest path length between all pairs of nodes in the graph.

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
   - 
#  Experimental Results
![输入图片说明](/imgs/2024-06-16/ptRhoSn9YP22ESx2.png)
1. **Figures 1(a), (b), and (c) **:
   - These sub-figures display the error evaluations of three algorithms—GA-KDA, TSRAM, and RL-KDA—across different metrics. Error evaluations are calculated by comparing the metrics of the anonymized graph to those of the original graph, as described by Equation (8).
   - The results show that RL-KDA generally outperforms the other two algorithms across these metrics. For example, in Figure 1(b), RL-KDA maintains an error below 0.02, whereas GA-KDA has errors above 0.1, and TSRAM's errors range between 0.02 and 0.04.
2. **Figure 1(d)**:
   - This plot primarily compares the edge differences between the UMGA and RL-KDA algorithms under varying values of the privacy parameter K. Edge difference is determined by calculating the difference in the number of edges between the original and the anonymized graphs.
   - The results indicate that neither algorithm needs to add extra edges when K is between 5 and 25. However, at K=50, the edge difference for UMGA is twice that of RL-KDA, demonstrating that RL-KDA better preserves the original graph structure at higher values of K.

Overall, this experiment evaluates the performance of graph anonymization algorithms under different strengths of privacy protection, emphasizing the advantage of the RL-KDA algorithm in maintaining graph structure. This is crucial for selecting suitable graph anonymization techniques to ensure data privacy while minimizing the impact on data utility.

![输入图片说明](/imgs/2024-06-16/rYawiKXlj95mJril.png)
Figure 2 from the experiment visually demonstrates how different graph anonymization algorithms perform in terms of maintaining structural characteristics of the Ca-AstroPh graph network as the privacy parameter K changes. The figure evaluates three algorithms: RL-KDA, FKDA, and a method labeled as VertexAdd, across different metrics—Average Clustering Coefficient (ACC), Transitivity (T), and Average Path Length (APL).

1. **Figure 2(a) - Average Clustering Coefficient (ACC):**
   - This graph shows the ACC across varying values of K. It illustrates that the ACC for FKDA decreases as K increases. However, all three methods do not sufficiently mimic the original graph's ACC, indicating an overestimation in clustering coefficients compared to the original graph.

2. **Figure 2(b) - Transitivity (T):**
   - In this chart, RL-KDA closely aligns with the transitivity of the original graph across different values of K, indicating that RL-KDA preserves the global connectivity pattern better than the other algorithms.

3. **Figure 2(c) - Average Path Length (APL):**
   - Here, RL-KDA closely matches the APL of the original graph, suggesting that it maintains path distances within the graph more effectively than other methods.

Overall, the results from these experiments suggest that RL-KDA outperforms the other tested algorithms in terms of preserving the structural properties of the original graph while anonymizing it, thereby ensuring higher data utility for the anonymized graphs. This makes RL-KDA a preferable choice when considering graph anonymization techniques that aim to maintain the utility of the graph data.

![输入图片说明](/imgs/2024-06-16/dRd4qx2JMUNTKYC3.png)

Figure 3 provides an evaluation of how the privacy parameter K affects different graph metrics on the Ca-CondMat graph, examining algorithms such as RL-KDA, FKDA, and VertexAdd. Each sub-figure measures a different aspect of graph structure after anonymization processes:

1. **Figure 3(a) - Average Clustering Coefficient (ACC):**
   - This graph shows that the ACC for RL-KDA closely aligns with that of the original graph throughout the range of K values, indicating that RL-KDA maintains the clustering characteristics effectively because it does not introduce new edges to the graph.

2. **Figure 3(b) - Transitivity (T):**
   - It depicts that transitivity decreases notably when K is greater than or equal to 15. This decrease is attributed to the fluctuations caused by edge switching, which impacts the global connectivity and thus the transitivity of the graph.

3. **Figure 3(c) - Average Path Length (APL):**
   - This plot shows how the APL metric changes with different K values after the graph has been anonymized. There is a slight decrease in APL at K=15 for RL-KDA, due to random modifications in the graph that result in the removal of some critical edges, affecting the shortest paths between nodes.

Overall, these results highlight the varying impacts of graph anonymization techniques on the structural integrity and characteristics of the Ca-CondMat graph. RL-KDA, in particular, is noted for its ability to preserve the original graph's clustering coefficients effectively while causing minimal disruption to the average path length, albeit with some decrease due to the necessary random edge modifications for achieving anonymity.






In a word, it can be found that RL-KDA is closer to the metrics of the original graph than other algorithms through comparison experiments. The reason why RL-KDA has advantages over the other four algorithms is that it reduces the information loss in the process of anonymity sequence, solves the problem of low data utility from the essence of the problem, and combines the new graph modification algorithm to improve data utility.
```
## Update log

```
- {24.06.15} Uploaded overall framework code and readme file
```

