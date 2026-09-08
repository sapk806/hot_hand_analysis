def fgp_histogram(simulated_fg_after_3, real_fg_after_3):
    import matplotlib.pyplot as plt
    import numpy as np

    fgps = np.append(simulated_fg_after_3, real_fg_after_3)
    plt.hist(fgps, bins=50)
    plt.title("Distribtion of FG% After Three Consecutive Makes")
    plt.xlabel("FG%")
    plt.ylabel("Frequency")
    plt.axvline(x=fgps[-1], color="red", linestyle="--", linewidth=2, label="Observed FG%")
    plt.legend(loc="upper right")
    plt.show()

def consecutive_makes_bar(simulated_consecutive_makes, real_consecutive_makes):
    import matplotlib.pyplot as plt
    import numpy as np

    consecutive_makes = np.concat([simulated_consecutive_makes, real_consecutive_makes])
    values, counts = np.unique(consecutive_makes, return_counts=True)

    plt.bar(values, counts)
    plt.xticks(ticks = np.arange(start=0, stop=18, step=1))
    plt.title("Distribtion of Max Consecutive Makes")
    plt.xlabel("Consecutive Makes")
    plt.ylabel("Frequency")
    plt.axvline(x=consecutive_makes[-1], color="red", linestyle="--", linewidth=2, label="Observed Max Streak")
    plt.legend(loc="upper right")
    plt.show()