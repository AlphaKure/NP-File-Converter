from bs4 import BeautifulSoup
import os
import shutil

from ERROR import ERRORReport

def music(path:str):
    '''
    path=Path to music folder
    '''
    #檢查路徑
    if os.path.isdir(path):
        if not path.endswith('\\'):
            path = path+'\\'
    
        #開檔處理
        dirlist=os.listdir(path)
        for dir in dirlist:

            ULTIMA=False
            nowfile=path+dir+'\Music.xml'
            print(f'[INFO] Now reading {nowfile}')
            try:
                with open(nowfile, 'r', encoding='utf-8')as f:
                    data = f.read()
                    data = BeautifulSoup(data, 'xml')
            except:
                ERRORReport(nowfile,4)
                return
                
            #檢查disableFlag和firstLock
            if data.disableFlag.string=='true':
                data.disableFlag.string='false'
                print(f'[SUCCESS] {nowfile} disableFlag fix!')
            
            if data.firstLock.string=='true':
                data.firstLock.string='false'
                print(f'[SUCCESS] {nowfile} firstLock disable!')
            

            #是否有ULTIMA譜面
            if data.enableUltima.string=='true':
                ULTIMA=True
            

            #依照有無ULTIMA進行格式修改
            if ULTIMA:
                dataName=data.dataName.string
                dataName=dataName[:5]+'5'+dataName[6:]
                data.dataName.string=dataName
                newnumber=dataName[5:]
                data.find('name').id.string=newnumber
                data.find('name').str.string=data.find('name').str.string+'(ULTIMA)'
                data.genreNames.list.StringID.id.string='100'
                data.genreNames.list.StringID.str.string='ULTIMA'
                for musicdata in data.find_all('MusicFumenData'):
                    id=musicdata.id.string
                    if id=='4' and musicdata.str.string=='Ultima':
                        level=musicdata.level.string
                        Dec=musicdata.levelDecimal.string
                        file=musicdata.file.path.string
                        musicdata.decompose()
                    elif id=='5':
                        musicdata.id.string='4'
                        musicdata.str.string='ID_04'
                    else:
                        musicdata.str.string='ID_0'+id
                        if id!='3':
                            musicdata.enable.string='false'
                            musicdata.level.string='0'
                            musicdata.levelDecimal.string='0'
                data.jaketFile.path.string='CHU_UI_Jacket_'+newnumber+'.dds'


                #第二次搜尋 將master資料以Ultima資料覆蓋
                for musicdata in data.find_all('MusicFumenData'):
                    id=musicdata.id.string
                    if id=='3':
                        musicdata.level.string=level
                        musicdata.levelDecimal.string=Dec
                        musicdata.file.path.string=file
                    else:
                        musicdata.path.string=newnumber+'_0'+id+'.c2s'

            #無ULTIMA譜面     
            else:
                for musicdata in data.find_all('MusicFumenData'):
                    id=musicdata.id.string
                    if id=='4' and musicdata.str.string=='Ultima':
                        musicdata.decompose()
                    elif id=='5':
                        musicdata.id.string='4'
                        musicdata.str.string='ID_04'
                    else:
                        musicdata.str.string='ID_0'+id
            
            #以下為共同修改
            rightinfo=BeautifulSoup('<rightsInfoName><id>0</id><str>なし</str><data /></rightsInfoName>','xml')
            preview=BeautifulSoup('<previewStartTime>50000</previewStartTime><previewEndTime>75000</previewEndTime>','xml')
            data.find('name').insert_after(rightinfo)
            data.find('cueFileName').insert_after(preview)

            if ULTIMA:
                count=0
                base=path+dir
                nowdir=path+dir+'\\'
                for file in os.listdir(nowdir):
                    if file.endswith('.c2s'):
                        os.rename(nowdir+file,nowdir+f'{newnumber}_0{count}.c2s')
                        count+=1
                    elif file.endswith('.dds'):
                        os.rename(nowdir+file,nowdir+f'CHU_UI_Jacket_{newnumber}.dds')
                os.rename(base,path+dataName)
                nowfile=path+dataName+'\Music.xml'

                
            with open(nowfile, 'w', encoding='utf-8')as f:
                f.write(str(data))
                f.close()
            print(f'[INFO] {nowfile} Convert success')   

            '''
            print(data)
            '''
        print('[SUCCESS] Music convert all done!') 
                        
                
    else:
        ERRORReport('music',99)
        return

                
                
        
if __name__=='__main__':
    music(str(input()))