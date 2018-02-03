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
def add_new_dictionary_element(cursor, hungarian, english, meaning):

    cursor.execute('''INSERT INTO  dictionary(hungarian_word, english_word, meaning) 
                      VALUES (%(hungarian)s, %(english)s, %(meaning)s);''',
                   {'hungarian': hungarian,
                    'english': english,
                    'meaning': meaning})


@database_common.connection_handler
def delete_element_form_dictionary(cursor, dictionary_id):
    cursor.execute(''' DELETE FROM dictionary
                      WHERE dictionary_id = %(id)s;''',
                   {'id': dictionary_id})


@database_common.connection_handler
def edit_element_form_dictionary(cursor, dictionary_id, hungarian_word, english_word, meaning):

    cursor.execute(''' UPDATE dictionary
                      SET hungarian_word = %(hungarian_word)s, english_word = %(english_word)s, meaning = %(meaning)s
                      WHERE dictionary_id = %(id)s;''',
                   {'hungarian_word': hungarian_word,
                    'english_word': english_word,
                    'meaning': meaning,
                    'id': dictionary_id})


@database_common.connection_handler
def add_new_topic_element(cursor, title, body, topic_type):

    cursor.execute('''INSERT INTO  topic(title, body, topic_type) 
                      VALUES (%(title)s, %(body)s, %(topic_type)s);''',
                   {'title': title,
                    'body': body,
                    'topic_type': topic_type})

