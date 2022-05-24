from bs4 import BeautifulSoup
import os 

try:
    import ERROR
    import tool
except ModuleNotFoundError:
    import dev.module.ERROR as ERROR
    import dev.module.tool as tool


def event(path:str):
    '''
    path=Path to event folder
    '''
    #檢查路徑
    if os.path.isdir(path):
        if not path.endswith('\\'):
            path = path+'\\'

        #開檔處理
        dirlist=os.listdir(path)
        for dir in dirlist:
            nowfile=path+dir+'\Event.xml'
            print(f'[INFO] Now reading {nowfile}')    
            try:
                with open(nowfile, 'r', encoding='utf-8')as f:
                    data = f.read()
                    data = BeautifulSoup(data, 'xml')
                    f.close()
            except:
                ERROR.ERRORReport(nowfile,4)
                return
        
            if data.alwaysOpen.string=='false':
                data.alwaysOpen.string='true'
                print(f'[SUCCESS] {nowfile} always open!')



            #寫檔
            with open(nowfile, 'w', encoding='utf-8')as f:
                f.write(str(data))
                f.close()

            tool.XMLFormat(nowfile)
            print(f'[INFO] {nowfile} Convert success')        
        
        print('[SUCCESS] Event convert all done!')
                
        


    else:
        ERROR.ERRORReport('event',99)
        return

if __name__=='__main__':
    event(str(input()))