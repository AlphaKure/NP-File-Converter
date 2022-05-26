from bs4 import BeautifulSoup
import os

try:
    import ERROR
    import tool
except ModuleNotFoundError:
    import dev.module.ERROR as ERROR
    import dev.module.tool as tool


def Music(Path:str):
    '''
    path=Path to music folder
    '''

    #需不需要修改
    EnableFixFirstLock=tool.ReadSetting('Detail','music_fix_firstLock')
    EnableFixDisableFlag=tool.ReadSetting('Detail','music_fix_disableFlag')


    #檢查路徑
    if os.path.isdir(Path):
        if not Path.endswith('\\'):
            Path = Path+'\\'
    
        #開檔處理
        for Dir in os.listdir(Path):

            HaveUltima=False
            NowFile=Path+Dir+'\Music.xml'
            print(f'[INFO] Now reading {NowFile}')
            try:
                with open(NowFile, 'r', encoding='utf-8')as File:
                    Data = File.read()
                    Data = BeautifulSoup(Data, 'xml')
            except:
                ERROR.ErrorReport(NowFile,4)
                return
                
            #檢查disableFlag和firstLock
            if EnableFixFirstLock=='True':
                if Data.disableFlag.string=='true':
                    Data.disableFlag.string='false'
                    print(f'[SUCCESS] {NowFile} disableFlag fix!')
            if EnableFixDisableFlag=='True':
                if Data.firstLock.string=='true':
                    Data.firstLock.string='false'
                    print(f'[SUCCESS] {NowFile} firstLock disable!')
            

            #是否有ULTIMA譜面
            if Data.enableUltima.string=='true':
                HaveUltima=True
            

            #依照有無ULTIMA進行格式修改
            if HaveUltima:
                DataUltima=False
                Data.releaseTagName.id.string='12'
                Data.releaseTagName.str.string='v2 2.00.00'
                DataName=Data.dataName.string
                DataName=DataName[:5]+'5'+DataName[6:]
                Data.dataName.string=DataName
                NewNumber=DataName[5:]
                Data.find('name').id.string=NewNumber
                Data.find('name').str.string=Data.find('name').str.string+'(ULTIMA)'
                Data.genreNames.list.StringID.id.string='100'
                Data.genreNames.list.StringID.str.string='ULTIMA'
                for MusicData in Data.find_all('MusicFumenData'):
                    MusicDataID=MusicData.id.string
                    if MusicDataID=='4' and MusicData.str.string=='Ultima':
                        DataUltima=True #有Ultime 將Ultima資料緩存
                        UltimaLevel=MusicData.level.string
                        UltimaDec=MusicData.levelDecimal.string
                        MusicData.decompose()
                    elif MusicDataID=='5':
                        MusicData.id.string='4'
                        MusicData.str.string='ID_04'
                    else:
                        MusicData.str.string='ID_0'+MusicDataID
                        if MusicDataID!='3':
                            MusicData.enable.string='false'
                            MusicData.level.string='0'
                            MusicData.levelDecimal.string='0'
                Data.jaketFile.path.string='CHU_UI_Jacket_'+NewNumber+'.dds'


                #第二次搜尋 將master資料以Ultima資料覆蓋
                for MusicData in Data.find_all('MusicFumenData'):
                    MusicDataID=MusicData.id.string
                    if MusicDataID=='3':
                        if DataUltima:
                            MusicData.level.string=UltimaLevel
                            MusicData.levelDecimal.string=UltimaDec
                            MusicData.file.path.string=NewNumber+'_04.c2s'
                    else:
                        MusicData.path.string=NewNumber+'_0'+MusicDataID+'.c2s'

            #無ULTIMA譜面     
            else:
                for MusicData in Data.find_all('MusicFumenData'):
                    MusicDataID=MusicData.id.string
                    if MusicDataID=='4' and MusicData.str.string=='Ultima':
                        MusicData.decompose()
                    elif MusicDataID=='5':
                        MusicData.id.string='4'
                        MusicData.str.string='ID_04'
                    else:
                        MusicData.str.string='ID_0'+MusicDataID
            
            #以下為共同修改
            RightInfo=BeautifulSoup('<rightsInfoName><id>0</id><str>なし</str><data /></rightsInfoName>','xml')

            #PreviewTime
            if tool.ReadSetting('PreviewTime','GetPreviewTime').lower()=='false':
                PreviewStartTag=BeautifulSoup('<previewStartTime>50000</previewStartTime>','xml')
                PreviewEndTag=BeautifulSoup('<previewEndTime>75000</previewEndTime>','xml')
            else:
                StartTime,EndTime=tool.FindPreviewTime(Data.find('jaketFile').path.string[14:18])
                PreviewStartTag=BeautifulSoup('<previewStartTime>'+StartTime+'</previewStartTime>','xml')
                PreviewEndTag=BeautifulSoup('<previewEndTime>'+EndTime+'</previewEndTime>','xml')
            if not Data.find('rightsInfoName'):
                Data.find('name').insert_after(RightInfo)
            if not Data.find('previewStartTime'):
                Data.find('cueFileName').insert_after(PreviewStartTag)
                Data.find('previewStartTime').insert_after(PreviewEndTag)

            if HaveUltima:
                Count=0
                Base=Path+Dir
                NowDir=Path+Dir+'\\'
                for File in os.listdir(NowDir):
                    if File.endswith('.c2s'):
                        os.rename(NowDir+File,NowDir+f'{NewNumber}_0{Count}.c2s')
                        Count+=1
                    elif File.endswith('.dds'):
                        os.rename(NowDir+File,NowDir+f'CHU_UI_Jacket_{NewNumber}.dds')
                os.rename(Base,Path+DataName)
                NowFile=Path+DataName+'\Music.xml'

                
            with open(NowFile, 'w', encoding='utf-8')as File:
                File.write(str(Data))
                File.close()
            tool.XMLFormat(NowFile) 

            print(f'[INFO] {NowFile} Convert success')   

            '''
            print(data)
            '''
        print('[SUCCESS] Music convert all done!') 
                        
                
    else:
        ERROR.ErrorReport('music',99)
        return

                
                
        
if __name__=='__main__':
    Music(str(input()))