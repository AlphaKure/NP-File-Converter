import os
import ujson


def cue(path:str):


    #讀取設定 deretore路徑
    with open('setting.json','r',encoding='utf-8')as f:
        setting=ujson.load(f)
        f.close()
    deretore=setting['deretore']

    #檢查path
    if os.path.isdir(path):
        if not path.endswith('\\'):
            path=path+'\\'
        filelist=os.listdir(path)
        
        #檢查path內非wav檔(保險用)
        for file in filelist:
            if not file.endswith('.wav'):
                filelist.remove(file)
        filecount=len(filelist)

        #重新編號命名
        for i in range(0,filecount):
            nowfile=path+filelist[i]
            if i<=9:
                newname=path+'0000'+str(i)+'_streaming.wav'
            else:
                newname=path+'000'+str(i)+'_streaming.wav'
            os.rename(nowfile,newname)
            os.system(f'{deretore} {newname}')
        
        #刪除轉換前檔案
        filelist=os.listdir(path)
        for file in filelist:
            if file.endswith('.wav'):
                os.remove(path+file)
        print('[SUCCESS] All Done!')

    else:
        print('[ERROR] path is not exist')

if __name__=='__main__':
    path=str(input('path:'))
    cue(path)