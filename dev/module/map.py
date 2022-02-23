from bs4 import BeautifulSoup
import os 
import ujson

from ERROR import ERRORReport


def cgauge_set(gauge:int):
    '''
    gauge:gauge level
    cgauge:1、2、2、3、3、4、4、5、5、6、6...
    '''
    if gauge==0:
        return 0
    elif gauge>0 and gauge<3:
        return 1
    elif gauge>=3 and gauge<5:
        return 2
    elif gauge>=5 and gauge<7:
        return 3
    elif gauge>=7 and gauge<9:
        return 4
    elif gauge>=9 and gauge<11:
        return 5
    elif gauge>=11:
        return 6

def map(path:str):
    '''
    path=Path to map folder
    '''
    gauge=0
    

    #開啟cgauge
    with open('dev/data/cgauge.json','r',encoding='utf-8')as f:
        cgauge=ujson.load(f)
        f.close()

    #檢查路徑
    if os.path.isdir(path):
        if not path.endswith('\\'):
            path = path+'\\'

        #開檔處理
        dirlist=os.listdir(path)
        for dir in dirlist:
            nowfile=path+dir+'\Map.xml'
            print(f'[INFO] Now reading {nowfile}')
            try:
                with open(nowfile, 'r', encoding='utf-8')as f:
                    data = f.read()
                    data = BeautifulSoup(data, 'xml')
                    f.close()
            except:
                ERRORReport(nowfile,4)
                return
        
            for tags in data.find_all('gaugeName'):
                tags.name='normalGaugeName'
            
            #課題
            for info in data.find_all('MapDataAreaInfo'):
                if info.musicName.id.string!='-1':
                    if not info.find('challengeGaugeName'):
                        lg=cgauge_set(gauge)
                        newtag=BeautifulSoup('<challengeGaugeName><id>'+cgauge[lg]['id']+'</id><str>'+cgauge[lg]['id']+'</str><data /></challengeGaugeName>','xml')
                        info.append(newtag)
                        gauge+=1

        
            #寫檔
            with open(nowfile, 'w', encoding='utf-8')as f:
                f.write(str(data))
                f.close()
            print(f'[INFO] {nowfile} Convert success')     
        
        print('[SUCCESS] Map convert all done!')
                
        


    else:
        ERRORReport('map',99)
        return
    
if __name__=='__main__':
    map(str(input()))