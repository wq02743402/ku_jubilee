from flask import Flask, request, render_template
import pandas as pd
import os

app = Flask(__name__)

# 設定 CSV 文件的路徑
CSV_FILE = 'C:\\Users\\akira\\Desktop\\ku_jubilee\\file.csv'  # 確保這個路徑是正確的

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_email', methods=['POST'])
def check_email():
    email = request.form.get('email')

    # 檢查 CSV 文件是否存在
    if not os.path.exists(CSV_FILE):
        return f"CSV 文件不存在，請檢查。路徑：{CSV_FILE}"

    print(f"正在讀取文件：{CSV_FILE}")  # 確認路徑是否正確

    # 讀取 CSV 文件，指定編碼為 UTF-8
    try:
        data = pd.read_csv(CSV_FILE, encoding='utf-8')
    except UnicodeDecodeError:
        return "讀取 CSV 文件時發生編碼錯誤，請確認文件編碼為 UTF-8。"

    # 查詢會員電子信箱
    user_data = data[data['會員電子信箱'] == email]

    if user_data.empty:
        # 當電子信箱不正確時，返回錯誤頁面
        return render_template('result.html', error_message="電子信箱不正確，請再試一次。", show_error=True)

    # 獲取已完成的條目數量
    completed_count = user_data['完成數量'].values[0]

    return render_template('result.html', user_data=user_data, completed_count=completed_count, show_error=False)

if __name__ == '__main__':
    app.run(debug=True)
