import os
from bs4 import BeautifulSoup
import ujson


def chara(path: str):
    if os.path.isdir(path):
        if not path.endswith('\\'):
            path = path+'\\'
        dirlist = os.listdir(path)
        for dir in dirlist:
            if not os.path.isdir(path+dir):
                break
            else:
                nowfile = path+dir+'\Chara.xml'
                with open(nowfile, 'r', encoding='utf-8')as f:
                    data = f.read()
                    data = BeautifulSoup(data, 'lxml')
                    f.close()
                ranks = data.find('ranks')
                for chararank in ranks.find_all('chararankdata'):
                    if not chararank.find('type').string=='1' or int(chararank.find('index').string)==1 :
                        chararank.decompose()
                #print(ranks.prettify())
    else:
        print('[ERROR] path is not exist')


if __name__ == '__main__':
    chara(str(input()))
