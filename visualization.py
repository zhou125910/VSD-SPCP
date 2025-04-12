# 修正导入语句并加载数据
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import pandas as pd

# 加载清洗后的数据
df = pd.read_csv("data/cleaned_soil_data.csv")  # 确保路径正确

# 创建地理坐标系
geometry = [Point(xy) for xy in zip(df["longitude"], df["latitude"])]
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")

# 绘制热力图（保留以下内容）
fig, ax = plt.subplots(figsize=(10, 8))
gdf.plot(column="N", cmap="YlOrRd", legend=True, markersize=50, ax=ax)
plt.title("模拟土壤氮含量空间分布")
plt.savefig("outputs/nitrogen_distribution.png")
plt.show()