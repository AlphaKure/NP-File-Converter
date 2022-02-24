import ujson

def read_setting(key:str):
    with open('setting.json','r',encoding='utf-8')as f:
        settings=ujson.load(f)
        f.close()
    return str(settings[key])

def edit_setting(key:str,value:str):
    with open('setting.json','r',encoding='utf-8')as f:
        settings=ujson.load(f)
        f.close()
    settings[key]=value
    with open('setting.json','w',encoding='utf-8')as f:
        ujson.dump(settings,f)
        f.close()