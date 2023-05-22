import json

with open('/home/pavel/cfg/words.json', 'r', encoding='utf-8') as ffile:
    data = json.load(ffile)
    
    if {'чернозадый'}\
        .intersection(set(i['word'] for i in data)) != set():
        print('word')
    else:
        print('----')

    #print(intersection(set(data)))
    #for i in data:
    #for i in data: print(i['word'])
    #for i in data: i['word']