import audio_sqlite_db

import json, asyncio


#file = open('/home/pavel/cfg/config.json', 'r')
#config = json.load(file)

#
if __name__ == '__main__':
    df = audio_sqlite_db.sql_read()
    print(df.info())
    print(df.iloc[0:2, [0,1,3]])
        #df.size

        #bbuf = str(df[['use_date', 'user_name', 'action']].iloc[my_lang.get_qty_to_select()])