from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__, template_folder='/Users/vasshil/PycharmProjects/Labs_5_sem/laba2/templates/')
app = Flask(__name__)

file_name = 'list.txt'


# Функция для записи слов в файл
def add_to_file(word1, word2):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(f"{word1}-{word2}\n")


# Функция для чтения слов из файла
def read_from_file():
    words1 = []
    words2 = []
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                if not line.__contains__("-"):
                    continue
                word1, word2 = line.strip().split("-")
                words1.append(word1)
                words2.append(word2)
    except FileNotFoundError:
        pass
    return words1, words2


# Домашняя страница
@app.route("/")
@app.route("/home")
def home():
    return "<h1>Добро пожаловать в словарь</h1>"


# Страница со списком слов
@app.route("/words_list")
def words_list():
    words1, words2 = read_from_file()
    return render_template('words_list.html', words1=words1, words2=words2)


# Страница для добавления слов
@app.route("/add_word", methods=["GET", "POST"])
def add_word():
    if request.method == "POST":
        word1 = request.form["word1"]
        word2 = request.form["word2"]
        add_to_file(word1, word2)
        return redirect(url_for("home"))
    return render_template('add_word.html')


if __name__ == "__main__":
    app.run(debug=True)

