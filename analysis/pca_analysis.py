import numpy as np
from sklearn.decomposition import PCA

# PCA HELPS US TO REDUCE THE NUMBER OF FEATURES OF A DATASET BY KEEPING THE MOST IMPORTANT FEATURES
# THIS USES LINEAR ALGEBRA AND EIGEN VALUES TO GET THE HIGHEST EIGENVALUE WHICH CONTAINS THE MOST IMPORTANT FEATURES

def run_pca(embeddings, n_components=10):
    pca = PCA(n_components=n_components)
    reduced = pca.fit_transform(embeddings)
    return reduced, pca.explained_variance_ratio_
