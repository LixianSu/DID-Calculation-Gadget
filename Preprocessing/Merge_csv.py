import os
import glob
import pandas as pd
import chardet

# 输入文件夹路径
folder_path = r"C:\Users\LIXIANSU\Desktop\1"

# 获取文件夹下所有csv文件
all_csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

# 合并所有csv文件
dfs = []
for file in all_csv_files:
    with open(file, 'rb') as f:
        result = chardet.detect(f.read())
        encoding = result['encoding']
        df = pd.read_csv(file, encoding=encoding, low_memory=False)
        dfs.append(df)
        print("reading file {}".format(file))
combined_csv = pd.concat(dfs, ignore_index=True)

# 输出合并后的csv文件
combined_csv.to_csv(os.path.join(folder_path, "combined_csv.csv"), index=False)