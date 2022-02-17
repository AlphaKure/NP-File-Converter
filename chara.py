import os
from bs4 import BeautifulSoup
import ujson


def chara(path: str):
    #開啟SKill json
    with open('Skill.json','r',encoding='utf-8')as f:
        database=ujson.load(f)
        f.close()

    #檢查路徑
    if os.path.isdir(path):
        if not path.endswith('\\'):
            path = path+'\\'

        #檢查路徑內資料夾
        dirlist = os.listdir(path)
        for dir in dirlist:
            if not os.path.isdir(path+dir):
                break
                
            #開檔處理
            else:
                nowfile = path+dir+'\Chara.xml'
                try:
                    with open(nowfile, 'r', encoding='utf-8')as f:
                        data = f.read()
                        data = BeautifulSoup(data, 'xml')
                        f.close()
                except:
                    print(f'[ERROR] {nowfile} can not read!')
                    break
                ranks = data.find('ranks')
                for chararank in ranks.find_all('CharaRankData'):
                    skillid=-1

                    #刪除不需要的資料
                    if not chararank.find('type').string=='1' or int(chararank.find('index').string)==1 :
                        chararank.decompose()
                    else:

                        #修改tag名稱
                        for tags in chararank.find_all('rewardSkillSeed'):
                            tags.name='skill'
                            
                        #讀取技能名稱並更改
                        skillname=chararank.skill.skill.str.string
                        if skillname.endswith('×5'):
                            skillname=skillname.replace('×5','')
                        elif skillname.endswith('×1'):
                            skillname=skillname.replace('×1','') 
                        if skillname=='Invalid':
                            skillid=-1
                        else:
                            for item in database:
                                if skillname==item['name']:
                                    skillid=item['id']
                                    break
                        chararank.skill.skill.id.string=skillid
                        chararank.skill.skill.str.string=skillname
                            
                #新增標籤 firstskill
                charaskill=data.find('skill').str.string
                charaskillid=data.find('skill').id.string
                newtag=BeautifulSoup('<firstSkill><id>'+charaskillid+'</id><str>'+charaskill+'</str><data /></firstSkill>','xml')
                data.CharaData.defaultHave.insert_after(newtag)

                #寫檔
                with open(nowfile, 'w', encoding='utf-8')as f:
                    f.write(data.prettify())
                    f.close()
                
                '''
                #測試用:
                print(data.prettify())
                os.system('PAUSE')
                '''
        print('[SUCCESS] All Done!')
    else:
        print('[ERROR] path is not exist')


if __name__ == '__main__':
    chara(str(input()))
