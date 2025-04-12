import os
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
from shapely.geometry import Point
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def visualize_and_analyze():
    # 加载清洗后的数据
    data = pd.read_csv("data/cleaned_soil_data.csv")
    
    # 创建输出目录
    os.makedirs("outputs", exist_ok=True)
    
    # 绘制所有指标的热力图
    def plot_all_choropleth_maps():
        indicators = ["N", "P", "K", "pH", "organic_matter"]
        cmaps = ["YlOrRd", "YlGn", "Blues", "PuOr", "Greens"]
        
        for indicator, cmap in zip(indicators, cmaps):
            gdf = gpd.GeoDataFrame(data, geometry=[Point(xy) for xy in zip(data["longitude"], data["latitude"])], crs="EPSG:4326")
            fig, ax = plt.subplots(figsize=(12, 8))
            gdf.plot(column=indicator, cmap=cmap, legend=True, markersize=50, ax=ax)
            plt.title(f"Soil {indicator} Content Spatial Distribution")
            plt.savefig(os.path.join("outputs", f"{indicator}_heatmap.png"))
            plt.close()
            print(f"{indicator} 热力图生成完成，保存到 outputs/{indicator}_heatmap.png")
    
    # 绘制所有指标的箱线图
    def plot_all_boxplots():
        indicators = ["N", "P", "K", "pH", "organic_matter"]
        
        for indicator in indicators:
            plt.figure(figsize=(12, 6))
            sns.boxplot(x="land_use", y=indicator, data=data)
            plt.title(f"{indicator} Content by Land Use Type")
            plt.xticks(rotation=45)
            plt.savefig(os.path.join("outputs", f"{indicator}_by_landuse.png"))
            plt.close()
            print(f"{indicator} 箱线图生成完成，保存到 outputs/{indicator}_by_landuse.png")
    
    # 绘制相关性热图
    def plot_correlation_heatmap():
        corr_matrix = data[["N", "P", "K", "pH", "organic_matter"]].corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
        plt.title("Soil Nutrients Correlation Heatmap")
        plt.savefig(os.path.join("outputs", "correlation_heatmap.png"))
        plt.close()
        print("相关性热图生成完成，保存到 outputs/correlation_heatmap.png")
    
    # 执行聚类分析
    def perform_clustering():
        X = data[["longitude", "latitude", "N", "P", "K", "pH", "organic_matter"]]
        kmeans = KMeans(n_clusters=4, random_state=42)
        data["cluster"] = kmeans.fit_predict(X)
        
        plt.figure(figsize=(12, 8))
        scatter = plt.scatter(data["longitude"], data["latitude"], c=data["cluster"], cmap="viridis", s=50)
        plt.colorbar(scatter)
        plt.title("Soil Nutrients Clustering")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.savefig(os.path.join("outputs", "soil_clustering.png"))
        plt.close()
        
        silhouette_avg = silhouette_score(X, data["cluster"])
        print(f"聚类轮廓系数: {silhouette_avg:.3f}")
        print("聚类分析完成，结果保存到 outputs/soil_clustering.png")
    
    # 执行所有可视化和分析
    plot_all_choropleth_maps()
    plot_all_boxplots()
    plot_correlation_heatmap()
    perform_clustering()

if __name__ == "__main__":
    visualize_and_analyze()