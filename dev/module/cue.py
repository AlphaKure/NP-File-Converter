import os
import ujson
import shutil

from ERROR import ERRORReport

def cue(path:str):
    '''
    path=Path to cueFile folder
    '''
    #讀取設定 
    with open('setting.json','r',encoding='utf-8')as f:
        setting=ujson.load(f)
        f.close()    
    deretore=setting['deretore']
    critool=setting['critool']
    key=setting['key']
    sat=setting['sat']

    #檢查setting
    if deretore=='':
        ERRORReport('setting',5)
        return
    if not deretore.endswith('hcaenc.exe'):
        ERRORReport('setting',6)
    if critool=='':
        ERRORReport('setting',7)
        return
    if not critool.endswith('index.js'):
        ERRORReport('setting',8)
    if key=='':
        ERRORReport('setting',9)
        return
    if sat=='':
        ERRORReport('setting',10)
        return
    if not sat.endswith('AcbEditor.exe'):
        ERRORReport('setting',11)
        return

    #檢查path
    if os.path.isdir(path):
        if not path.endswith('\\'):
            path=path+'\\'
        dirlist=os.listdir(path)

        #讀取acb檔並解密
        for dir in dirlist:
            filelist=os.listdir(path+dir)
            for file in filelist:
                if file.endswith('.acb'):
                    target_acb=path+dir+'\\'+file
                    print(f'[INFO] Now reading {target_acb}')
                    tmpdir=(path+dir+'\\'+file).replace('.acb','\\')
            os.system(f'node {critool} acb2wavs -k {key} {target_acb} ')
            tmplist=os.listdir(tmpdir)
            filecount=len(tmplist)
            tmplist.sort(key=lambda x:int(x.split('.')[0].split('_')[1]))

            #重新編號命名
            for i in range(0,filecount):
                nowfile=tmpdir+tmplist[i]
                if i<=9:
                    newname=tmpdir+'0000'+str(i)+'_streaming.wav'
                else:
                    newname=tmpdir+'000'+str(i)+'_streaming.wav'
                os.rename(nowfile,newname)
                os.system(f'{deretore} {newname}')
            print(f'[INFO] {target_acb} Convert success')    
        
            #刪除轉換前檔案
            tmplist=os.listdir(tmpdir)
            for file in tmplist:
                if file.endswith('.wav'):
                    os.remove(tmpdir+file)    
            
            #重新包裝
            os.system(f'{sat} {tmpdir[:-1]}')
            shutil.rmtree(tmpdir)
          
        print('[SUCCESS] CueFile convert all done!')    
    else:
        ERRORReport('cueFile',99)
        return



if __name__=='__main__':
    path=str(input('path:'))
    cue(path)