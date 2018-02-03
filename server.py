import query_manager
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/szotar')
def get_dictionary():
    dictionary = query_manager.dictionary()

    return render_template('dictionary.html', dictionary=dictionary)


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
