# Latex
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
    
