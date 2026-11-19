import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("Wholesale.csv")
df.loc[len(df)+1, "Milk"] = 2300
X = df[["Milk"]]

model = KMeans(n_clusters=4, n_init=10, random_state=42)

df["Cluster"] = model.fit_predict(X)

print(df[["Channel", "Milk", "Cluster"]])

print("\nCluster Counts:")
print(df["Cluster"].value_counts().sort_index())

names = {
    0: "c1",
    1: "c2",
    2: "c3",
    3: "c4"
}

df["Cluster_Name"] = df["Cluster"].map(names)

print("\nCluster Names:")
print(df[["Milk", "Cluster", "Cluster_Name"]])
