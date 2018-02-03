import query_manager
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/szotar')
def get_dictionary():
    dictionary = query_manager.dictionary()

    return render_template('dictionary.html', dictionary=dictionary)


@app.route('/uj-szo', methods=['GET', 'POST'])
def add_new_dictionary_element():

    if request.method == "POST":
        query_manager.add_new_dictionary_element()
        return redirect('/szotar')
    else:
        return render_template('dictionary_form.html')


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
