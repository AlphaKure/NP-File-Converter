import os
from bs4 import BeautifulSoup



def newduel(path:str):
    #檢查路徑
    if not os.path.isdir(path):
        print('[ERROR] path is not exist.')
        return
    else:
        if not (path.endswith('\\')or path.endswith('/')):
            path+='/'
        dirlist=os.listdir(path)
        for dir in dirlist:
            if not os.path.isdir(path+dir):
                continue
            else:
                nowfile=path+dir+'\Duel.xml'
                print(f'[INFO] Now reading {nowfile}')
                try:
                    with open(nowfile, 'r', encoding='utf-8')as f:
                        data = f.read()
                        data = BeautifulSoup(data, 'xml')
                except:
                    print(f'[ERROR] {nowfile} read failure!')
                    os.system('PAUSE')
                    continue

                #刪除多餘tag
                if data.find('resourceVersion'):
                    for resourceVersion in data.find_all('resourceVersion'):
                        resourceVersion.decompose()
                
                if data.find('formatVersion'):
                    for formatVersion in data.find_all('formatVersion'):
                        formatVersion.decompose()
                
                #新增tag
                if not data.find('netOpenName'):#不確定有無影響
                    netOpenName=BeautifulSoup('<netOpenName><id>2000</id><str>v2_00 00_0</str><data /></netOpenName>','xml')
                    data.find('dataName').insert_after(netOpenName)

                with open(nowfile,'w',encoding='utf-8')as f:
                    f.write(str(data))
                    f.close()