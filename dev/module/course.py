import os
from bs4 import BeautifulSoup

try:
    import ERROR
    import tool
except ModuleNotFoundError:
    import dev.module.ERROR as ERROR
    import dev.module.tool as tool


def Course(Path: str):

    # 檢查路徑
    if os.path.isdir(Path):
        if not Path.endswith('\\'):
            Path = Path+'\\'

        # 開檔處理
        for Dir in os.listdir(Path):

            NowFile = Path+Dir+'\Course.xml'
            try:
                with open(NowFile, 'r', encoding='utf-8')as File:
                    Data = File.read()
                    Data = BeautifulSoup(Data, 'xml')
                    File.close()
            except:
                ERROR.ErrorReport(NowFile, 4)
                return

            # 將tag內資料修改為Para支援的
            for CourseMusicData in Data.find_all('CourseMusicDataInfo'):
                if CourseMusicData.musicDiff.data.string == 'BASIC':
                    CourseMusicData.musicDiff.id.string = '0'
                    CourseMusicData.musicDiff.str.string = 'ID_00'
                elif CourseMusicData.musicDiff.data.string == 'ADVANCE':
                    CourseMusicData.musicDiff.id.string = '1'
                    CourseMusicData.musicDiff.str.string = 'ID_01'
                elif CourseMusicData.musicDiff.data.string == 'EXPERT':
                    CourseMusicData.musicDiff.id.string = '2'
                    CourseMusicData.musicDiff.str.string = 'ID_02'
                elif CourseMusicData.musicDiff.data.string == 'MASTER':
                    CourseMusicData.musicDiff.id.string = '3'
                    CourseMusicData.musicDiff.str.string = 'ID_03'
                elif CourseMusicData.musicDiff.data.string == 'WORLD\'S END':
                    CourseMusicData.musicDiff.id.string = '4'
                    CourseMusicData.musicDiff.str.string = 'ID_04'
                elif CourseMusicData.musicDiff.data.string == 'ULTIMA':
                    CourseMusicData.musicDiff.id.string = '3'
                    CourseMusicData.musicDiff.str.string = 'ID_03'
                    CourseMusicData.musicName.id.string = '5'+CourseMusicData.musicName.id.string

            # print(data)

            with open(NowFile, 'w', encoding='utf-8')as File:
                File.write(str(Data))
                File.close()
            tool.XMLFormat(NowFile)

            print(f'[INFO] {NowFile} Convert success')


if __name__ == '__main__':
    Course(str(input()))
