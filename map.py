from bs4 import BeautifulSoup
import os 

def map(path:str):
    
    #檢查路徑
    if os.path.isdir(path):
        if not path.endswith('\\'):
            path = path+'\\'

        #開檔處理
        dirlist=os.listdir(path)
        for dir in dirlist:
            nowfile=path+dir+'\Map.xml'
            try:
                with open(nowfile, 'r', encoding='utf-8')as f:
                    data = f.read()
                    data = BeautifulSoup(data, 'xml')
                    f.close()
            except:
                print(f'[ERROR] {nowfile} can not read!')
                break
        
            for tags in data.find_all('gaugeName'):
                tags.name='normalGaugeName'
        
            #寫檔
            with open(nowfile, 'w', encoding='utf-8')as f:
                f.write(str(data))
                f.close()
        
        print('[SUCCESS] All Done!')
                
        


    else:
        print('[ERROR] path is not exist')

if __name__=='__main__':
    map(str(input()))