import matplotlib.pyplot as plt

def plot_momentum(ts, title, component=1):
    pc = f"PC{component}"

    plot_ts = (
        ts
        .set_index("date")
        .resample("M")      # 🔥 monthly
        .mean()
    )

    momentum = plot_ts[pc].diff()

    print(len(ts))

    plt.figure(figsize=(10, 4))
    plt.plot(momentum.index, momentum)
    plt.axhline(0, linestyle="--")
    plt.title(f"{title} – {pc}")
    plt.tight_layout()
    plt.show()
