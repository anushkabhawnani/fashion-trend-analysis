import pandas as pd
import numpy as np

# EMBEDDINGS ARE DENSE VECTOR REPRESENTATIONS OF THESE IMAGES, THE IMAGES ARE REDUCED AND THEN EMBEDDED TO REDUCE THE DIMENSIONALITY OF THESE IMAGES

def build_time_series(pca_embeddings, dates, freq="M"):
    """
    pca_embeddings: (N, k)
    dates: datetime64[D]
    freq: 'M' for monthly, 'W' for weekly
    """
    # REPRESENTING THE PC EMBEDDINGS WITH THEIR COMPONENTS

    df = pd.DataFrame(pca_embeddings, columns=[f"PC{i+1}" for i in range(pca_embeddings.shape[1])]) # WITDH
    df["date"] = pd.to_datetime(dates)

    # Group by time
    ts = (
        df
        .set_index("date")
        .resample(freq)
        .mean()
        .reset_index()
    )

    return ts
