# main.py
import subprocess

scripts = [
    "python generate_soil_data.py",    # 生成数据
    "python data_cleaning.py",          # 清洗数据
    "python analysis.py",               # 统计分析
    "python visualization.py",          # 空间可视化
    "python landuse_analysis.py"        # 土地利用分析
]

for cmd in scripts:
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"✅ {cmd} 执行成功")
    except subprocess.CalledProcessError as e:
        print(f"❌ {cmd} 执行失败: {str(e)}")
        exit(1)

print("所有步骤执行完毕！")