import os
import ujson

import tool

lPreviewTime=list()

def PreviewTimeget(musicID,file):
    global lPreviewTime
    if tool.read_setting('PreviewTime','GetPreviewTime')=='True':
        if tool.read_setting('PreviewTime','PreviewTimeSave')=='False':
            with open(file,'rb')as f:
                Data=f.read().hex()
                f.close()
            lPreviewTime.append({'musicID':musicID,'PrewviewTimeStart':str(int(Data[8236:8242],16)),'PreviewTimeEnd':str(int(Data[8264:8270],16))})


if __name__=='__main__':
    targetdir=input()
    for dir in os.listdir(targetdir):
        for file in os.listdir(targetdir+'\\'+dir):
            if file.endswith('.acb'):
                target_acb=targetdir+'\\'+dir+'\\'+file
                PreviewTimeget(file[5:9],target_acb)

with open('TEST.json','w',encoding='utf-8')as f:
    f.write(ujson.dumps(lPreviewTime))
    f.close()