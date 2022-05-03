import configparser

def read_setting(section:str,type:str)->str:
    Config=configparser.ConfigParser()
    Config.read('setting.ini') #不能和第四行合併
    return Config[section][type]

