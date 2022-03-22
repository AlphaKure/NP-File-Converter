import os
from bs4 import BeautifulSoup

from cross import mapFilter

def newevent(path:str):
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
                nowfile=path+dir+'\Event.xml'
                print(f'[INFO] Now reading {nowfile}')
                try:
                    with open(nowfile, 'r', encoding='utf-8')as f:
                        data = f.read()
                        data = BeautifulSoup(data, 'xml')
                except:
                    print(f'[ERROR] {nowfile} read failure!')
                    os.system('PAUSE')
                    continue
            
                #刪除多餘標籤
                if data.find('resourceVersion'):
                    for resourceVersion in data.find_all('resourceVersion'):
                        resourceVersion.decompose()
                
                if data.find('formatVersion'):
                    for formatVersion in data.find_all('formatVersion'):
                        formatVersion.decompose()

                if data.information.find('mapType'):
                    for mapType in data.information.find_all('mapType'):
                        mapType.decompose()
                if data.find('isAou'):
                    for isAou in data.find_all('isAou'):
                        isAou.decompose()
                
                #fix alwaysopen
                if data.alwaysOpen.string=='false':
                    data.alwaysOpen.string='true'

                

                #新增標籤
                if not data.find('netOpenName'):#不確定有無影響
                    netOpenName=BeautifulSoup('<netOpenName><id>2000</id><str>v2_00 00_0</str><data /></netOpenName>','xml')
                    data.find('dataName').insert_after(netOpenName)

                if not data.find('teamOnly'):
                    teamOnly=BeautifulSoup('<teamOnly>false</teamOnly>','xml')
                    data.find('alwaysOpen').insert_after(teamOnly)
                
                if not data.find('isKop'):
                    isKop=BeautifulSoup('<isKop>false</isKop>','xml')
                    data.find('teamOnly').insert_after(isKop)

                #substances information tag add
                if not data.substances.information.find('informationDispType'): #我沒有找到規律，於是暫定全部為0
                    informationDispType=BeautifulSoup('<informationDispType>0</informationDispType>','xml')
                    data.find('informationType').insert_after(informationDispType)
                
                if not data.substances.information.find('mapFilterID'): #不確定有無影響 map裡已經有Filter了
                    mapFilterID=BeautifulSoup('<mapFilterID><id>-1</id><str>Invalid</str><data /></mapFilterID>','xml')
                    data.find('informationDispType').insert_after(mapFilterID)
                else:
                    nid,nstr,ndata=mapFilter(data.substances.information.mapFilterID.id.string)
                    data.substances.information.mapFilterID.id.string=nid
                    data.substances.information.mapFilterID.str.string=nstr
                    data.substances.information.mapFilterID.data.string=ndata

                if not data.substances.information.find('courseNames'):#不確定有無影響 反正我是不想轉course
                    courseNames=BeautifulSoup('<courseNames><list /></courseName>','xml')
                    data.substances.information.find('mapFilterID').insert_after(courseNames)

                if not data.substances.information.find('text'):
                    text=BeautifulSoup('<text />','xml')
                    data.substances.information.find('courseNames').insert_after(text)
                
                #substances other tag add
                if not data.substances.find('release'):
                    release=BeautifulSoup('<release><value>0</value></release>','xml')
                    data.find('recommendMusic').insert_after(release)

                if not data.substances.find('course'):
                    course=BeautifulSoup('<course><courseNames><list /></courseNames></course>','xml')
                    data.substances.find('release').insert_after(course)

                if not data.substances.find('quest'):
                    quest=BeautifulSoup('<quest><questNames><list /></questNames></quest>','xml')
                    data.substances.find('course').insert_after(quest)

                if not data.substances.find('duel'):
                    duel=BeautifulSoup('<duel><duelName><id>-1</id><str>Invalid</str><data /></duelName></duel>','xml')
                    data.substances.find('quest').insert_after(duel)

                if not data.substances.find('changeSurfBoardUI'):
                    changeSurfBoardUI=BeautifulSoup('<changeSurfBoardUI><value>0</value></changeSurfBoardUI>','xml')
                    data.substances.find('duel').insert_after(changeSurfBoardUI)
                
                if not data.substances.find('avatarAccessoryGacha'):
                    avatarAccessoryGacha=BeautifulSoup('<avatarAccessoryGacha><avatarAccessoryGachaName><id>-1</id><str>Invalid</str><data /></avatarAccessoryGachaName></avatarAccessoryGacha>','xml')
                    data.substances.find('changeSurfBoardUI').insert_after(avatarAccessoryGacha)
                
                if not data.substances.find('rightsInfo'):
                    rightsInfo=BeautifulSoup('<rightsInfo><rightsNames><list /></rightsNames></rightsInfo>','xml')
                    data.substances.find('avatarAccessoryGacha').insert_after(rightsInfo)
                
                if not data.substances.find('battleReward'):
                    battleReward=BeautifulSoup('<battleReward><battleRewardName><id>-1</id><str>Invalid</str><data /></battleRewardName></battleReward>','xml')
                    data.substances.find('rightsInfo').insert_after(battleReward)
            #print(data)
            with open(nowfile,'w',encoding='utf-8')as f:
                f.write(str(data))
                f.close()
               
if __name__=='__main__':
    newevent(input())