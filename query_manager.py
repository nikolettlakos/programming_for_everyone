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
def add_new_dictionary_element(cursor, hungarian, english, abbreviation, meaning):

    cursor.execute('''INSERT INTO  dictionary(hungarian_word, english_word, abbreviation, meaning) 
                      VALUES (%(hungarian)s, %(english)s, %(abbreviation)s, %(meaning)s);''',
                   {'hungarian': hungarian,
                    'english': english,
                    'abbreviation': abbreviation,
                    'meaning': meaning})


@database_common.connection_handler
def delete_element_form_dictionary(cursor, dictionary_id):
    cursor.execute(''' DELETE FROM dictionary
                      WHERE dictionary_id = %(id)s;''',
                   {'id': dictionary_id})


@database_common.connection_handler
def delete_element_form_topic(cursor, topic_type, topic_id):
    cursor.execute(''' DELETE FROM topic
                      WHERE topic_type = %(topic_type)s AND topic_id = %(topic_id)s''',
                   {'topic_id': topic_id,
                    'topic_type': topic_type})


@database_common.connection_handler
def edit_element_form_dictionary(cursor, dictionary_id, hungarian_word, english_word, abbreviation, meaning):

    cursor.execute(''' UPDATE dictionary
                      SET hungarian_word = %(hungarian_word)s, english_word = %(english_word)s, abbreviation = %(abbreviation)s, meaning = %(meaning)s
                      WHERE dictionary_id = %(id)s;''',
                   {'hungarian_word': hungarian_word,
                    'english_word': english_word,
                    'meaning': meaning,
                    'abbreviation': abbreviation,
                    'id': dictionary_id})


@database_common.connection_handler
def add_new_topic_element(cursor, title, body, topic_type):

    cursor.execute('''INSERT INTO  topic(title, body, topic_type) 
                      VALUES (%(title)s, %(body)s, %(topic_type)s);''',
                   {'title': title,
                    'body': body,
                    'topic_type': topic_type})


@database_common.connection_handler
def get_rigth_topic(cursor, topic_type):
    cursor.execute("""
                    SELECT * FROM topic
                    WHERE topic_type = %(topic_type)s; """,
                   {'topic_type': topic_type})
    data = cursor.fetchall()
    return data


@database_common.connection_handler
def get_rigth_lesson(cursor, topic_type, topic_id):
    cursor.execute("""
                    SELECT * FROM topic
                    WHERE topic_type = %(topic_type)s AND topic_id = %(topic_id)s; """,
                   {'topic_type': topic_type,
                    'topic_id': topic_id})
    data = cursor.fetchall()
    return data


@database_common.connection_handler
def add_topic_to_favourites(cursor, topic_type, topic_id, fav_or_not):
    cursor.execute(''' UPDATE topic
                      SET fav = %(fav)s
                      WHERE topic_type = %(topic_type)s AND topic_id = %(topic_id)s;''',
                   {'topic_type': topic_type,
                    'topic_id': topic_id,
                    'fav': fav_or_not})

@database_common.connection_handler
def get_favs(cursor):
    cursor.execute(''' SELECT * FROM topic
                    WHERE fav = 1
                    ORDER BY topic_type ASC;''',)
    data = cursor.fetchall()
    return data


@database_common.connection_handler
def learnt_update(cursor, topic_type, topic_id, learnt):
    cursor.execute(''' UPDATE topic
                      SET learnt = %(learnt)s
                      WHERE topic_type = %(topic_type)s AND topic_id = %(topic_id)s;''',
                   {'topic_type': topic_type,
                    'topic_id': topic_id,
                    'learnt': learnt})


@database_common.connection_handler
def searching(cursor, searching_phrase):
    cursor.execute(''' SELECT topic.title, topic.body, dictionary.meaning FROM topic, dictionary
                      WHERE topic.title LIKE %(searching_phrase)s OR topic.body LIKE %(searching_phrase)s OR dictionary.meaning LIKE %(searching_phrase)s;''',
                   {'searching_phrase': '%' + searching_phrase + '%'})
    return cursor.fetchall()


@database_common.connection_handler
def get_rehearsal_questions(cursor):
    cursor.execute(''' SELECT * FROM rehearsal_question
                      ORDER BY question_title;''',)
    return cursor.fetchall()


@database_common.connection_handler
def get_rigth_rehearsal_question(cursor, question_id):
    cursor.execute("""
                    SELECT * FROM rehearsal_question
                    WHERE rehearsal_question_id = %(question_id)s; """,
                   {'question_id': question_id})
    data = cursor.fetchall()
    return data
