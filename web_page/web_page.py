from flask import Flask, request, render_template

app = Flask(__name__)

# Главная страница с формой для ввода страны
@app.route('/')
def index():
    return render_template('index.html')  # Загружает файл index.html из папки templates

# Страница с результатом
@app.route('/result', methods=['POST'])
def result():
    user_country = request.form['country'].strip().lower()
    correct_countries = {"tajikistan", "таджикистан"}  # Множество вариантов правильного ответа

    if user_country in correct_countries:
        return render_template('success.html', country="Таджикистан")  # Загружает success.html
    else:
        return render_template('failure.html', user_country=user_country)  # Загружает failure.html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

