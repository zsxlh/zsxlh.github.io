from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

choices = {}  # 用于存储用户选择的字典

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_name = request.form['user_name']
    selected_option = int(request.form['selected_option'])
    choices[user_name] = selected_option
    return jsonify({"message": "选择已提交。"}), 200

@app.route('/random_assign', methods=['POST'])
def random_assign():
    user_name = request.form['user_name']
    selected_option = random.randint(1, 5)
    choices[user_name] = selected_option
    return jsonify({"message": f"用户 {user_name} 被随机分配到选项 {selected_option}"}), 200

@app.route('/view_choices')
def view_choices():
    return render_template('view_choices.html', choices=choices)

if __name__ == '__main__':
    app.run(debug=True)
