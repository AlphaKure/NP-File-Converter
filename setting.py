import ujson

def setting():

    while True:
        with open('setting.json','r',encoding='utf-8')as f:
            database=ujson.load(f)
            f.close()
        print('Your setting:')
        print('deretore:',database['deretore'])
        print('sat:',database['sat'])
        print('critool:',database['critool'])
        print('key:',database['key'])
        print('WorksSort.xml_path:',database['WorksSort.xml_path'])
        print('What do you want to setting?')
        print('[0]deretore:You need to point to hcaenc.exe in deretore.')
        print('[1]sat:You need to point to AcbEditor.exe in Sonic Audio Tools.')
        print('[2]critool:You need to point to index.js in critool.')
        print('[3]key:You need to set acb key(17 digits decimal).')
        print('[4]WorksSort.xml_path:You need to point to WorkSort.xml.')
        print('[5]Exit')
        num=int(input('Enter the number:'))
        if num==0:
            pick='deretore'
        elif num==1:
            pick='sat'
        elif num==2:
            pick='critools'
        elif num==3:
            pick='key'
        elif num==4:
            pick='WorksSort.xml_path'
        elif num==5:
            return    
        string=str(input('Setting Value:'))
        database[pick]=string
        with open('setting.json','w',encoding='utf-8')as f:
            ujson.dump(database,f)
            f.close()

if __name__=='__main__':
    setting()