import os
from bs4 import BeautifulSoup
import ujson

from ERROR import ERRORReport
from tool import read_setting

def chara(path: str):
    '''
    path=Path to chara folder
    '''
    #開啟SKill json
    try:
        with open('dev/data/Skill.json','r',encoding='utf-8')as f:
            database=ujson.load(f)
            f.close()
    except:
        ERRORReport('chara',1)
        return
        
    
    #開啟設定json 獲得WorkSort.xml位置
    p_WorkS=read_setting('WorksSort.xml_path')
    if p_WorkS=='':
        ERRORReport('chara',2)
        return

    #讀取WorkSort.xml
    try:
        with open(p_WorkS,'r',encoding='utf-8')as f:
            work = f.read()
            work = BeautifulSoup(work, 'xml')
            f.close()
    except:
        ERRORReport('chara',3)
        return

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
                print(f'[INFO] Now reading {nowfile}')
                try:
                    with open(nowfile, 'r', encoding='utf-8')as f:
                        data = f.read()
                        data = BeautifulSoup(data, 'xml')
                        f.close()
                except:
                    ERRORReport(nowfile,4)
                    return
                ranks = data.find('ranks')
                for chararank in ranks.find_all('CharaRankData'):
                    skillid=-1

                    #刪除不需要的資料
                    if not chararank.find('type').string=='1' or chararank.find('index').string=='1' :
                        chararank.decompose()
                    else:
                        
                        #修改tag名稱
                        try:
                            for tags in chararank.find_all('rewardSkillSeed'):
                                tags.name='skill'
                        except:
                            pass
                        
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
                if not data.find('firstSkill'):
                    charaskill=data.find('skill').str.string
                    if charaskill=='Invalid':
                        charaskill='スキルなし'
                        charaskillid='0'
                    else:
                        charaskillid=data.find('skill').id.string
                    newtag=BeautifulSoup('<firstSkill><id>'+charaskillid+'</id><str>'+charaskill+'</str><data /></firstSkill>','xml')
                    data.CharaData.defaultHave.insert_after(newtag)

                workid=data.works.id.string
                workstr=data.works.str.string
                isFind=False
                for StringID in work.find_all('StringID'):
                    if StringID.id.string==workid and StringID.str.string==workstr:
                        isFind=True
                        break
                    elif StringID.str.string==workstr and StringID.id.string!=workid:
                        data.works.id.string=StringID.id.string
                        break
                    else:
                        continue
                
                if not isFind:
                    tag=BeautifulSoup('<StringID><id>'+workid+'</id><str>'+workstr+'</str><data /></StringID>','xml')
                    work.SortList.append(tag)
                    with open(p_WorkS,'w',encoding='utf-8')as f:
                        f.write(str(work))
                        f.close()
                #寫檔
                with open(nowfile, 'w', encoding='utf-8')as f:
                    f.write(str(data))
                    f.close()
                print(f'[INFO] {nowfile} Converter success!')
                
                ''' 
                #測試用:
                print(data)
                os.system('PAUSE')
                '''

        print('[SUCCESS] chara convert all done!')
    else:
        ERRORReport('chara',99)
        return
    
    

if __name__ == '__main__':
    chara(str(input()))
