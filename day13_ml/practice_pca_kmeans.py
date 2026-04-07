# ================================
# PCA + KMeans Practice
# ================================

from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# 고차원 데이터 느낌 (3차원)
X = [
    [2, 3, 100],
    [3, 4, 120],
    [10, 10, 900],
    [11, 11, 950],
    [1, 0, 80]
]

# 1. 차원축소 (3차원 -> 2차원)
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

print("차원축소 결과:")
for x in X_reduced:
    print(x)

print("설명된 분산 비율:")
print(pca.explained_variance_ratio_)
print("설명된 분산 비율 합:")
print(sum(pca.explained_variance_ratio_))

# 2. 클러스터링
model = KMeans(n_clusters=2)
model.fit(X_reduced)

print("labels:", model.labels_)
print("cluster centers:")
print(model.cluster_centers_)