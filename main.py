import os

from dev.module.tool import *
from dev.module.chara import *
from dev.module.course import *
from dev.module.cue import *
from dev.module.ERROR import *
from dev.module.event import *
from dev.module.map import *
from dev.module.music import *

def main(path:str):

    if os.path.isdir(path):
        if not path.endswith('\\'):
            path=path+'\\'
        if read_setting('Switch','cue')=='True':
            cue(path+'cueFile')
        if read_setting('Switch','chara')=='True':
            chara(path+'chara')
        if read_setting('Switch','event')=='True':
            event(path+'event')
        if read_setting('Switch','map')=='True':
            map(path+'map')
        if read_setting('Switch','music')=='True':
            music(path+'music')
        if read_setting('Switch','course')=='True':
            course(path+'course')
        print('[INFO]Convert completed')
    else:
        ERRORReport('root',99)
        return

if __name__=='__main__':
    while True:
        print('\nWelcome to use NP File converter:')
        print('Please enter the root path of the option folder to be converted:')
        print('Ex: D:\Desktop\A999')
        print('Or enter \'exit\' to exit.')
        cmd=str(input('Command:'))
        if cmd.lower()=='exit':
            os.system('PAUSE')
            break
        else:
            main(cmd)