## Mi4c-Unbrick
Notes to unbrick my Mi4c.

## Pre-requirement
 - Driver for Qualcomm devices: "QDLoader HS-USB Driver_64bit_Setup.zip" from [here](https://androidfilehost.com/?fid=24459283995295983)
 - Miflash: "MiPhone20151028.exe" from [here](http://en.miui.com/thread-150494-1-1.html)
 - ADB installer: "adb-setup-1.4.3.exe" from [here](https://forum.xda-developers.com/showthread.php?p=48915118#post48915118)
 - Miui 6.1.7: "libra_images_6.1.7_20151221.0000.11_5.1_cn_b09dac70a0.tgz" from [here](https://forum.xda-developers.com/mi-4c/general/guide-unlocking-mi4c-bl-verification-t3336779)
 - TWRP: "libra_ts_twrp_3_0_2_0.img" from [here](http://www.teamsuperluminal.org/download/libra_ts_twrp_3_0_2_0-img/)
 - Win 8/10,  better physical machine instead of VM
 
## Steps
### Prepare
1. Install first three softwares
2. Untar Miui 6.1.7, create a folder (like ```C:\ISO```) and move the content to this folder
2. Run Miflash, click "Browse" and select the folder in previous step
2. Copy "libra_ts_twrp_3_0_2_0" to ```C:\adb```
2. Open "Device Manager" under "Control panel" (search for "device" in windows)
3. Launch cmd, nevigate to ```C:\adb```
4. Reboot Mi4c into fastboot mode (Press "power btn" + "volumn `down`" at the same time)
5. In cmd, type ```fastboot devices``` to check the connection. If failed, consider using another type-c cable

### Important
1. In cmd, type ```fastboot oem edl```, the screen on Mi4c becomes completely black
2. Check submenu in "Device Manager > Ports" to see whether the icon for "Qualcomm ... 9008" device is on (instead of gray icon). If not, the driver has some problems
4. In Miflash, choose "Flash all" on the bottom. Then click "Refresh" and choose the device. Click "Flash" and wait.
5. When it is done, reboot the phone by long-press the power button
6. Setup the phone and reboot again to fastboot mode when you see the desktop
7. In cmd, type ```fastboot flash recovery twrp.img```
8. Reboot to recovery mode when it is done (Press "power btn" + "volumn `up`" at the same time)

### Post-process
1. You may wipe all data including internal storage (Most folders in internal storage are created by Miui 6.1.7)
2. Connect Mi4c to the computer, copy your new OS like [AICP](https://forum.xda-developers.com/mi-4c/development/official-aicp-12-1-nightlies-t3566731) to it, along with [GAPPs](http://opengapps.org/)
3. Install new OS
