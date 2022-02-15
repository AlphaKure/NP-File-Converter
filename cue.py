import os

deretore='D:\DeskTop\deretore\hcaenc.exe'

def cue(path:str):
    if os.path.isdir(path):
        if not path.endswith('\\'):
            path=path+'\\'
        filelist=os.listdir(path)
        for file in filelist:
            if not file.endswith('.wav'):
                filelist.remove(file)
        filecount=len(filelist)
        for i in range(0,filecount):
            nowfile=path+filelist[i]
            if i<=9:
                newname=path+'0000'+str(i)+'_streaming.wav'
            else:
                newname=path+'000'+str(i)+'_streaming.wav'
            os.rename(nowfile,newname)
            os.system(f'{deretore} {newname}')
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