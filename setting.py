from dev.module.tool import *

def setting():

    while True:
        print('Your setting:')
        print('deretore:',read_setting('deretore'))
        print('sat:',read_setting('sat'))
        print('critool:',read_setting('critool'))
        print('key:',read_setting('key'))
        print('WorksSort.xml_path:',read_setting('WorksSort.xml_path'))
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
        edit_setting(pick,string)

if __name__=='__main__':
    setting()