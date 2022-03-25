import os
from bs4 import BeautifulSoup

def newtrophy(path:str):
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
                nowfile=path+dir+'\Trophy.xml'
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
                if data.find('openCondition'):
                    for openCondition in data.find_all('openCondition'):
                        openCondition.decompose()
                if data.find('rankMax'):
                    for rankMax in data.find_all('rankMax'):
                        rankMax.decompose()
                
                #新增tag
                if not data.find('disableFlag'):
                    disableFlag=BeautifulSoup('<disableFlag>false</disableFlag>','xml')
                    data.find('netOpenName').insert_after(disableFlag)

                #修改tag
                for ConditionSubData in data.find_all('ConditionSubData'):

                    if ConditionSubData.playMusicData.musicDif.id.string=='0':
                        ConditionSubData.playMusicData.musicDif.str.string='Basic'
                    elif ConditionSubData.playMusicData.musicDif.id.string=='1':
                        ConditionSubData.playMusicData.musicDif.str.string='Advanced'
                    elif ConditionSubData.playMusicData.musicDif.id.string=='2':
                        ConditionSubData.playMusicData.musicDif.str.string='Expert'
                    elif ConditionSubData.playMusicData.musicDif.id.string=='3':
                        ConditionSubData.playMusicData.musicDif.str.string='Master'
                    elif ConditionSubData.playMusicData.musicDif.id.string=='4':
                        ConditionSubData.playMusicData.musicDif.id.string='5'
                        ConditionSubData.playMusicData.musicDif.str.string='WorldsEnd'
                    
                    if not ConditionSubData.find('totalNetBattle'):
                        totalNetBattle=BeautifulSoup('<totalNetBattle>0</totalNetBattle>','xml')
                        ConditionSubData.find('totalGamePoint').insert_after(totalNetBattle)
                    if not ConditionSubData.find('battleRank'):
                        battleRank=BeautifulSoup('<battleRank><id>-1</id><str>Invalid</str><data /></battleRank>','xml')
                        ConditionSubData.find('totalNetBattle').insert_after(battleRank)
                    if not ConditionSubData.find('lapNum'):
                        lapNum=BeautifulSoup('<lapNum>0</lapNum>','xml')
                        ConditionSubData.find('playedRegionNum').insert_after(lapNum)
                    
                    if ConditionSubData.musicData.musicDif.id.string=='0':
                        ConditionSubData.musicData.musicDif.str.string='Basic'
                    elif ConditionSubData.musicData.musicDif.id.string=='1':
                        ConditionSubData.musicData.musicDif.str.string='Advanced'
                    elif ConditionSubData.musicData.musicDif.id.string=='2':
                        ConditionSubData.musicData.musicDif.str.string='Expert'
                    elif ConditionSubData.musicData.musicDif.id.string=='3':
                        ConditionSubData.musicData.musicDif.str.string='Master'
                    elif ConditionSubData.musicData.musicDif.id.string=='4':
                        ConditionSubData.musicData.musicDif.id.string='5'
                        ConditionSubData.musicData.musicDif.str.string='WorldsEnd'

                    if not ConditionSubData.find('totalPlayNum'):
                        totalPlayNum=BeautifulSoup('<totalPlayNum>0</totalPlayNum>','xml')
                        ConditionSubData.find('masterUnderAll').insert_after(totalPlayNum)

                with open(nowfile,'w',encoding='utf-8')as f:
                    f.write(str(data))
                    f.close()

if __name__=='__main__':
    newtrophy(input())
                    
                 