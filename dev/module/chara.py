import os
from bs4 import BeautifulSoup
import ujson

try:
    import ERROR
    import tool
except ModuleNotFoundError:
    import dev.module.ERROR as ERROR
    import dev.module.tool as tool



def chara(Path: str):
    # The main function of the program is to convert the new version of Chara.xml to the old compatible version.
    # Path:Path to chara folder

    # Read SKill.json
    try:
        with open('dev/data/Skill.json', 'r', encoding='utf-8')as File:
            DataBase = ujson.load(File)
            File.close()
    except:
        ERROR.ERRORReport('chara', 1)
        return

    # Get WorkSort.xml Path at setting
    WorkSortFilePath = tool.read_setting('ToolPath', 'WorksSort.xml_path')
    DefaultHave = tool.read_setting('Detail', 'chara_defaultHave')
    if WorkSortFilePath == '':
        ERROR.ERRORReport('chara', 2)
        return

    # Read WorkSort.xml
    try:
        with open(WorkSortFilePath, 'r', encoding='utf-8')as File:
            WorkSortData = File.read()
            WorkSortData = BeautifulSoup(WorkSortData, 'xml')
            File.close()
    except:
        ERROR.ERRORReport('chara', 3)
        return

    # Check Path 
    if os.path.isdir(Path):
        if not Path.endswith('\\'):
            Path = Path+'\\'

        # Get Path file list
        for Dir in os.listdir(Path):
            if not os.path.isdir(Path+Dir):
                break
            else:
                NowFile = Path+Dir+'\Chara.xml'
                print(f'[INFO] Now reading {NowFile}')
                try:
                    with open(NowFile, 'r', encoding='utf-8')as File:
                        Data = File.read()
                        Data = BeautifulSoup(Data, 'xml')
                        File.close()
                except:
                    ERROR.ERRORReport(NowFile, 4)
                    return
                
                # Read ranks tag
                ranks = Data.find('ranks')
                for CharaRankData in ranks.find_all('CharaRankData'):
                    SkillID = -1
                    # Remove unwanted tags
                    if not CharaRankData.find('type').string == '1' or CharaRankData.find('index').string == '1':
                        CharaRankData.decompose()
                    else:
                        # Modify the tag name
                        try:
                            for rewardSkillSeed in CharaRankData.find_all('rewardSkillSeed'):
                                rewardSkillSeed.name = 'skill'
                        except:
                            pass

                        # Read the skill name and change it
                        SkillName = CharaRankData.skill.skill.str.string
                        if SkillName.endswith('×5'):
                            SkillName = SkillName.replace('×5', '')
                        elif SkillName.endswith('×1'):
                            SkillName = SkillName.replace('×1', '')
                        if SkillName == 'Invalid':
                            SkillID = -1
                        else:
                            SkillFindFlag = False
                            for Item in DataBase:
                                if SkillName == Item['name']:
                                    SkillID = Item['id']
                                    SkillFindFlag = True
                                    break
                            if not SkillFindFlag:
                                SkillName = 'Invalid'
                                SkillID = '-1'
                        CharaRankData.skill.skill.id.string = SkillID
                        CharaRankData.skill.skill.str.string = SkillName

                # Modify defaultHave
                if DefaultHave == 'True':
                    Data.defaultHave.string = 'True'

                # Add tag firstskill
                if not Data.find('firstSkill'):
                    CharaSkill = Data.find('skill').str.string
                    if CharaSkill == 'Invalid':
                        CharaSkill = 'スキルなし'
                        CharaSkillID = '0'
                    else:
                        CharaSkillID = Data.find('skill').id.string
                    FirstSkillTag = BeautifulSoup(
                        '<firstSkill><id>'+CharaSkillID+'</id><str>'+CharaSkill+'</str><data /></firstSkill>', 'xml')
                    Data.CharaData.defaultHave.insert_after(FirstSkillTag)

                # Get Works data
                WorkID = Data.works.id.string
                WorkStr = Data.works.str.string
                IsFind = False

                # Read WorkSort.xml and find the same ID and Name
                for StringID in WorkSortData.find_all('StringID'):
                    if StringID.id.string == WorkID and StringID.str.string == WorkStr:
                        IsFind = True
                        break
                    elif StringID.str.string == WorkStr and StringID.id.string != WorkID:
                        Data.works.id.string = StringID.id.string
                        break
                    else:
                        continue
                
                # If not found, add a new tag and write it to WorkSort.xml
                if not IsFind:
                    tag = BeautifulSoup(
                        '<StringID><id>'+WorkID+'</id><str>'+WorkStr+'</str><data /></StringID>', 'xml')
                    WorkSortData.SortList.append(tag)
                    with open(WorkSortFilePath, 'w', encoding='utf-8')as File:
                        File.write(str(WorkSortData))
                        File.close()

                # Save modified file
                with open(NowFile, 'w', encoding='utf-8')as File:
                    File.write(str(Data))
                    File.close()
                tool.xmlformat(NowFile)

                print(f'[INFO] {NowFile} Converter success!')

                ''' 
                #debug
                print(data)
                os.system('PAUSE')
                '''

        print('[SUCCESS] chara convert all done!')
    else:
        ERROR.ERRORReport('chara', 99)
        return


if __name__ == '__main__':
    chara(str(input()))
