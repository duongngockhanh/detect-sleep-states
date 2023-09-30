import pandas as pd
import numpy as np
from itertools import groupby
import gc

train = pd.read_parquet("data/child-mind-institute-detect-sleep-states/test_series.parquet")

new = train[["series_id", "step"]]

new['event'] = 1
new.loc[300:449, 'event'] = 0

new.to_csv("sample_solution.csv", index=False)