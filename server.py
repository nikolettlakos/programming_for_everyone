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
        hungarian = request.form['hungarian']
        english = request.form['english']
        meaning = request.form['meaning']
        query_manager.add_new_dictionary_element(hungarian,english,meaning)
        return redirect('/szotar')
    else:
        return render_template('dictionary_form.html')


@app.route('/szotar/<id_dictionary>/torles', methods=['GET', 'POST'])
def delete_dictionary_element(id_dictionary):
    query_manager.delete_element_form_dictionary(id_dictionary)
    return redirect('/szotar')


@app.route('/szotar/<id_dictionary>/szerkesztes', methods=['GET', 'POST'])
def edit_dictionary_element(id_dictionary):
    if request.method == 'POST':
        hungarian_word = request.form['hungarian']
        english_word = request.form['english']
        meaning = request.form['meaning']
        query_manager.edit_element_form_dictionary(id_dictionary, hungarian_word, english_word, meaning)
        return redirect('/szotar')
    else:
        return render_template('dictionary_form.html')


@app.route('/uj-cikk', methods=['GET', 'POST'])
def add_new_topic():

    if request.method == "POST":
        title = request.form['title']
        body = request.form['body']
        topic = request.form['topic']
        query_manager.add_new_topic_element(title, body, topic)
        return redirect('/')
    else:
        return render_template('new_topic_form.html')


@app.route('/tananyag/<topic_type>', methods=['GET', 'POST'])
def get_topic(topic_type):
    datas = query_manager.get_rigth_topic(topic_type)
    return render_template('topic.html', datas=datas)


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
