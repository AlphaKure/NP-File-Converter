# -*- coding : utf-8-*-
#pipreqs . --encoding=utf8 --force

import os

import dev.module as module

def Main(Path:str):
    
    # Make sure the path entered by the user is correct.
    if os.path.isdir(Path):
        if not Path.endswith('\\'):
            Path=Path+'\\'



        #Try to init PreviewTimelist
        module.tool.InitPreviewTimeList()

        # Read the setting and call the transfer program
        if module.tool.ReadSetting('Switch','cue')=='True':
            module.cue.Cue(Path+'cueFile')
        if module.tool.ReadSetting('Switch','chara')=='True':
            module.chara.Chara(Path+'chara')
        if module.tool.ReadSetting('Switch','event')=='True':
            module.event.Event(Path+'event')
        if module.tool.ReadSetting('Switch','map')=='True':
            module.map.Map(Path+'map')
        if module.tool.ReadSetting('Switch','music')=='True':
            module.music.Music(Path+'music')
        if module.tool.ReadSetting('Switch','course')=='True':
            module.course.Course(Path+'course')

        print('[INFO]Convert completed')
    else:
        module.ERROR.ErrorReport('root',99)
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
            Main(Command)