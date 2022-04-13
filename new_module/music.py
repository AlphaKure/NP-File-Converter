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

                #處理stageid更改
                for stageName in data.find_all('stageName'):
                    if stageName.str.string=='WORLD\'S END0001_ノイズ':
                        stageName.id.string='0'
                    elif stageName.str.string=='レーベル 共通0001_イエローリング':
                        stageName.id.string='1'
                    elif stageName.str.string=='レーベル 共通0002_AIR':
                        stageName.id.string='2'
                    elif stageName.str.string=='レーベル 共通0003_STAR':
                        stageName.id.string='3'
                    elif stageName.str.string=='レーベル 共通0004_AMAZON':
                        stageName.id.string='4'
                    elif stageName.str.string=='レーベル 共通0005_CRYSTAL':
                        stageName.id.string='5'
                    elif stageName.str.string=='レーベル 共通0006_PARADISE':
                        stageName.id.string='6'
                    elif stageName.str.string=='レーベル 共通0007_PARADISELOST':
                        stageName.id.string='7'
                    elif stageName.str.string=='レーベル 共通0008_新イエローリング':
                        stageName.id.string='8'
                    
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
        
                
if __name__=='__main__':
    newmusic(str(input()))
    

                
                    




                
                


                


                

