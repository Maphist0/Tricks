## Latex
1. How to setup environment for [SJTU Thesis Latex template](https://github.com/sjtug/SJTUThesis)
    1. Install Visual Studio Code.
    1. Install LaTex Workshop plugin.
    1. Install CTex.
    1. Update latexmk. Download from [here](http://personal.psu.edu/~jcc8/software/latexmk/) 
    (click ```Latexmk``` at the beginning of the first line). 
    Backup the original ```latexmk.pl``` file inside ```C:\Program Files\CTEX\MiKTeX\scripts\latexmk\perl```, 
    or ```C:\CTEX\MiKTeX\scripts\latexmk\perl``` depending on your settings.
    Copy the new Perl file ```latexmk-455\latexmk\latexmk.pl``` to the previous directory.
    1. If you encounter an error: ```pdflatex.exe:The memory dump file could be found.```, 
    check [here](http://bbs.ctex.org/forum.php?mod=viewthread&tid=79936).
    1. Download ```newtxmath.sty```, ```newtxtext.sty``` from [here](https://ctan.org/pkg/newtx?lang=en), 
    and ```sourcecodepro.sty``` from [here](https://ctan.org/pkg/sourcecodepro?lang=en).
    Put them in the main directory of project.
    1. Download and install all fonts [here](https://github.com/silkeh/latex-sourcecodepro/tree/master/fonts/opentype/adobe/sourcecodepro)
    1. Download ```gb7714-2015.bbx``` and ```gb7714-2015.cbx``` from [here](https://github.com/hushidong/biblatex-gb7714-2015) 
    and put in the main directory of project.
    1. Still working on it ......
    
1. Error ```MSVCR100.dll is missing``` and ```MSVCP100.dll is missing``` while opening TexStudio. Install VC++ 2010 from [here](https://social.technet.microsoft.com/Forums/windows/en-US/52f0bd37-9a08-41b6-bb43-fa01ef3ebc4a/msvcr100dll-is-missing?forum=w8itprogeneral)

## Windows
### Powershell
1. Change the execution policy to allow a rc file being loaded in each new shell (like ```~/.bashrc``` in *nix system).\
Call:
```PS C:\Users\user> Set-ExecutionPolicy -Scope CurrentUser```
and enter ```REMOTESIGNED``` in the prompt. \
More info [here](https://technet.microsoft.com/zh-CN/library/hh847748.aspx)
1. [Setup path](https://stackoverflow.com/questions/714877)
1. Enable [```which```](https://stackoverflow.com/questions/63805#65148)
