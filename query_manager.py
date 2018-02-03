import database_common


@database_common.connection_handler
def dictionary(cursor):
    cursor.execute("""
                    SELECT * FROM dictionary
                    ORDER BY english_word;
                   """,)
    data = cursor.fetchall()
    return data