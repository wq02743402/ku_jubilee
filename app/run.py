from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    email = request.form['email']
    # �b�o�̲K�[�d���޿�
    return render_template('result.html', email=email)

if __name__ == '__main__':
    app.run(debug=True)