import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = "new.csv"
a = pd.read_csv(path)

a2 = a["anglez"]
print(type(a2))

plt.plot(list(range(10000)),a2[:10000])
plt.show()