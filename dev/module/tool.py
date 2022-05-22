import configparser
import ujson

lPreviewTime=list()

def read_setting(section:str,type:str)->str:
    Config=configparser.ConfigParser()
    Config.read('setting.ini') #不能和第四行合併
    return Config[section][type]

def SavePreviewTime():
    if read_setting('PreviewTime','PreviewTimeSave')=='True':
        if read_setting('PreviewTime','PreviewTimeSavePath')=='':
            print('[ERROR] You didn\'t set Save Path for PreviewTime')
            return
        global lPreviewTime
        with open(read_setting('PreviewTime','PreviewTimeSavePath'),'w',encoding='utf-8')as f:
            f.write(ujson.dumps(lPreviewTime))
            f.close()

def PreviewTimeget(musicID,file):
    global lPreviewTime
    if read_setting('PreviewTime','GetPreviewTime')=='True':
        with open(file,'rb')as f:
            Data=f.read().hex()
            f.close()
        lPreviewTime.append({'musicID':musicID,'PrewviewTimeStart':str(int(Data[8236:8242],16)),'PreviewTimeEnd':str(int(Data[8264:8270],16))})


def XmlFormater():
    pass