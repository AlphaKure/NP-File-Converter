# NP-File-Converter

<p>某款遊戲的轉檔器</p>

<p>不是轉譜器!!!<p>

## 目錄

<li><a href="#使用到的工具">使用到的工具</a></li>
<li><a href="#尚未完成的功能">尚未完成的功能</a></li>
<li><a href="#使用方法">使用方法</a></li>
<li><a href="#運作原理">運作原理</a></li>
<li><a href="CHANGELOG.md">開發紀錄</a></li>
<li><a href="EN_README.md">English</a>(Not written yet)</li>

## 使用到的工具

<li><a href="https://github.com/kohos/CriTools">CriTools</a></li>
<li><a href="https://github.com/OpenCGSS/DereTore">deretore</a></li>
<li><a href="https://github.com/blueskythlikesclouds/SonicAudioTools">SonicAudioTools</a></li>
<li>python使用os、shutil、beautifulsoup、ujson套件</li>

## 尚未完成的功能

<p>

&emsp;1.整合
	
&emsp;PL轉N ~~等我玩到了再說w~~

</p>

## 使用方法

### 第零步：事先準備

<p> 

&emsp; 請參考<a href="#使用到的工具">使用到的工具</a>，本程式除了python之外，必須使用deretore、Cri-Tools、Sonic Audio Tools進行acb的解密以及打包。

也需要準備好遊戲的acb、awb key，17位十進制，這裡就不方便提供。

</p>

### 第一步：設定


<p>
	
&emsp; 請先至setting.json檔設定需要的外部程式路徑，可使用setting.py協助修改。

&emsp;&emsp; deretore:請指向deretore裡的hca.exe。

&emsp;&emsp; sat:請指向Sonic Audio Tool裡的AcbEditor.exe。 

&emsp;&emsp; key:遊戲的acb、awb key。

&emsp;&emsp; WorksSort.xml_path:chara分類顯示需要，**非常重要**，可以從A000中拿(建議使用P版的)。請指向WorksSort.xml。

&emsp; 其他為自定義功能開關，可以先行更改，亦或是在index.py裡修改，詳細內容將告知於第二步。

</p>
<br />
<p>
&emsp; 以下為範例:

```json
{
    "deretore":"D:/DeskTop/deretore/hcaenc.exe",
    "sat":"D:/DeskTop/sat/AcbEditor.exe",
    "critool":"D:/DeskTop/CriTools-master/src/index.js",
    "key":"00000000000000000",
    "WorksSort.xml_path":"D:/Desktop/WorksSort.xml",
	
    "cue":"True",
    "chara":"True",
    "event":"True",
    "map":"True",
    "music":"True",
    "chara_defaultHave":"False",
    "music_fix_firstLock":"True",
    "music_fix_disableFlag":"True"
}

```
</p>

### 第二步：開始使用

待補..

## 運作原理

待補..
