import configparser

import ujson
from lxml import etree

def read_setting(Section:str,Type:str)->str:
    Config=configparser.ConfigParser()
    Config.read('setting.ini') #不能和第四行合併
    return Config[Section][Type]


PreviewTimeList=list()

def InitPreviewTimeList():
    global PreviewTimeList
    try:
        PreviewTimeSavePath=read_setting('PreviewTime','PreviewTimeSavePath')
        with open(PreviewTimeSavePath,'r',encoding='utf-8')as File:
            PreviewTimeList=ujson.dumps(File.read())
            File.close()
    except:
        pass

def SavePreviewTime():
    if read_setting('PreviewTime','PreviewTimeSavePath')=='':
        print('[ERROR] You didn\'t set Save Path for PreviewTime')
        return
    global PreviewTimeList
    with open(read_setting('PreviewTime','PreviewTimeSavePath'),'w',encoding='utf-8')as File:
        File.write(ujson.dumps(PreviewTimeList))
        File.close()

def PreviewTimeget(musicID,FileName):
    global PreviewTimeList
    with open(FileName,'rb')as File:
        Data=File.read().hex()
        File.close()
    PreviewTimeList.append({'musicID':musicID,'PreviewTimeStart':str(int(Data[8236:8242],16)),'PreviewTimeEnd':str(int(Data[8264:8270],16))})

def FindPreviewTime(TargetID):
    global PreviewTimeList
    for Item in PreviewTimeList:
        if Item['musicID']==TargetID:
           return Item['PreviewTimeStart'],Item['PrevieTimeEnd']
    print(f'[ERROR] Not Found ID {TargetID}')
    return '50000','75000'

def XMLFormat(File):
    Parser = etree.XMLParser(remove_blank_text=True)
    Tree = etree.parse(File, Parser)
    Tree.write(File, pretty_print=True,encoding='utf-8',xml_declaration=True)