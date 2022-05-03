def ERRORReport(where:str,code:int): 

    if code==1:
        print(f'[ERROR] {where}:Skill.json read failure!')
    
    elif code==2:
        print(f'[ERROR] {where}:You have not setting the path of Worksort.xml ')
        print(f'[Tips] Please check setting.ini ')
        print(f'[Tips] ex: WorksSort.xml_path=D:/Desktop/WorksSort.xml ')
    
    elif code==3:
        print(f'[ERROR] {where}:Worksort.xml read failure!')

    elif code==4:
        print(f'[ERROR] {where} read failure!')
    
    elif code==5:
        print(f'[ERROR] {where}:You have not setting the path of deretore')
        print(f'[Tips] Please check setting.ini ')
        print(f'[Tips] ex: deretore=D:/DeskTop/deretore/hcaenc.exe ')
    
    elif code==6:
        print(f'[ERROR] {where}:Your deretore is not pointing to hcaenc.exe, please check again ')
        print(f'[Tips] Please check setting.ini ')
        print(f'[Tips] ex: deretore=D:/DeskTop/deretore/hcaenc.exe ')

    elif code==7:
        print(f'[ERROR] {where}:You have not setting the path of Critool')
        print(f'[Tips] Please check setting.ini ')
        print(f'[Tips] ex: critool=D:/DeskTop/CriTools-master/src/index.js ')
    
    elif code==8:
        print(f'[ERROR] {where}:Your Critool is not pointing to index.js, please check again ')
        print(f'[Tips] Please check setting.ini ')
        print(f'[Tips] ex: critool=D:/DeskTop/CriTools-master/src/index.js ')

    elif code==9:
        print(f'[ERROR] {where}:You have not setting the key')
        print(f'[Tips] Please check setting.ini ')
        print(f'[Tips] ex: key=00000000000000000 ')

    elif code==10:
        print(f'[ERROR] {where}:You have not setting the path of Sonic Audio Tools')
        print(f'[Tips] Please check setting.ini ')
        print(f'[Tips] ex: sat=D:/DeskTop/sat/AcbEditor.exe ')
    
    elif code==11:
        print(f'[ERROR] {where}:Your sat is not pointing to AcbEditor.exe, please check again ')
        print(f'[Tips] Please check setting.ini ')
        print(f'[Tips] ex: sat=D:/DeskTop/sat/AcbEditor.exe ')

    elif code==99:
        print(f'[INFO] {where} folder is not exist')