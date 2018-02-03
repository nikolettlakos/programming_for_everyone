from datetime import datetime

from flask import request

import database_common


@database_common.connection_handler
def dictionary(cursor):
    cursor.execute("""
                    SELECT * FROM dictionary
                    ORDER BY english_word;
                   """,)
    data = cursor.fetchall()
    return data


@database_common.connection_handler
def add_new_dictionary_element(cursor):
    hungarian = request.form['hungarian']
    english = request.form['english']
    meaning = request.form['meaning']
    cursor.execute('''INSERT INTO  dictionary(hungarian_word, english_word, meaning) 
                      VALUES (%(hungarian)s, %(english)s, %(meaning)s);''',
                   {'hungarian': hungarian,
                    'english': english,
                    'meaning': meaning})
