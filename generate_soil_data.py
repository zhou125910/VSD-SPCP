from faker import Faker  
import pandas as pd  
import numpy as np  

# 初始化生成器  
fake = Faker()  

# 生成100条模拟数据  
data = {  
    "longitude": [fake.longitude() for _ in range(100)],  
    "latitude": [fake.latitude() for _ in range(100)],  
    "N": np.random.normal(100, 20, 100).round(1),  # 正态分布模拟氮含量  
    "P": np.random.uniform(10, 50, 100).round(1),  # 均匀分布模拟磷含量  
    "K": np.random.uniform(100, 300, 100).round(1),  
    "land_use": np.random.choice(["farmland", "forest", "urban"], 100)  
}  

# 保存为CSV  
df = pd.DataFrame(data)  
df.to_csv("data/synthetic_soil_data.csv", index=False)  
print("模拟数据已生成！")  