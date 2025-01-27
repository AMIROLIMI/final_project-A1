from flask import Flask, request, render_template

app = Flask(__name__)

# Главная страница с формой для ввода страны
@app.route('/')
def index():
    return render_template('index.html')

# Страница с результатом
@app.route('/result', methods=['POST'])
def result():
    user_country = request.form['country'].strip().lower()
    correct_countries = {"tajikistan", "таджикистан"}  # Множество вариантов правильного ответа

    if user_country in correct_countries:
        return render_template('result.html', success=True, country=user_country)
    else:
        return render_template('result.html', success=False, country=user_country)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

