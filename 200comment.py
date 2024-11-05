import pandas as pd
from venv import create
from sqlalchemy import create_engine

# Đọc file Excel
xlsx_path = 'H:/My Drive/Learn Python/comment 7 col.xlsx'  # Dùng / để tránh lỗi escape character
df = pd.read_excel(xlsx_path)
df = df.drop_duplicates()

# Lọc dữ liệu theo từ khóa
key = "vinh|tiên|vc|vợ chồng|vk ck|từ thiện|cứu trợ|đồng bào|tỷ|vc|quyên góp|miền trung|đồng bào|cv|tỷ|kiện|Hằng|lux"
data = df[df['Column1'].str.lower().str.contains(key.lower(), case=False, na=False)]

# Tạo DataFrame từ dữ liệu lọc được
df = pd.DataFrame(data)

# Kết nối đến MySQL
username = 'root'
password = 'halong123'
db = 'long_db'

url = f"mysql+pymysql://{username}:{password}@localhost/{db}"
engine = create_engine(url)

# Đẩy dữ liệu lên MySQL
df.to_sql('comment', con=engine, if_exists='replace', index=False)
print(df)