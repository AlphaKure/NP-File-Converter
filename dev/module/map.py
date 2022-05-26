from bs4 import BeautifulSoup
import os
import ujson

try:
    import ERROR
    import tool
except ModuleNotFoundError:
    import dev.module.ERROR as ERROR
    import dev.module.tool as tool


def GaugeSet(GaugeCount: int):
    '''
    gauge:gauge level
    cgauge:1、2、2、3、3、4、4、5、5、6、6...
    '''
    if GaugeCount == 0:
        return 0
    elif GaugeCount > 0 and GaugeCount < 3:
        return 1
    elif GaugeCount >= 3 and GaugeCount < 5:
        return 2
    elif GaugeCount >= 5 and GaugeCount < 7:
        return 3
    elif GaugeCount >= 7 and GaugeCount < 9:
        return 4
    elif GaugeCount >= 9:
        return 5


def Map(Path: str):
    '''
    path=Path to map folder
    '''
    GaugeCount = 0

    # 開啟cgauge
    with open('dev/data/cgauge.json', 'r', encoding='utf-8')as File:
        GaugeData = ujson.load(File)
        File.close()

    # 檢查路徑
    if os.path.isdir(Path):
        if not Path.endswith('\\'):
            Path = Path+'\\'

        # 開檔處理
        for Dir in os.listdir(Path):
            NowFile = Path+Dir+'\Map.xml'
            print(f'[INFO] Now reading {NowFile}')
            try:
                with open(NowFile, 'r', encoding='utf-8')as File:
                    Data = File.read()
                    Data = BeautifulSoup(Data, 'xml')
                    File.close()
            except:
                ERROR.ErrorReport(NowFile, 4)
                return

            # 修改分類
            OriFilter = Data.find('mapFilterID').str.string
            if OriFilter == 'Current':
                NewFiltersID = '0'
                NewFilterStr = 'Current'
                NewFilterData = '現行バージョン'
            elif OriFilter == 'Collaboration':
                NewFiltersID = '1'
                NewFilterStr = 'Collaboration'
                NewFilterData = 'コラボ系'
            elif OriFilter == 'Sega':
                NewFiltersID = '2'
                NewFilterStr = 'Sega'
                NewFilterData = '自社'
            elif OriFilter == 'Other':
                NewFiltersID = '3'
                NewFilterStr = 'Other'
                NewFilterData = 'その他'
            Data.mapFilterID.id.string = NewFiltersID
            Data.mapFilterID.str.string = NewFilterStr
            Data.mapFilterID.data.string = NewFilterData
            # 修改標籤名稱
            for Tags in Data.find_all('gaugeName'):
                Tags.name = 'normalGaugeName'

            NewGaugeType = 0
            # 課題
            for MapData in Data.find_all('MapDataAreaInfo'):
                if MapData.musicName.id.string != '-1':
                    if not MapData.find('challengeGaugeName'):
                        NewGaugeType = GaugeSet(GaugeCount)
                        NewTag = BeautifulSoup(
                            '<challengeGaugeName><id>'+GaugeData[NewGaugeType]['id']+'</id><str>'+GaugeData[NewGaugeType]['id']+'</str><data /></challengeGaugeName>', 'xml')
                        MapData.append(NewTag)
                        GaugeCount += 1

            # 寫檔
            with open(NowFile, 'w', encoding='utf-8')as File:
                File.write(str(Data))
                File.close()
            tool.XMLFormat(NowFile)

            print(f'[INFO] {NowFile} Convert success')

        print('[SUCCESS] Map convert all done!')

    else:
        ERROR.ErrorReport('map', 99)
        return


if __name__ == '__main__':
    Map(str(input()))
