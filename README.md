# NP-File-Converter

<p>某款遊戲的轉檔器</p>

<p>不是轉譜器!!!<p>

## 目錄

<li><a href="#使用到的工具">使用到的工具</a></li>
<li><a href="#尚未完成的功能">尚未完成的功能</a></li>
<li><a href="#使用方法">使用方法</a></li>
<li><a href="CHANGELOG.md">開發紀錄</a></li>
<li><a href="EN_README.md">English</a></li>

## 使用到的工具

<li><a href="https://github.com/kohos/CriTools">CriTools</a></li>
<li><a href="https://github.com/OpenCGSS/DereTore">deretore</a></li>
<li><a href="https://github.com/blueskythlikesclouds/SonicAudioTools">SonicAudioTools</a></li>
<li>python使用os、shutil、beautifulsoup、ujson、lxml套件</li>

## 尚未完成的功能

<p>

&emsp;設定改用ini

&emsp;程式碼整理

&emsp;翻譯文件及與語言選項

&emsp;cue previewTime數值獲取
</p>

## 使用方法

### 第零步：事先準備

<p> 

&emsp; 請參考<a href="#使用到的工具">使用到的工具</a>，本程式除了python之外，必須使用deretore、Cri-Tools、Sonic Audio Tools進行acb的解密以及打包。

也需要準備好遊戲的hca key，17位十進制，這裡就不方便提供。

</p>

### 第一步：設定


<p>
	
&emsp; 請先至setting.ini檔設定需要的外部程式路徑。

&emsp;&emsp; deretore:請指向deretore裡的hca.exe。

&emsp;&emsp; sat:請指向Sonic Audio Tool裡的AcbEditor.exe。 

&emsp;&emsp; key:遊戲的acb、awb key。

&emsp;&emsp; WorksSort.xml_path:chara分類顯示需要，**非常重要**，可以從A000中拿(建議使用P版的)。請指向WorksSort.xml。

&emsp; 其他為功能開關，若有不需要的功能可在這裡關閉。

</p>
<br />
<p>
&emsp; 以下為範例:

```ini
[ToolPath]
;deretore:You need to point to hcaenc.exe in deretore.
deretore=D:\deretore\hcaenc.exe
;sat:You need to point to AcbEditor.exe in Sonic Audio Tools.
sat=D:/DeskTop/sat/AcbEditor.exe
;critool:You need to point to index.js in critool.
critool=D:\DeskTop\CriTools-master\src\index.js
;key:You need to set acb key(17 digits decimal).
key=00000000000000000
;WorksSort.xml_path:You need to point to WorkSort.xml.
WorksSort.xml_path=D:\Desktop\WorksSort.xml

[Switch]
;True=On False=Off
cue=True
chara=True
event=True
map=True
music=True
course=True

[Detail]
;True=On False=Off
chara_defaultHave=False
music_fix_firstLock=True
music_fix_disableFlag=True
```
</p>

### 第二步：開始使用

<p>
&emsp; 請先確定安裝好lxml、beautifulsoup、ujson套件。

&emsp; 執行main.py。
	
```cmd	
python -u "d:\DeskTop\NP-File-Converter\main.py"
```
	
&emsp; 如果要直接進行轉換，可以直接輸入需要轉換的option資料夾位置，例如:

&emsp;&emsp; D:\Desktop\A999
	
&emsp; 如果不想要進行某些轉換，可以輸入"setting"，即可進入調整設定，把不想要或想要執行的項目進行修改。

</p>

