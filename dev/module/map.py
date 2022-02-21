from bs4 import BeautifulSoup
import os 


from ERROR import ERRORReport

def map(path:str):
    '''
    path=Path to map folder
    '''
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