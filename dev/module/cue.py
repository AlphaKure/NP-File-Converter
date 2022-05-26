import os
import shutil

try:
    import ERROR
    import tool
except ModuleNotFoundError:
    import dev.module.ERROR as ERROR
    import dev.module.tool as tool


def Cue(Path:str):
    
    #讀取設定 
    ToolDeretore=tool.ReadSetting('ToolPath','deretore')
    ToolCritool=tool.ReadSetting('ToolPath','critool')
    AcbKey=tool.ReadSetting('ToolPath','key')
    ToolSAT=tool.ReadSetting('ToolPath','sat')

    #檢查setting
    if ToolDeretore=='':
        ERROR.ErrorReport('setting',5)
        return
    if not ToolDeretore.endswith('hcaenc.exe'):
        ERROR.ErrorReport('setting',6)
    if ToolCritool=='':
        ERROR.ErrorReport('setting',7)
        return
    if not ToolCritool.endswith('index.js'):
        ERROR.ErrorReport('setting',8)
    if AcbKey=='':
        ERROR.ErrorReport('setting',9)
        return
    if ToolSAT=='':
        ERROR.ErrorReport('setting',10)
        return
    if not ToolSAT.endswith('AcbEditor.exe'):
        ERROR.ErrorReport('setting',11)
        return

    #檢查path
    if os.path.isdir(Path):
        if not Path.endswith('\\'):
            Path=Path+'\\'

        #讀取acb檔並解密
        for Dir in os.listdir(Path):
            for File in os.listdir(Path+Dir):
                if File.endswith('.acb'):
                    TargetAcb=Path+Dir+'\\'+File
                    print(f'[INFO] Now reading {TargetAcb}')
                    if tool.ReadSetting('PreviewTime','GetPreviewTime').lower()=='true':
                        if int(File[7:])<10000:
                            tool.PreviewTimeget(File[5:9],TargetAcb)
                    TempDir=(Path+Dir+'\\'+File).replace('.acb','\\')
            os.system(f'node {ToolCritool} acb2wavs -k {AcbKey} {TargetAcb} ')
            TempList=os.listdir(TempDir)
            FileCount=len(TempList)
            TempList.sort(key=lambda x:int(x.split('.')[0].split('_')[1]))

            #重新編號命名
            for Num in range(0,FileCount):
                NowFile=TempDir+TempList[Num]
                if Num<=9:
                    NewFileName=TempDir+'0000'+str(Num)+'_streaming.wav'
                else:
                    NewFileName=TempDir+'000'+str(Num)+'_streaming.wav'
                os.rename(NowFile,NewFileName)
                os.system(f'{ToolDeretore} {NewFileName}')
            print(f'[INFO] {TargetAcb} Convert success')    
        
            #刪除轉換前檔案
            TempList=os.listdir(TempDir)
            for File in TempList:
                if File.endswith('.wav'):
                    os.remove(TempDir+File)    
            
            #重新包裝
            os.system(f'{ToolSAT} {TempDir[:-1]}')
            shutil.rmtree(TempDir)

            #Save PreviewTime
            if tool.ReadSetting('PreviewTime','PreviewTimeSave').lower()=='true':
                tool.SavePreviewTime()

        print('[SUCCESS] CueFile convert all done!')    
    else:
        ERROR.ErrorReport('cueFile',99)
        return



if __name__=='__main__':
    Cue(str(input('path:')))