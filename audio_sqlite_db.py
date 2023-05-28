import sqlite3 as sq
from datetime import datetime
import pandas as pd 

def sql_start(logger) -> None:
    global dbase, cur
    dbase = sq.connect('yandex_stt.db')
    cur = dbase.cursor()
    if dbase:
        logger.warning("yandex_stt: Data base connected Ok!")
    dbase.execute('create table if not exists yandex_stt_use_log(use_date TEXT, user_name TEXT, user_id TEXT, action TEXT, words INT, language_code TEXT, confidence REAL)')
    dbase.commit()

def use_log_add_command(user_name, user_id, action, words, language_code, confidence):
    use_date = datetime.now()
    params = (use_date, user_name, user_id, action, words, language_code, confidence)
    dbase.execute('insert into yandex_stt_use_log values (?,?,?,?,?,?,?)', params)
    dbase.commit()

def sql_read() -> pd.DataFrame :
    df = pd.read_sql_query("SELECT * FROM yandex_stt_use_log", dbase)
    return df

