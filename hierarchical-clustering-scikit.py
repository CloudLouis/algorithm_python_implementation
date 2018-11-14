import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.cluster.hierarchy as sch
import scipy.spatial.distance as ssd
from sklearn.cluster import AgglomerativeClustering


def cophenet(model, X):
    children = model.children_

    distance = np.arange(children.shape[0])

    no_of_observation = np.arange(2, children.shape[0]+2)

    linkage_matrix = np.column_stack([children, distance, no_of_observation]).astype(float)
    print(sch.cophenet(linkage_matrix, ssd.pdist(X, metric="euclidean")))


X = np.array([[4, 13, 6], [14, 9, 10], [8, 6, 15], [6, 7, 9], [0, 5, 7], [5, 6, 13], [10, 9, 5],
              [5, 8, 10], [10, 12, 14], [3, 0, 5]])


for i in range(0, X.shape[0]):
    for y in range(i+1, X.shape[0]):
        print ("Dissimilarity between ", i+1," and", y+1,": ",
            np.linalg.norm(X[i]-X[y])
        )
print("\n\n")
"""for i in range(0, X.shape[0]):
    for y in range(i+1, X.shape[0]):
        print ("Similarity between ", i+1," and", y+1,": ",
            1/((np.linalg.norm(X[i]-X[y])-1))
        )"""

plt.figure(figsize=(10,7))
plt.title("Test")
Z = sch.linkage(X, method="single", metric="euclidean")
print(Z)
print(sch.cophenet(Z, ssd.pdist(X, metric="euclidean")))
sch.dendrogram(Z)
plt.show()


