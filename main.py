# -*- coding : utf-8-*-
#pipreqs . --encoding=utf8 --force

import os

import dev.module as module

def main(path:str):

    if os.path.isdir(path):
        if not path.endswith('\\'):
            path=path+'\\'
        if module.tool.read_setting('Switch','cue')=='True':
            module.cue.cue(path+'cueFile')
        if module.tool.read_setting('Switch','chara')=='True':
            module.chara.chara(path+'chara')
        if module.tool.read_setting('Switch','event')=='True':
            module.event.event(path+'event')
        if module.tool.read_setting('Switch','map')=='True':
            module.map.map(path+'map')
        if module.tool.read_setting('Switch','music')=='True':
            module.music.music(path+'music')
        if module.tool.read_setting('Switch','course')=='True':
            module.course.course(path+'course')
        print('[INFO]Convert completed')
    else:
        module.ERROR.ERRORReport('root',99)
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