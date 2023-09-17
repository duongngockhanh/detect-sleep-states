import pyarrow.parquet as pq
import pandas as pd

src_data = "data"

sample_submission_path = f"{src_data}/sample_submission.csv"
sample_submission_df = pd.read_csv(sample_submission_path)
# print(sample_submission_df)




b1 = f"{src_data}/test_series.parquet"
b2 = pq.read_table(b1)     # <class 'pyarrow.lib.Table'>
b3 = b2.to_pandas()          # <class 'pandas.core.frame.DataFrame'>
# b3.to_csv("b4.csv")
# [450 rows x 5 columns]



c1 = f"{src_data}/train_events.csv"
c2 = pd.read_csv(c1)
# print(c2.info())



d1 = f"{src_data}/train_series.parquet"
d2 = pq.read_table(d1)
d3 = d2.to_pandas()
d4 = d3[0:500]
d4.to_csv(f"{src_data}/d_0_500.csv")

# d5 = d3[26000:29000]
# d5.to_csv("d2629.csv")