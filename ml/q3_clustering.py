from itertools import permutations

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler


wine = load_wine()
X = wine.data
y = wine.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)

cross_tab = pd.crosstab(y, clusters, rownames=["Actual class"], colnames=["Cluster"])
print("K-Means:")
print(cross_tab)

best = 0
for permutation in permutations(range(3)):
    matched = sum(cross_tab.iloc[i, permutation[i]] for i in range(3))
    if matched > best:
        best = matched

print("Accuracy:", round(best / len(y), 4))
