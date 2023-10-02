import pandas as pd
import matplotlib.pyplot as plt
import glob

src_data = glob.glob("a5_scoring/*/test_standard.csv")

for a1 in src_data:
    # Declare variables
    a2 = pd.read_csv(a1)
    n_sample = a2.shape[0]
    n_durable = n_sample // 150
    a3 = a2[["step", "anglez", "enmo"]]
    x, ay1, ay2 = range(len(a3["step"])), a3["anglez"], a3["enmo"]


    # Visualize
    fig, ax = plt.subplots(ncols=2, nrows=1, figsize=(12, 4))

    ax[0].plot(x, ay1)
    for i in range(1, n_durable):
        ax[0].plot([i*150,i*150],[-90,90], linestyle="--", color="red")
        ax[0].plot([i*150-130,i*150-130],[-90,90], linestyle="--", color="green")
    ax[0].plot([n_durable*150-130,n_durable*150-130],[-90,90], linestyle="--", color="green")
    # ax[0].legend()
    ax[0].set(title="onset - anglez",
                xlabel="step",
                ylabel="anglez")


    ax[1].plot(x, ay2)
    for i in range(1, n_durable):
        ax[1].plot([i*150,i*150],[-0.1,1.1], linestyle="--", color="red")
        ax[1].plot([i*150-130,i*150-130],[-0.1,1.1], linestyle="--", color="green")
    ax[1].plot([n_durable*150-130,n_durable*150-130],[-0.1,1.1], linestyle="--", color="green")
    # ax[1].legend()
    ax[1].set(title="onset - enmo",
                xlabel="step",
                ylabel="enmo")


    fig.savefig(a1[:-4] + "_event.png")