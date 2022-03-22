import os
from bs4 import BeautifulSoup

def newreward(path:str):
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
                nowfile=path+dir+'\Reward.xml'
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
                
                if data.find('skill'):
                    for skill in data.find_all('skill'):
                        skill.decompose()
                
                #新增tag
                if not data.find('skillSeed'):
                    skillSeed=BeautifulSoup('<skillSeed><skillSeedName><id>-1</id><str>Invalid</str><data /></skillSeedName><skillSeedCount>1</skillSeedCount></skillSeed>','xml')
                    data.find('chara').insert_after(skillSeed)
                
                if not data.find('avatarAccessory'):
                    avatarAccessory=BeautifulSoup('<avatarAccessory><avatarAccessoryName><id>-1</id><str>Invalid</str><data /></avatarAccessoryName></avatarAccessory>','xml')
                    data.find('systemVoice').insert_after(avatarAccessory)

                if not data.find('frame'):
                    frame=BeautifulSoup('<frame><frameName><id>-1</id><str>Invalid</str><data /></frameName></frame>','xml')
                    data.find('avatarAccessory').insert_after(frame)
                
                with open(nowfile,'w',encoding='utf-8')as f:
                    f.write(str(data))
                    f.close()
                

if __name__=='__main__':
    newreward(input())
                
