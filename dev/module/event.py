from bs4 import BeautifulSoup
import os 

def event(path:str):
    
    #檢查路徑
    if os.path.isdir(path):
        if not path.endswith('\\'):
            path = path+'\\'

        #開檔處理
        dirlist=os.listdir(path)
        for dir in dirlist:
            nowfile=path+dir+'\Event.xml'
            try:
                with open(nowfile, 'r', encoding='utf-8')as f:
                    data = f.read()
                    data = BeautifulSoup(data, 'xml')
                    f.close()
            except:
                print(f'[ERROR] {nowfile} can not read!')
                break
        
            if data.alwaysOpen.string=='false':
                data.alwaysOpen.string='true'
                print(f'[SUCCESS] {nowfile} always open!')



            #寫檔
            with open(nowfile, 'w', encoding='utf-8')as f:
                f.write(str(data))
                f.close()
        
        print('[SUCCESS] All Done!')
                
        


    else:
        print('[ERROR] path is not exist')

if __name__=='__main__':
    event(str(input()))