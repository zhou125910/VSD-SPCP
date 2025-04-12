# 在文件开头添加以下导入语句和数据加载代码
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 加载清洗后的数据
df = pd.read_csv("data/cleaned_soil_data.csv")  # 确保路径正确

# 原代码（保留以下内容）
plt.figure(figsize=(10, 6))
sns.boxplot(x="land_use", y="K", data=df)
plt.title("不同土地利用类型的钾含量对比")
plt.xticks(rotation=45)
plt.savefig("outputs/k_landuse.png")
plt.show() 