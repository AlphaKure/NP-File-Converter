import os
from bs4 import BeautifulSoup

def newmapBonus(path:str):
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
                nowfile=path+dir+'\MapBonus.xml'
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
                
                for MapBonusSubstanceData in data.find_all('MapBonusSubstanceData'):
                    if MapBonusSubstanceData.find('musicDif'):
                        if MapBonusSubstanceData.musicDif.id.string=='-1':
                            MapBonusSubstanceData.musicDif.str.string='Invalid'
                        elif MapBonusSubstanceData.musicDif.id.string=='0':
                            MapBonusSubstanceData.musicDif.str.string='Basic'
                        elif MapBonusSubstanceData.musicDif.id.string=='1':
                            MapBonusSubstanceData.musicDif.str.string='Advanced'
                        elif MapBonusSubstanceData.musicDif.id.string=='2':
                            MapBonusSubstanceData.musicDif.str.string='Expert'
                        elif MapBonusSubstanceData.musicDif.id.string=='3':
                            MapBonusSubstanceData.musicDif.str.string='Master'
                        elif MapBonusSubstanceData.musicDif.id.string=='4':
                            MapBonusSubstanceData.musicDif.id.string='5'
                            MapBonusSubstanceData.musicDif.str.string='WorldsEnd'
                            MapBonusSubstanceData.musicDif.data.string='WORLD\'S END'
                    if MapBonusSubstanceData.find('skill'):
                        MapBonusSubstanceData.skill.skillName.id.string='-1'
                        MapBonusSubstanceData.skill.skillName.str.string='Invalid'
                        MapBonusSubstanceData.skill.skillName.data.string=''
                    if MapBonusSubstanceData.find('skillCategory'):
                        MapBonusSubstanceData.skillCategory.skillCategory.id.string='-1'
                        MapBonusSubstanceData.skillCategory.skillCategory.str.string='Invalid'
                        MapBonusSubstanceData.skillCategory.skillCategory.data.string=''
                   
                #print(data.prettify())
                with open(nowfile,'w',encoding='utf-8')as f:
                    f.write(str(data))
                    f.close()
                
                    
if __name__=='__main__':
    newmapBonus(input())