def ErrorReport(Where: str, Code: int):

    if Code == 1:
        print(f'[ERROR] {Where}:Skill.json read failure!')

    elif Code == 2:
        print(
            f'[ERROR] {Where}:You have not setting the path of Worksort.xml ')
        print(f'[Tips] Please check setting.ini ')
        print(f'[Tips] ex: WorksSort.xml_path=D:/Desktop/WorksSort.xml ')

    elif Code == 3:
        print(f'[ERROR] {Where}:Worksort.xml read failure!')

    elif Code == 4:
        print(f'[ERROR] {Where} read failure!')

    elif Code == 5:
        print(f'[ERROR] {Where}:You have not setting the path of deretore')
        print(f'[Tips] Please check setting.ini ')
        print(f'[Tips] ex: deretore=D:/DeskTop/deretore/hcaenc.exe ')

    elif Code == 6:
        print(
            f'[ERROR] {Where}:Your deretore is not pointing to hcaenc.exe, please check again ')
        print(f'[Tips] Please check setting.ini ')
        print(f'[Tips] ex: deretore=D:/DeskTop/deretore/hcaenc.exe ')

    elif Code == 7:
        print(f'[ERROR] {Where}:You have not setting the path of Critool')
        print(f'[Tips] Please check setting.ini ')
        print(f'[Tips] ex: critool=D:/DeskTop/CriTools-master/src/index.js ')

    elif Code == 8:
        print(
            f'[ERROR] {Where}:Your Critool is not pointing to index.js, please check again ')
        print(f'[Tips] Please check setting.ini ')
        print(f'[Tips] ex: critool=D:/DeskTop/CriTools-master/src/index.js ')

    elif Code == 9:
        print(f'[ERROR] {Where}:You have not setting the key')
        print(f'[Tips] Please check setting.ini ')
        print(f'[Tips] ex: key=00000000000000000 ')

    elif Code == 10:
        print(
            f'[ERROR] {Where}:You have not setting the path of Sonic Audio Tools')
        print(f'[Tips] Please check setting.ini ')
        print(f'[Tips] ex: sat=D:/DeskTop/sat/AcbEditor.exe ')

    elif Code == 11:
        print(
            f'[ERROR] {Where}:Your sat is not pointing to AcbEditor.exe, please check again ')
        print(f'[Tips] Please check setting.ini ')
        print(f'[Tips] ex: sat=D:/DeskTop/sat/AcbEditor.exe ')

    elif Code == 99:
        print(f'[INFO] {Where} folder is not exist')
