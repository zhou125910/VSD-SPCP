import pandas as pd
import os  # 新增导入

# 加载清洗后数据
df = pd.read_csv("data/cleaned_soil_data.csv")

# 统计摘要
summary = df.describe()
print("数据统计摘要：\n", summary)

# 创建 outputs 目录（如果不存在）
os.makedirs("outputs", exist_ok=True)  # 新增代码

# 保存统计结果
summary.to_csv("outputs/data_summary.csv")