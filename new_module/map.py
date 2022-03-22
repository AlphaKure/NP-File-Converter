import os
from bs4 import BeautifulSoup

from cross import mapFilter


def cgauge(count:int):
    #1*1 2 4 5 6 8各*4
    if count==1:
        gid='11'
        gstr='基本セット11'
    elif count>1 and count<=5:
        gid='12'
        gstr='基本セット12'
    elif count>5 and count<=9:
        gid='14'
        gstr='基本セット14'
    elif count>9 and count<=13:
        gid='15'
        gstr='基本セット15'
    elif count>13 and count<=17:
        gid='16'
        gstr='基本セット16'
    else:
        gid='18'
        gstr='基本セット18'
    return gid,gstr
    
    



def newmap(path:str):
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
                nowfile=path+dir+'\Map.xml'
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
                if data.find('stopUnlockEventName'):
                    for stopUnlockEventName in data.find_all('stopUnlockEventName'):
                        stopUnlockEventName.decompose()
                        
                #修改標籤名稱    
                if data.find('stopMapAreaName'):
                    data.find('stopMapAreaName').name='stopReleaseEventName'


                #修改標籤
                if data.find('mapFilterID'):
                    nid,nstr,ndata=mapFilter(data.mapFilterID.id.string)
                    data.mapFilterID.id.string=nid
                    data.mapFilterID.str.string=nstr
                    data.mapFilterID.data.string=ndata


                #新增標籤
                if not data.find('categoryName'):
                    categoryName=BeautifulSoup('<categoryName><id>0</id><str>設定なし</str><data /></categoryName>','xml')
                    data.find('mapFilterID').insert_after(categoryName)
                
                if not data.find('timeTableName'):
                    timeTableName=BeautifulSoup('<timeTableName><id>-1</id><str>Invalid</str><data/></timeTableName>','xml')
                    data.find('categoryName').insert_after(timeTableName)

                if not data.find('stopPageIndex'):
                    stopPageIndex=BeautifulSoup('<stopPageIndex>0</stopPageIndex>','xml')
                    data.find('timeTableName').insert_after(stopPageIndex)

                #更改格式
                gaugecount=1
                page=0
                index=0
                for MapDataAreaInfo in data.find_all('MapDataAreaInfo'):                        

                    MapDataAreaInfo.normalGaugeName.decompose()
                    MapDataAreaInfo.challengeGaugeName.decompose()
                    MapDataAreaInfo.challengeRating.decompose()

                    if not MapDataAreaInfo.find('isHard'):
                        isHard=BeautifulSoup('<isHard>false</isHard>','xml')
                        MapDataAreaInfo.rewardName.insert_after(isHard)

                    if not MapDataAreaInfo.find('pageIndex'):
                        pageIndex=BeautifulSoup('<pageIndex>'+str(page)+'</pageIndex>','xml')
                        MapDataAreaInfo.find('isHard').insert_after(pageIndex)

                    if not MapDataAreaInfo.find('indexInPage'):
                        indexInPage=BeautifulSoup('<indexInPage>'+str(index)+'</indexInPage>','xml')
                        MapDataAreaInfo.find('pageIndex').insert_after(indexInPage)
                        if index!=8:
                            index+=1
                        else:
                            index=0
                            page+=1
                    
                    if not MapDataAreaInfo.find('requiredAchievementCount'):
                        requiredAchievementCount=BeautifulSoup('<requiredAchievementCount>0</requiredAchievementCount>','xml')
                        MapDataAreaInfo.find('indexInPage').insert_after(requiredAchievementCount)
                    
                    if not MapDataAreaInfo.find('gaugeName'):
                        gid,gstr=cgauge(gaugecount)
                        gaugeName=BeautifulSoup('<gaugeName><id>'+gid+'</id><str>'+gstr+'</str><data /></gaugeName>','xml')
                        MapDataAreaInfo.find('requiredAchievementCount').insert_after(gaugeName)
                        gaugecount+=1
                    
                    with open(nowfile,'w',encoding='utf-8')as f:
                        f.write(str(data))
                        f.close()



if __name__=='__main__':
    newmap(input())

