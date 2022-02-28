import os

from dev.module.tool import *
from dev.module.chara import *
from dev.module.cue import *
from dev.module.ERROR import *
from dev.module.event import *
from dev.module.map import *
from dev.module.music import *

def setting():
    while True:
        print('Enter the number to modify it.\n True=On False=Off')
        print('[0]cueFile:',read_setting('cue'))
        print('[1]chara:',read_setting('chara'))
        print('[2]event:',read_setting('event'))
        print('[3]map:',read_setting('map'))
        print('[4]music:',read_setting('music'))
        print('[5]Chara all defaultHave:',read_setting('chara_defaultHave'))
        print('[6]Fix music firstLock:',read_setting('music_fix_firstLock'))
        print('[7]Fix music disableflag:',read_setting('music_fix_disableFlag'))
        print('[8]Exit')
        pick=int(str(input('Command:')))
        if pick==8:
            break
        elif pick==0:
            key='cue'
        elif pick==1:
            key='chara'
        elif pick==2:
            key='event'
        elif pick==3:
            key='map'
        elif pick==4:
            key='music'
        elif pick==5:
            key='chara_defaultHave'
        elif pick==6:
            key='music_fix_firstLock'
        elif pick==7:
            key='music_fix_disableFlag'
        
        if read_setting(key)=='True':
            if str(input('Are you sure to turn it off?(Y/N):'))=='Y':
                edit_setting(key,'False')
        else:
            if str(input('Are you sure to turn it on?(Y/N):'))=='Y':
                edit_setting(key,'True')
        


def main(path:str):

    
    if os.path.isdir(path):
        if not path.endswith('\\'):
            path=path+'\\'
        if read_setting('cue')=='True':
            cue(path+'cueFile')
        if read_setting('chara')=='True':
            chara(path+'chara')
        if read_setting('event')=='True':
            event(path+'event')
        if read_setting('map')=='True':
            map(path+'map')
        if read_setting('music')=='True':
            music(path+'music')
        print('[INFO]Convert completed')
    else:
        ERRORReport('root',99)
        return

if __name__=='__main__':
    while True:
        print('\nWelcome to use NP File converter:')
        print('Please enter the root path of the option folder to be converted:')
        print('Ex: D:\Desktop\A999')
        print('Or enter \'setting\' to modify the customization options.')
        print('Or enter \'exit\' to exit.')
        cmd=str(input('Command:'))
        if cmd.lower()=='exit':
            os.system('PAUSE')
            break
        elif cmd.lower()=='setting':
            setting()
        else:
            main(cmd)