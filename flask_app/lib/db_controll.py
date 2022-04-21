import psycopg2



def db_insert(data):
    conn = psycopg2.connect(
        host="arjuna.db.elephantsql.com",
        database="bkxwjxhh",
        user="bkxwjxhh",
        password="O5_S6rDOodpP1oB0_k6vN6K0kU5qB1R9")
    cur = conn.cursor()
    for i in data:
        try:
            game = i["Game"].replace("'","''")
            cur.execute(f"""INSERT INTO twitch_data VALUES ({int(i['Rank'])},
                                                            \'{game}\',
                                                            {int(i['Month'])},
                                                            {int(i['Year'])},
                                                            {int(i['Hours_watched'])},
                                                            {int(i['Hours_Streamed'].split(' ')[0])},
                                                            {int(i['Peak_viewers'])},
                                                            {int(i['Peak_channels'])},
                                                            {int(i['Streamers'])},
                                                            {int(i['Avg_viewers'])},
                                                            {int(i['Avg_channels'])},
                                                            {float(i['Avg_viewer_ratio'])});""")
        except:
            print(f'{i["Game"]}, {int(i["Year"])}, {int(i["Month"])} // db입력 못했습니다.')
            continue
    conn.commit()
    cur.close()
    conn.close()


def db_select():
    conn = psycopg2.connect(
        host="arjuna.db.elephantsql.com",
        database="bkxwjxhh",
        user="bkxwjxhh",
        password="O5_S6rDOodpP1oB0_k6vN6K0kU5qB1R9")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM twitch_data""")
    data = cur.fetchall()
    result = []
    for i in data:
        i = list(i)
        result.append([x for x in i])
    cur.close()
    conn.close()
    return result

def game_list():
    conn = psycopg2.connect(
        host="arjuna.db.elephantsql.com",
        database="bkxwjxhh",
        user="bkxwjxhh",
        password="O5_S6rDOodpP1oB0_k6vN6K0kU5qB1R9")
    cur = conn.cursor()
    cur.execute("""SELECT DISTINCT game FROM twitch_data""")
    data = cur.fetchall()
    result = [i[0] for i in data]
    cur.close()
    conn.close()
    return result

def game_data(game):
    conn = psycopg2.connect(
        host="arjuna.db.elephantsql.com",
        database="bkxwjxhh",
        user="bkxwjxhh",
        password="O5_S6rDOodpP1oB0_k6vN6K0kU5qB1R9")
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM twitch_data WHERE game={game}""")
    data = cur.fetchall()
    result = []
    for i in data:
        i = list(i)
        result.append([x for x in i])
    cur.close()
    conn.close()
    return result

    