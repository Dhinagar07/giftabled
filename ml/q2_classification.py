from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier


wine = load_wine()
X = wine.data
y = wine.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("Raw:")

lr = LogisticRegression(max_iter=1000, random_state=42)
lr.fit(X_train, y_train)
lr_raw = accuracy_score(y_test, lr.predict(X_test))
print(f"LR: {lr_raw:.4f}")

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
knn_raw = accuracy_score(y_test, knn.predict(X_test))
print(f"KNN: {knn_raw:.4f}")

tree = DecisionTreeClassifier(random_state=42)
tree.fit(X_train, y_train)
tree_raw = accuracy_score(y_test, tree.predict(X_test))
print(f"DT: {tree_raw:.4f}")

forest = RandomForestClassifier(n_estimators=100, random_state=42)
forest.fit(X_train, y_train)
forest_raw = accuracy_score(y_test, forest.predict(X_test))
print(f"RF: {forest_raw:.4f}")

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Scaled:")

lr2 = LogisticRegression(max_iter=1000, random_state=42)
lr2.fit(X_train_scaled, y_train)
lr_scaled = accuracy_score(y_test, lr2.predict(X_test_scaled))
print(f"LR: {lr_scaled:.4f}")

knn2 = KNeighborsClassifier(n_neighbors=5)
knn2.fit(X_train_scaled, y_train)
knn_scaled = accuracy_score(y_test, knn2.predict(X_test_scaled))
print(f"KNN: {knn_scaled:.4f}")

print("KNN gain:", f"{knn_raw:.4f} -> {knn_scaled:.4f}")
print("LR gain:", f"{lr_raw:.4f} -> {lr_scaled:.4f}")

print("Model  Raw  Scaled")
print(f"LR  {lr_raw:.4f}  {lr_scaled:.4f}")
print(f"KNN  {knn_raw:.4f}  {knn_scaled:.4f}")
print(f"DT  {tree_raw:.4f}  {tree_raw:.4f}")
print(f"RF  {forest_raw:.4f}  {forest_raw:.4f}")
