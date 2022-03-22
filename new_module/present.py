import os
from bs4 import BeautifulSoup

def newpresent(path:str):
    #檢查路徑
    if not os.path.isdir(path):
        print('[ERROR] path is not exist.')
        return
    else:
        if not (path.endswith('\\')or path.endswith('/')):
            path+='/'
        dirlist=os.listdir(path)
        for dir in dirlist:
            if not os.path.isdir(path+dir):
                continue
            else:
                nowfile=path+dir+'\Present.xml'
                print(f'[INFO] Now reading {nowfile}')
                try:
                    with open(nowfile, 'r', encoding='utf-8')as f:
                        data = f.read()
                        data = BeautifulSoup(data, 'xml')
                except:
                    print(f'[ERROR] {nowfile} read failure!')
                    os.system('PAUSE')
                    continue

                #刪除多餘tag
                if data.find('resourceVersion'):
                    for resourceVersion in data.find_all('resourceVersion'):
                        resourceVersion.decompose()
                
                if data.find('formatVersion'):
                    for formatVersion in data.find_all('formatVersion'):
                        formatVersion.decompose()
                
                if data.find('skillName'):
                    for skillName in data.find_all('skillName'):
                        skillName.decompose()
                
                #新增tag
                if not data.find('skillSeedName'):
                    skillSeedName=BeautifulSoup('<skillSeedName><id>-1</id><str>Invalid</str><data /></skillSeedName>','xml')
                    data.find('charaName').insert_after(skillSeedName)

                if not data.find('mapIconName'):
                    mapIconName=BeautifulSoup('<mapIconName><id>-1</id><str>Invalid</str><data /></mapIconName>','xml')
                    data.find('namePlateName').insert_after(mapIconName)

                if not data.find('systemVoiceName'):
                    systemVoiceName=BeautifulSoup('<systemVoiceName><id>-1</id><str>Invalid</str><data /></systemVoiceName>','xml')
                    data.find('mapIconName').insert_after(systemVoiceName)

                if not data.find('avatarAccessoryName'):
                    avatarAccessoryName=BeautifulSoup('<avatarAccessoryName><id>-1</id><str>Invalid</str><data /></avatarAccessoryName>','xml')
                    data.find('systemVoiceName').insert_after(avatarAccessoryName)

                if not data.find('frameName'):
                    frameName=BeautifulSoup('<frameName><id>-1</id><str>Invalid</str><data /></frameName>','xml')
                    data.find('avatarAccessoryName').insert_after(frameName)

                if not data.find('symbolChatName'):
                    symbolChatName=BeautifulSoup('<symbolChatName><id>-1</id><str>Invalid</str><data /></symbolChatName>','xml')
                    data.find('frameName').insert_after(symbolChatName)
                
                if not data.find('priority'):
                    priority=BeautifulSoup('<priority>0</priority>','xml')
                    data.find('symbolChatName').insert_after(priority)

                #print(data.prettify())
                
                with open(nowfile,'w',encoding='utf-8')as f:
                    f.write(str(data))
                    f.close()
                

if __name__=='__main__':
    newpresent(input())
                
