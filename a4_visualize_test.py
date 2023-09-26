import pandas as pd
import matplotlib.pyplot as plt


src_data = "data"

# Declare variables
a1 = f"{src_data}/b4.csv"
a2 = pd.read_csv(a1)
a3 = a2[["step", "anglez", "enmo"]]
x, ay1, ay2 = range(len(a3["step"])), a3["anglez"], a3["enmo"]


# Visualize
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 6))

ax[0,0].plot(x, ay1, label="anglez")
ax[0,0].scatter(x[150], 0, color="red")
ax[0,0].scatter(x[300], 0, color="red")
ax[0,0].legend()
ax[0,0].set(title="onset - anglez",
            xlabel="step",
            ylabel="anglez")


ax[0,1].plot(x, ay2, label="enmo")
ax[0,1].scatter(x[150], 0, color="red")
ax[0,1].scatter(x[300], 0, color="red")
ax[0,1].legend()
ax[0,1].set(title="onset - enmo",
            xlabel="step",
            ylabel="enmo")


fig.savefig("visualize_test.png")