from bs4 import BeautifulSoup
import os

try:
    import ERROR
    import tool
except ModuleNotFoundError:
    import dev.module.ERROR as ERROR
    import dev.module.tool as tool


def Event(Path: str):
    '''
    path=Path to event folder
    '''
    # 檢查路徑
    if os.path.isdir(Path):
        if not Path.endswith('\\'):
            Path = Path+'\\'

        # 開檔處理
        for Dir in os.listdir(Path):
            NowFile = Path+Dir+'\Event.xml'
            print(f'[INFO] Now reading {NowFile}')
            try:
                with open(NowFile, 'r', encoding='utf-8')as File:
                    Data = File.read()
                    Data = BeautifulSoup(Data, 'xml')
                    File.close()
            except:
                ERROR.ErrorReport(NowFile, 4)
                return

            if Data.alwaysOpen.string == 'false':
                Data.alwaysOpen.string = 'true'
                print(f'[SUCCESS] {NowFile} always open!')

            # 寫檔
            with open(NowFile, 'w', encoding='utf-8')as File:
                File.write(str(Data))
                File.close()

            tool.XMLFormat(NowFile)
            print(f'[INFO] {NowFile} Convert success')

        print('[SUCCESS] Event convert all done!')

    else:
        ERROR.ErrorReport('event', 99)
        return


if __name__ == '__main__':
    Event(str(input()))
