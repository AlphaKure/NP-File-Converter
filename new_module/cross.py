
def mapFilter(id:str):
    if id=='-1':
        fid='-1'
        fstr='Invalid'
        fdata=''
    elif id=='0':
        fid='1'
        fstr='Current'
        fdata='現行バージョン'
    elif id=='1':
        fid='0'
        fstr='Collaboration'
        fdata='イベント'
    elif id=='2':
        fid='2'
        fstr='Sega'
        fdata='ゲキチュウマイ'
    elif id=='3':
        fid='3'
        fstr='Other'
        fdata='過去バージョン'
    return fid,fstr,fdata


