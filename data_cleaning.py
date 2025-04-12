import pandas as pd  

# 加载数据  
raw_data = pd.read_csv("data/synthetic_soil_data.csv")  

# 清洗：删除负值  
clean_data = raw_data[(raw_data["N"] > 0) & (raw_data["P"] > 0) & (raw_data["K"] > 0)]  

# 保存清洗后数据  
clean_data.to_csv("data/cleaned_soil_data.csv", index=False)  
print("数据清洗完成！")  