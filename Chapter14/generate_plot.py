import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

from sklearn.preprocessing import normalize
data_scaled = normalize(data)
data_scaled = pd.DataFrame(data_scaled, columns=data.columns)
data_scaled.head()

import scipy.cluster.hierarchy as shc
plt.figure(figsize=(12, 8))  
plt.title("Hierarchical Clustering Dendrograms Example")  
dend = shc.dendrogram(shc.linkage(data_scaled, method='ward'))
plt.xlabel("Individual Records Position in Hierarchy")
plt.ylabel("Distance between Records")

plt.savefig('dendrograms.png',  dpi=300)
