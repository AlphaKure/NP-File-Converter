import configparser

def read_setting(section:str,type:str)->str:
    Config=configparser.ConfigParser()
    Config.read('setting.ini')
    return Config[section][type]

print(read_setting('Switch','cue'))