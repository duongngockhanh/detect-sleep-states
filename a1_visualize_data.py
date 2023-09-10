import pandas as pd
import matplotlib.pyplot as plt


# Declare variables
a1 = "d0406.csv"
a2 = pd.read_csv(a1)
a3 = a2[["step", "anglez", "enmo"]]
x, ay1, ay2 = a3["step"], a3["anglez"], a3["enmo"]


b1 = "d1012.csv"
b2 = pd.read_csv(b1)
b3 = b2[["step", "anglez", "enmo"]]
bx, by1, by2 = b3["step"], b3["anglez"], b3["enmo"]


# Visualize
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

ax[0,0].plot(x, ay1, label="anglez")
ax[0,0].scatter(x[992], ay1[992], color="red")
ax[0,0].legend()
ax[0,0].set(title="onset - anglez",
            xlabel="step",
            ylabel="anglez")

ax[1,0].scatter(x[992], ay2[992], color="red")
ax[1,0].plot(x, ay2, label="enmo")
ax[1,0].legend()
ax[1,0].set(title="onset - enmo",
            xlabel="step",
            ylabel="enmo")

ax[0,1].plot(bx, by1, label="anglez")
ax[0,1].scatter(bx[932], by1[932], color="red")
ax[0,1].legend()
ax[0,1].set(title="wakeup - anglez",
            xlabel="step",
            ylabel="anglez")

ax[1,1].plot(bx, by2, label="enmo")
ax[1,1].scatter(bx[932], by2[932], color="red")
ax[1,1].legend()
ax[1,1].set(title="wakeup - enmo",
            xlabel="step",
            ylabel="enmo")


fig.savefig("visualize_1.png")