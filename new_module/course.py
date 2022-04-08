import os
from bs4 import BeautifulSoup


def newcourse(path:str):
    
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
                nowfile=path+dir+'\Course.xml'
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
                if data.find('category'):
                    data.find('category').decompose()
                #修復disableFlag
                if data.find('disableFlag'):
                    if data.disableFlag.string=='true':
                        data.disableFlag.string='false'
                        print(f'[SUCCESS] {nowfile} disableFlag Fix!')

                #新增標籤
                if not data.find('reward2nd'):
                    reward2nd=BeautifulSoup('<reward2nd><id>0</id><str>なし</str><data /></reward2nd>','xml')
                    data.reward.insert_after(reward2nd)
                if not data.find('teamOnly'):
                    teamOnly=BeautifulSoup('<teamOnly>false</teamOnly>','xml')
                    data.reward2nd.insert_after(teamOnly)
                if not data.find('isMusicDuplicateAllowed'):
                    isMusicDuplicateAllowed=BeautifulSoup('<isMusicDuplicateAllowed>true</isMusicDuplicateAllowed>','xml')
                    data.teamOnly.insert_after(isMusicDuplicateAllowed)
                

                #將tag內資料修改為new支援的
                for tag in data.find_all('CourseMusicDataInfo'):
                    if tag.musicDiff.data.string=='BASIC':
                        tag.musicDiff.id.string='0'
                        tag.musicDiff.str.string='Basic'
                    elif tag.musicDiff.data.string=='ADVANCED':
                        tag.musicDiff.id.string='1'
                        tag.musicDiff.str.string='Advenced'
                    elif tag.musicDiff.data.string=='EXPERT':
                        tag.musicDiff.id.string='2'
                        tag.musicDiff.str.string='Expert'
                    elif tag.musicDiff.data.string=='MASTER':
                        tag.musicDiff.id.string='3'
                        tag.musicDiff.str.string='Master'
                    elif tag.musicDiff.data.string=='WORLD\'S END':
                        tag.musicDiff.id.string='5'
                        tag.musicDiff.str.string='WorldsEnd'
                    elif tag.musicDiff.data.string=='ULTIMA':
                        tag.musicDiff.id.string='4'
                        tag.musicDiff.str.string='Ultima' 
                    if data.find('CourseMusicListSubData'):
                        for SubData in data.find_all('CourseMusicListSubData'):
                            if SubData.diff.data.string=='BASIC':
                                SubData.diff.id.string='0'
                                SubData.diff.str.string='Basic'
                            elif SubData.diff.data.string=='ADVANCED':
                                SubData.diff.id.string='1'
                                SubData.diff.str.string='Advenced'
                            elif SubData.diff.data.string=='EXPERT':
                                SubData.diff.id.string='2'
                                SubData.diff.str.string='Expert'
                            elif SubData.diff.data.string=='MASTER':
                                SubData.diff.id.string='3'
                                SubData.diff.str.string='Master'
                            elif SubData.diff.data.string=='WORLD\'S END':
                                SubData.diff.id.string='5'
                                SubData.diff.str.string='WorldsEnd'
                            elif SubData.diffdata.string=='ULTIMA':
                                SubData.diffid.string='4'
                                SubData.diff.str.string='Ultima'
            #print(data)
                with open(nowfile, 'w', encoding='utf-8')as f:
                    f.write(str(data))
                    f.close()

if __name__=='__main__':
    newcourse(input())