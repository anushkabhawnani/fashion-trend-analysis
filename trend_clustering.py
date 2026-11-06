import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Load embeddings + dates
data = np.load("features/global_data.npz", allow_pickle=True)
embeddings = data["embeddings"]
dates = pd.to_datetime(data["dates"])

# PCA
pca = PCA(n_components=10)
reduced = pca.fit_transform(embeddings)

# Clustering
k = 5  # number of style clusters
kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(reduced)

# Build dataframe
df = pd.DataFrame(reduced, columns=[f"PC{i+1}" for i in range(10)])
df["date"] = dates
df["cluster"] = clusters

# Monthly cluster proportions
monthly = (
    df
    .set_index("date")
    .groupby("cluster")
    .resample("M")
    .size()
    .unstack(0)
    .fillna(0)
)

monthly_prop = monthly.div(monthly.sum(axis=1), axis=0)

# Plot trend evolution
plt.figure()
for c in monthly_prop.columns:
    plt.plot(monthly_prop.index, monthly_prop[c])
plt.title("Global Fashion Trend Clusters Over Time")
plt.xlabel("Time")
plt.ylabel("Proportion")
plt.show()

from sklearn.metrics.pairwise import cosine_similarity

# Cluster centroids
centroids = kmeans.cluster_centers_

# Cosine similarity between styles
similarity = cosine_similarity(centroids)

# Visualize similarity matrix
plt.figure()
plt.imshow(similarity)
plt.colorbar()
plt.title("Global Style Similarity Between Clusters")
plt.show()
