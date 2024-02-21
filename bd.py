import psycopg2
import asyncio

from config import host, user, password, db_name


async def addUser(user_id, username, date, chat_id, language):

                #    f'''INSERT INTO users (UserID, UserName, CurrentTime, ChatID, Language) VALUES
                #('{user_id}', '{username}', '{date}', '{chat_id}', '{language}')'''
    delet = f'''DELETE FROM users WHERE userid = {user_id}'''
    ins = f'''INSERT INTO users (UserID, UserName, CurrentTime, ChatID, Language) VALUES
                ('{user_id}', '@{username}', '{date}', '{chat_id}', '{language}');'''

    try:
        conn = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
    
    
        with conn.cursor() as cursor:
            cursor.execute(delet)
            cursor.execute(ins)
            conn.commit()
    
    except Exception as _ex:
        print('Error:', _ex)
    finally:
        if conn:
            conn.close()
            print('Closed')
    
    
async def getUsers():

    select = '''SELECT userid, username FROM users;'''
        

    try:
        with psycopg2.connect(host=host,user=user,password=password,database=db_name) as conn:
            with conn.cursor() as cursor:
                cursor.execute(select)
                d = cursor.fetchall()
            
        

        #conn = psycopg2.connect(
        #    host=host,
        #    user=user,
        #    password=password,
        #    database=db_name
        #)


            #with conn.cursor() as cursor:
            #    cursor.execute(select)
            #    return 

    except Exception as _ex:
        print('Error:', _ex)
    finally:
        if conn:
            conn.close()
            print('Closed')
    
    text = ''

    for a in d:
        text += f'{a} \n'

    text = text.replace("'",'')
    text = text.replace(")",'')
    text = text.replace("(",'')
    return text


async def getData(user_id):

    select = f'''SELECT messagetime, usersmessage FROM messages WHERE userid = {user_id};'''
        

    try:
        with psycopg2.connect(host=host,user=user,password=password,database=db_name) as conn:
            with conn.cursor() as cursor:
                cursor.execute(select)
                d = cursor.fetchall()
            

    except Exception as _ex:
        print('Error:', _ex)
    finally:
        if conn:
            conn.close()
            print('Closed')
    
    text = ''

    for a in d:
        text += f'{a} \n'

    text = text.replace("'",'')
    text = text.replace(")",'')
    text = text.replace("(",'')
    text = text.replace(",",'\n')
    return text


async def addMessage(user_id, text, date):

    ins = f'''INSERT INTO messages (userid, usersmessage, messagetime) VALUES
            ('{user_id}', '{text}', '{date}');'''

    try:
        conn = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
    
    
        with conn.cursor() as cursor:
            cursor.execute(ins)
            conn.commit()
    
    except Exception as _ex:
        print('Error:', _ex)
    finally:
        if conn:
            conn.close()
            print('Closed')


