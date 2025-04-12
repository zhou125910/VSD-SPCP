import pandas as pd
import os

def clean_soil_data(input_file, output_file):
    """
    清洗土壤数据，并自动创建保存路径
    
    参数:
    input_file: 输入的模拟数据文件路径
    output_file: 输出的清洗后数据文件路径
    """
    # 检查输出文件的目录是否存在，不存在则创建
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"自动创建目录: {output_dir}")
    
    # 加载原始数据
    data = pd.read_csv(input_file)
    
    # 检查缺失值
    print("缺失值检查：")
    print(data.isnull().sum())
    
    # 剔除异常值（例如氮含量低于0的记录）
    data_clean = data[(data["N"] > 0) & (data["P"] > 0) & (data["K"] > 0)]
    data_clean = data_clean[(data_clean["pH"] >= 4.5) & (data_clean["pH"] <= 8.5)]
    
    # 生成统计摘要
    summary = data_clean.describe()
    print("\n数据统计摘要：")
    print(summary)
    
    # 保存清洗后数据
    data_clean.to_csv(output_file, index=False)
    print(f"\n成功保存 {len(data_clean)} 个清洗后的数据样本到 {output_file}")

# 执行数据清洗
if __name__ == "__main__":
    clean_soil_data(
        input_file="data/simulated_soil_data.csv", 
        output_file="data/cleaned_soil_data.csv"
    )