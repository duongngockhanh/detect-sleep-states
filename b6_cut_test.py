import pandas as pd

path = "data/child-mind-institute-detect-sleep-states/train_series.parquet"
a = pd.read_parquet(path)

b = [246324, 270132, 297576, 322596, 349596]

c = []

for i in b:
    temp = a[i-1000:i+1000]
    c.append(temp)

save_path = "new_test.csv"
res = pd.concat(c, ignore_index=True)
res.to_csv(save_path)