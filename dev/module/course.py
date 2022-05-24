import os
from bs4 import BeautifulSoup

try:
    import ERROR
    import tool
except ModuleNotFoundError:
    import dev.module.ERROR as ERROR
    import dev.module.tool as tool


def course(path:str):

    #檢查路徑
    if os.path.isdir(path):
        if not path.endswith('\\'):
            path = path+'\\'
    
        #開檔處理
        dirlist=os.listdir(path)
        for dir in dirlist:

            nowfile=path+dir+'\Course.xml'
            try:
                with open(nowfile, 'r', encoding='utf-8')as f:
                    data = f.read()
                    data = BeautifulSoup(data, 'xml')
            except:
                ERROR.ERRORReport(nowfile,4)
                return
            
            #將tag內資料修改為Para支援的
            for tag in data.find_all('CourseMusicDataInfo'):
                if tag.musicDiff.data.string=='BASIC':
                    tag.musicDiff.id.string='0'
                    tag.musicDiff.str.string='ID_00'
                elif tag.musicDiff.data.string=='ADVANCE':
                    tag.musicDiff.id.string='1'
                    tag.musicDiff.str.string='ID_01'
                elif tag.musicDiff.data.string=='EXPERT':
                    tag.musicDiff.id.string='2'
                    tag.musicDiff.str.string='ID_02'
                elif tag.musicDiff.data.string=='MASTER':
                    tag.musicDiff.id.string='3'
                    tag.musicDiff.str.string='ID_03'
                elif tag.musicDiff.data.string=='WORLD\'S END':
                    tag.musicDiff.id.string='4'
                    tag.musicDiff.str.string='ID_04'
                elif tag.musicDiff.data.string=='ULTIMA':
                    tag.musicDiff.id.string='3'
                    tag.musicDiff.str.string='ID_03'
                    tag.musicName.id.string='5'+tag.musicName.id.string
            
            #print(data)

            with open(nowfile, 'w', encoding='utf-8')as f:
                f.write(str(data))
                f.close()
            tool.XMLFormat(nowfile)

            print(f'[INFO] {nowfile} Convert success')   

if __name__=='__main__':
    course(str(input()))