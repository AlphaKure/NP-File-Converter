from bs4 import BeautifulSoup
import os
import ujson

preview_time_save=True
pt_sava_path='D:\Desktop\pt.json'
pt=list()

auto_disableFlag_fix=True
auto_firstlock_fix=True

def newmusic(path:str):

    global preview_time_save
    global pt_sava_path
    global pt

    global auto_disableFlag_fix
    global auto_firstlock_fix

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
                nowfile=path+dir+'/Music.xml'
                print(f'[INFO] Now reading {nowfile}')

                #開檔
                try:
                    with open(nowfile,'r',encoding='utf-8')as f:
                        data=BeautifulSoup(f.read(),'xml')
                        f.close()
                except:
                    print(f'[ERROR] {nowfile} read failure!')
                    os.system('PAUSE')
                    continue
                
                #修復disableFlag firstLock
                if auto_disableFlag_fix:
                    if data.find('disableFlag'):
                        if data.disableFlag.string=='true':
                            data.disableFlag.string='false'
                            print(f'[SUCCESS] {nowfile} disableFlag Fix!')
                    else:
                        disableflag=BeautifulSoup('<disableFlag>false</disableFlag>','xml')
                        data.netOpenName.insert_after(disableflag)

                if auto_firstlock_fix:
                    if data.firstLock.string=='true':
                        data.firstLock.string='false'
                        print(f'[SUCCESS] {nowfile} firstLock disable!')

                #刪除多餘標籤
                if data.find('resourceVersion'):
                    for resourceVersion in data.find_all('resourceVersion'):
                        resourceVersion.decompose()
                if data.find('rightsInfoName'):
                    data.find('rightsInfoName').decompose()
                if data.find('musicLableID'):
                    data.find('musicLableID').decompose()

                #舊代必定沒有ultima 這邊加回enableultima
                if not data.find('enableUltima'):
                    enableUltimatag=BeautifulSoup('<enableUltima>false</enableUltima>','xml')
                    data.find('firstLock').insert_after(enableUltimatag)
                
                #儲存預覽時間軸
                if preview_time_save:
                    previewStartTime=data.previewStartTime.string
                    previewEndTime=data.previewEndTime.string
                    dataName=data.dataName.string
                    pt.append({'dataName':dataName,'previewStartTime':previewStartTime,'previewEndTime':previewEndTime})
                    
                #處理MusicFumenData 
                musicfumendatastr=['Basic','Advanced','Expert','Master','Ultima','WorldsEnd']   
                musicfumendatasid=0
                for MusicFumenData in data.find_all('MusicFumenData'):
                    if MusicFumenData.data.string!='WORLD\'S END':
                        MusicFumenData.id.string=str(musicfumendatasid)
                        MusicFumenData.str.string=str(musicfumendatastr[musicfumendatasid])
                        if musicfumendatasid==3:
                            Ultimatag=BeautifulSoup('<MusicFumenData><type><id>4</id><str>'+musicfumendatastr[4]+'</str><data>ULTIMA</data></type><file><path /></file><level>0</level><levelDecimal>0</levelDecimal><notesDesigner /><defaultBpm>0</defaultBpm></MusicFumenData>','xml')
                            MusicFumenData.insert_after(Ultimatag)
                    else:
                        MusicFumenData.id.string='5'
                        MusicFumenData.str.string=musicfumendatastr[5]
                        if MusicFumenData.path.string!=None:
                            WEdataname=MusicFumenData.path.string
                            newname=WEdataname[:6]+'5'+WEdataname[7:]
                            MusicFumenData.path.string=newname
                            os.rename(path+dir+'/'+WEdataname,path+dir+'/'+newname)
                    musicfumendatasid+=1

                #寫檔
                with open(nowfile,'w',encoding='utf-8')as f:
                    f.write(str(data))
                    f.close()

        #預覽時間輸出            
        if preview_time_save:
            with open(pt_sava_path,'w',encoding='utf-8')as f:
                ujson.dump(pt,f)    
                f.close()    
        #print(pt)
        #print(data)
        



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
                    elif tag.musicDiff.data.string=='ADVANCE':
                        tag.musicDiff.id.string='1'
                        tag.musicDiff.str.string='Advence'
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
                            elif SubData.diff.data.string=='ADVANCE':
                                SubData.diff.id.string='1'
                                SubData.diff.str.string='Advence'
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
    #newmusic(str(input()))
    newcourse(str(input()))
                

                
                    




                
                


                


                

                
