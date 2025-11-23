import pandas as pd
import numpy as np

def clean_dataset():
    # 1. 读取原始数据
    # 请确保文件名与你下载的一致
    input_file = 'Global_Mobile_Prices_2025_Extended.csv'
    output_file = 'Global_Mobile_Prices_2025_Fixed.csv'
    
    try:
        df = pd.read_csv(input_file)
        print(f"成功读取文件，共 {len(df)} 行数据。")
    except FileNotFoundError:
        print("❌ 找不到原始 CSV 文件，请检查文件名！")
        return

    # 2. 定义修复 Apple 价格的逻辑
    def fix_apple_price(row):
        if row['brand'] != 'Apple':
            return row['price_usd']
        
        model = str(row['model'])
        storage = row['storage_gb']
        
        # 基础价格设定 (参考现实市场)
        if 'Pro Max' in model:
            base_price = 1199
        elif 'Pro' in model: # 包含 Pro 但不含 Max
            base_price = 999
        elif 'Plus' in model:
            base_price = 899
        else:
            # 标准版 (如 iPhone 14, 16)
            base_price = 799
            
        # 存储溢价 (粗略估算)
        if storage == 256:
            base_price += 100
        elif storage == 512:
            base_price += 300
        elif storage >= 1000: # 1TB
            base_price += 500
            
        # 添加一点点随机波动 (-20 到 +20 美元)，让数据看起来不那么死板
        variation = np.random.randint(-20, 21)
        return base_price + variation

    # 3. 定义修复 Apple 处理器的逻辑 (Bonus)
    def fix_apple_processor(row):
        if row['brand'] != 'Apple':
            return row['processor']
        
        model = str(row['model'])
        if '16' in model:
            return 'A18 Pro' if 'Pro' in model else 'A18'
        elif '15' in model:
            return 'A17 Pro' if 'Pro' in model else 'A16 Bionic'
        elif '14' in model:
            return 'A16 Bionic' if 'Pro' in model else 'A15 Bionic'
        return 'Apple A-Series' # 兜底

    # 4. 应用修复
    print("正在修复 Apple 手机的价格和处理器信息...")
    df['price_usd'] = df.apply(fix_apple_price, axis=1)
    df['processor'] = df.apply(fix_apple_processor, axis=1)

    # 5. 保存新文件
    df.to_csv(output_file, index=False)
    print(f"✅ 修复完成！新文件已保存为: {output_file}")
    print("\nApple 数据预览 (Top 5):")
    print(df[df['brand']=='Apple'][['model', 'price_usd', 'processor', 'storage_gb']].head())

if __name__ == "__main__":
    clean_dataset()