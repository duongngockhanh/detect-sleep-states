import pandas as pd

path = "data/child-mind-institute-detect-sleep-states/train_series.parquet"
selected_event = [["7822ee8fe3ec", "onset", 299964], ["7df249527c63", "onset", 366204], ["844f54dcab89", "wakeup", 356352]]
save_path = "test_standard.csv"
solution_path = "solution.csv"

train_df = pd.read_parquet(path)


selected_df_list = []

for i in selected_event:
    idx = train_df.index[(train_df['series_id'] == i[0]) & (train_df['step'] == i[2])].to_list()[0]
    temp = train_df[idx-20:idx+130]
    selected_df_list.append(temp)

res = pd.concat(selected_df_list, ignore_index=True)
res.to_csv(save_path)


solution_df = pd.DataFrame(selected_event, columns=["series_id", "event", "step"])
solution_df.to_csv(solution_path, index=False)