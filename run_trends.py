import numpy as np
from analysis.pca_analysis import run_pca
from analysis.trend_model import build_time_series
from analysis.plot_trends import plot_trend
from analysis.visualizations import plot_momentum

# Load India data
india_data = np.load("features/indian_data.npz", allow_pickle=True)
india_embeddings = india_data["embeddings"]
india_dates = india_data["dates"]

# Load West data
west_data = np.load("features/global_data.npz", allow_pickle=True)
west_embeddings = west_data["embeddings"]
west_dates = west_data["dates"]

# PCA
india_pca, _ = run_pca(india_embeddings)
west_pca, _  = run_pca(west_embeddings)

# Time series
india_ts = build_time_series(india_pca, india_dates)
west_ts  = build_time_series(west_pca, west_dates)

print(india_ts.head())
print(west_ts.head())

plot_trend(india_ts, west_ts, component=1)
plot_trend(india_ts, west_ts, component=2)
plot_momentum(india_ts, "South Asian Trend Momentum")
plot_momentum(west_ts, "Western Trend Momentum")

def avg_volatility(ts, component=1):
    pc = f"PC{component}"
    return ts[pc].std()

print("India volatility:", avg_volatility(india_ts))
print("West volatility:", avg_volatility(west_ts))

# India volatility: 2.7096505
# West volatility: 2.9685814