from flask import Flask, request, render_template_string

app = Flask(__name__)

# Главная страница с формой для ввода страны
@app.route('/')
def index():
    return render_template_string('''
        <h1>Добро пожаловать в игру "Угадай мою страну"!</h1>
        <p>Привет! Меня зовут Олимов Амир. Сможешь угадать, из какой я страны?</p>
        <form action="/result" method="post">
            <label for="country">Введите название страны:</label>
            <input type="text" id="country" name="country" required>
            <button type="submit">Отправить</button>
        </form>
    ''')

# Страница с результатом
@app.route('/result', methods=['POST'])
def result():
    user_country = request.form['country'].strip().lower()
    correct_countries = {"tajikistan", "таджикистан"}  # Множество вариантов правильного ответа

    if user_country in correct_countries:
        return render_template_string('''
            <h1>Поздравляем!!! 🎉</h1>
            <p>Вы угадали! Я действительно из Таджикистана! 🇹🇯</p>
            <p>Спасибо, что сыграли со мной. Вы — настоящий знаток географии и просто молодец!</p>
            <p>Таджикистан — это страна с великолепными горами, гостеприимными людьми и богатой историей. Добро пожаловать к нам в гости!</p>
            <a href="/">Попробовать снова</a>
        ''')
    else:
        return render_template_string(f'''
            <h1>Увы, вы не угадали... 😢</h1>
            <p>Вы ввели: <b>{user_country.capitalize()}</b></p>
            <p>Но ничего страшного! Попробуйте ещё раз — я верю в вас!</p>
            <p>Подсказка: Это страна, где невероятные горы, древние города и очень гостеприимные люди. </p>
            <a href="/">Попробовать снова</a>
        ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
