import query_manager
from flask import Flask, render_template, request, redirect, url_for
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
        abbreviation_of_the_word = request.form['abbreviation']
        query_manager.add_new_dictionary_element(hungarian, english, abbreviation_of_the_word, meaning)
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
        abbreviation_of_the_word = request.form['abbreviation']
        meaning = request.form['meaning']
        query_manager.edit_element_form_dictionary(id_dictionary, hungarian_word, abbreviation_of_the_word, english_word, meaning)
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


@app.route('/tananyag/<topic_type>/<topic_id>', methods=['GET', 'POST'])
def get_lesson(topic_type, topic_id):
    datas = query_manager.get_rigth_lesson(topic_type, topic_id)
    return render_template('lesson.html', datas=datas)


@app.route('/tananyag/<topic_type>/<topic_id>/tananyag-szerkesztese', methods=['GET', 'POST'])
def edit_lesson(topic_type, topic_id):
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        query_manager.edit_topic_element(topic_type, topic_id, title, body)
        return redirect('/')
    else:
        return render_template('new_topic_form.html')

@app.route('/tananyag/<topic_type>/<topic_id>/tananyag-torlese', methods=['GET', 'POST'])
def delete_topic(topic_type, topic_id):
    query_manager.delete_element_form_topic(topic_type, topic_id)
    return redirect('/tananyag/'+topic_type)


@app.route('/tananyag/<topic_type>/<topic_id>/kedvencnek-jeloles', methods=['GET', 'POST'])
def add_topic_to_fav(topic_type, topic_id):
    datas = query_manager.get_rigth_lesson(topic_type, topic_id)
    for data in datas:
        if data['fav'] == 0:
            query_manager.add_topic_to_favourites(topic_type, topic_id, 1)
            return redirect('/kedvencek')
        else:
            query_manager.add_topic_to_favourites(topic_type, topic_id, 0)
            return redirect('/kedvencek')


@app.route('/kedvencek', methods=['GET', 'POST'])
def fav_page():
    favs_topic = query_manager.get_favs()
    favs_question = query_manager.get_favs_from_rehearsal_question()
    return render_template('fav.html', favs=favs_topic, favs_question=favs_question)


@app.route('/tananyag/<topic_type>/<topic_id>/megtanult', methods=['GET', 'POST'])
def add_topic_to_learnt(topic_type, topic_id):
    datas = query_manager.get_rigth_lesson(topic_type, topic_id)
    for data in datas:
        if data['learnt'] == 0:
            query_manager.learnt_update(topic_type, topic_id, 1)
            return redirect('/')
        else:
            query_manager.learnt_update(topic_type, topic_id, 0)
            return redirect('/')


@app.route('/talalat', methods=['GET', 'POST'])
def searching():
    search_phrase = request.args['search']
    search_data = query_manager.searching(search_phrase)
    return render_template('search_found.html', search_data=search_data)


@app.route('/ismetles', methods=['GET', 'POST'])
def get_rehearsal_questions():
    rehearsal_question = query_manager.get_rehearsal_questions()
    return render_template('rehearsal_question.html', rehearsal_question=rehearsal_question)


@app.route('/ismetles/<question_id>', methods=['GET', 'POST'])
def get_rehearsal_question_by_id(question_id):
    datas = query_manager.get_rigth_rehearsal_question(question_id)
    return render_template('answer_for_question.html', datas=datas)


@app.route('/ismetles/<question_id>/kedvencnek-jeloles', methods=['GET', 'POST'])
def add_question_to_fav(question_id):
    datas = query_manager.get_rigth_rehearsal_question(question_id)
    for data in datas:
        if data['fav'] == 0:
            query_manager.add_question_to_favourites(question_id, 1)
            return redirect('/kedvencek')
        else:
            query_manager.add_question_to_favourites(question_id, 0)
            return redirect('/kedvencek')


@app.route('/uj-ismetlo-kerdes', methods=['GET', 'POST'])
def new_rehearsal_question():
    if request.method == "POST":
        title = request.form['title']
        answer = request.form['answer']
        query_manager.add_new_rehearsal_question_element(title, answer)
        return redirect('/ismetles')
    else:
        return render_template('rehearsal_question_form.html')


@app.route('/ismetles/<rehearsal_question_id>/torles', methods=['GET', 'POST'])
def delete_rehearsal_question_item(rehearsal_question_id):
    query_manager.delete_element_form_rehearsal_question(rehearsal_question_id)
    return redirect('/ismetles')


'''
@app.route('/regisztracio', methods=['GET', 'POST'])
def registration():
    if request.method == "GET":
        return render_template('registration.html', page_details=page_details)
    else:
        new_user = {
                    'username': request.form['username'],
                    'password': request.form['password'],
                    'dt': datetime.now()
                    }
        reg_successful = data_manager.user_registration(new_user)
        if reg_successful:
            session['username'] = new_user['username']
            user_id = data_manager.get_user_id_by_username(new_user)['id']
            session['user_id'] = user_id
            return redirect('/list')
        else:
            return redirect('/registration')
'''


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
