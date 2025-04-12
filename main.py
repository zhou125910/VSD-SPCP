import os
import sys
import pandas as pd

def main():
    # 确保所有必要的模块都已安装
    try:
        import numpy as np
        import matplotlib.pyplot as plt
        import geopandas as gpd
        from faker import Faker
        import seaborn as sns
        from sklearn.cluster import KMeans
        from sklearn.metrics import silhouette_score
    except ImportError as e:
        print(f"缺少必要的库: {e}")
        print("请确保安装了所有必要的库。")
        sys.exit(1)
    
    # 1. 数据生成
    os.system("python data_generator.py")
    
    # 2. 数据清洗
    os.system("python data_processing.py")
    
    # 3. 数据加载与预处理
    os.system("python up-datr.py")
    
    # 4. 可视化与分析
    os.system("python Choropleth_Map.py")
    
    print("所有步骤执行完成！")

if __name__ == "__main__":
    main()