import pandas as pd
import numpy as np
from faker import Faker

def generate_soil_data(num_samples=1000, seed=42):
    """
    生成模拟土壤数据
    
    参数:
    num_samples: 生成的样本数量
    seed: 随机种子，保证结果可复现
    """
    np.random.seed(seed)
    fake = Faker()
    Faker.seed(seed)
    
    data = []
    land_use_types = ["农田", "林地", "草地", "城市用地"]
    
    for _ in range(num_samples):
        # 生成地理坐标
        lat = fake.latitude()
        lon = fake.longitude()
        
        # 随机选择土地利用类型
        land_use = np.random.choice(land_use_types)
        
        # 根据土地利用类型生成合理的土壤养分数据
        if land_use == "农田":
            N = np.random.normal(120, 20)  # 氮含量均值120，标准差20
            P = np.random.normal(60, 15)
            K = np.random.normal(80, 20)
            pH = np.random.normal(6.5, 0.5)
            organic_matter = np.random.normal(2.5, 0.8)
        elif land_use == "林地":
            N = np.random.normal(100, 15)
            P = np.random.normal(40, 10)
            K = np.random.normal(70, 15)
            pH = np.random.normal(5.8, 0.4)
            organic_matter = np.random.normal(3.0, 1.0)
        elif land_use == "草地":
            N = np.random.normal(90, 18)
            P = np.random.normal(35, 8)
            K = np.random.normal(65, 12)
            pH = np.random.normal(6.0, 0.3)
            organic_matter = np.random.normal(2.0, 0.7)
        else:  # 城市用地
            N = np.random.normal(80, 25)
            P = np.random.normal(30, 12)
            K = np.random.normal(50, 18)
            pH = np.random.normal(7.0, 0.6)
            organic_matter = np.random.normal(1.5, 0.5)
        
        # 添加随机噪声
        noise_factor = np.random.uniform(0.8, 1.2)
        N *= noise_factor
        P *= noise_factor
        K *= noise_factor
        pH = max(4.5, min(8.5, pH * noise_factor))  # 限制pH值范围
        
        data.append([lon, lat, N, P, K, pH, organic_matter, land_use])
    
    # 转换为DataFrame
    columns = ["longitude", "latitude", "N", "P", "K", "pH", "organic_matter", "land_use"]
    df = pd.DataFrame(data, columns=columns)
    
    return df

# 生成1000个样本并保存为CSV文件
if __name__ == "__main__":
    soil_data = generate_soil_data(num_samples=1000)
    soil_data.to_csv("data/simulated_soil_data.csv", index=False)
    print(f"成功生成 {len(soil_data)} 个模拟土壤数据样本")