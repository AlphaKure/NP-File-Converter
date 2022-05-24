# -*- coding : utf-8-*-
#pipreqs . --encoding=utf8 --force

import os

import dev.module as module

def main(Path:str):
    
    # Make sure the path entered by the user is correct.
    if os.path.isdir(Path):
        if not Path.endswith('\\'):
            Path=Path+'\\'



        #Try to init PreviewTimelist
        module.tool.InitPreviewTimeList()

        # Read the setting and call the transfer program
        if module.tool.read_setting('Switch','cue')=='True':
            module.cue.cue(Path+'cueFile')
        if module.tool.read_setting('Switch','chara')=='True':
            module.chara.chara(Path+'chara')
        if module.tool.read_setting('Switch','event')=='True':
            module.event.event(Path+'event')
        if module.tool.read_setting('Switch','map')=='True':
            module.map.map(Path+'map')
        if module.tool.read_setting('Switch','music')=='True':
            module.music.music(Path+'music')
        if module.tool.read_setting('Switch','course')=='True':
            module.course.course(Path+'course')

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
        Command=str(input('Command:'))
        if Command.lower()=='exit':
            os.system('PAUSE')
            break
        else:
            main(Command)