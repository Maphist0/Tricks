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

### RemoteFX
1. [Win Server 2012 setup guide](https://social.technet.microsoft.com/wiki/contents/articles/16652.remotefx-vgpu-setup-and-configuration-guide-for-windows-server-2012.aspx).
*Recent NVIDIA GPUs might not be supported! (e.g. GTX 1070).*
1. [Win Server 2016 setup guide](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-remotefx-vgpu).
*Before you start: Notice that the vGPU memory is limited to less than 1GB. Some game may fail to start (e.g. FIFA 18).*

## Video Streaming
1. Use OBS on server, [setup RTMP server on client](https://obsproject.com/forum/resources/how-to-set-up-your-own-private-rtmp-server-using-nginx.50/), [use ffplay instead of VLC](https://www.quora.com/How-can-I-stream-a-game-to-a-friend-with-minimal-delay) for low latency.
1. [Connect FFMPEG with Python](http://zulko.github.io/blog/2013/09/27/read-and-write-video-frames-in-python-using-ffmpeg/) so that each frame can be processed on the fly.
1. For ?better? performance, use [librtmp-python](https://pythonhosted.org/python-librtmp/) to get raw RTMP data. 
`>stream.read()` returns the raw FLV data which can be saved directly to a file and play. 
Check [here](http://wwwimages.adobe.com/www.adobe.com/content/dam/acom/en/devnet/rtmp/pdf/rtmp_specification_1.0.pdf) for RTMP specification.
1. Instead of OBS, [use FFMPEG in cmd to push stream](https://github.com/arut/nginx-rtmp-module/issues/378).
Check the [streaming guide](https://trac.ffmpeg.org/wiki/StreamingGuide#Latency).

## Router
1. [Flash NetGear NightHawk R8000 guide](http://avi.im/blag/2015/asus-wrt-merlin-on-netgear-r7000/).
1. [Tomato for R8000](https://www.myopenrouter.com/download/tomato-firmware-shibby-netgear-r8000-initial).
1. [Merlin for R8000](https://sourceforge.net/projects/asuswrt-merlin/files/RT-AC3200/Release/).
