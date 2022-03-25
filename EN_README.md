# NP-File-Converter

## Menu

<li><a href="#Tools_used">Tools used</a></li>
<li><a href="#Usage">Usage</a></li>

## Tools_used

<li><a href="https://github.com/kohos/CriTools">CriTools</a></li>
<li><a href="https://github.com/OpenCGSS/DereTore">deretore</a></li>
<li><a href="https://github.com/blueskythlikesclouds/SonicAudioTools">SonicAudioTools</a></li>
<li>python using os, shutil, beautifulsoup, ujson, lxml modules.</li>

## Usage

### 

<p> 

&emsp; Please refer to <a href="#Tool_used">Tool used</a>. This program must use deretore, Cri-Tools, Sonic Audio Tools for decryption of acb and packaging in addition to python.

Also need to prepare the game hca key. Decimal system. Not provided here.

</p>

### Step 1: Setup


<p>
	
&emsp; Please go to setting.json file first to set the required external program path. You can use setting.py to help modify it.

&emsp;&emsp; deretore:Please enter the path of hca.exe in deretore.

&emsp;&emsp; sat:Please enter the path of AcbEditor.exe in Sonic Audio Tool.

&emsp;&emsp; key:hca key. decimal system. 

&emsp;&emsp; WorksSort.xml_path:chara classification requires WorksSort.xml. **Very important!!!** You can take it from A000.( we recommend using the P version.) Please enter the path of WorksSort.xml.

&emsp; Other custom function switches can be changed first or in index.py. Details will be given in step 2.

</p>
<br />
<p>
&emsp; Example of setting.json:

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
    "course":"True",
    "chara_defaultHave":"False",
    "music_fix_firstLock":"True",
    "music_fix_disableFlag":"True"
}

```
</p>

### Step 2: Getting Started

<p>
&emsp; Please make sure that lxml, beautifulsoup, and ujson modules are installed first.

&emsp; Run main.py.
	
```cmd	
python -u "d:\DeskTop\NP-File-Converter\main.py"
```
	
&emsp; If you want to convert directly. You can enter the location of the option folder to be converted. e.g. :

&emsp;&emsp; D:\Desktop\A999
	
&emsp; If you do not want to perform certain conversions. You can enter "setting" to adjust the settings and change the items you do not want or want to perform.

</p>
