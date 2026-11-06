import matplotlib.pyplot as plt

def plot_trend(india_ts, west_ts, component=1):
    pc = f"PC{component}"

    plt.figure(figsize=(10, 5))
    plt.plot(india_ts["date"], india_ts[pc], label="South Asia")
    plt.plot(west_ts["date"], west_ts[pc], label="West")

    plt.title(f"Fashion Trend Comparison – {pc}")
    plt.xlabel("Time")
    plt.ylabel("PCA Value")
    plt.legend()
    plt.grid(True)
    plt.show()
