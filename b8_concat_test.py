import pandas as pd
import numpy as np

a = pd.DataFrame(([1, 2],
                  [1, 2],
                  [1, 2]),
                  columns=["a", "b"])

b = pd.DataFrame(([1, 2],
                  [1, 2],
                  [1, 2]),
                  columns=["a", "b"])

c = pd.DataFrame(([1, 2],
                  [1, 2],
                  [1, 2]),
                  columns=["a", "b"])

d = [a, b, c]

result = pd.concat(d, ignore_index=True)

print(result)