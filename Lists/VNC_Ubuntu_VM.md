## Tricks for VNC, Ubuntu and VirtualBox

### VNC
1. [Install VNC server on Ubuntu 16.04 server](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-vnc-on-ubuntu-16-04)
1. [Config shared clipboard](https://askubuntu.com/questions/41273#754420)
1. [Solve ```tab``` not working](https://stackoverflow.com/questions/23418831)
1. [Clean up when VNC server crashed](https://ubuntuforums.org/showthread.php?t=821629#4)

### VirtualBox
1. [Install VirtualBox](https://www.virtualbox.org/wiki/Linux_Downloads)
1. [Install guest addon and enable share folder](https://askubuntu.com/questions/456400#456404)
1. [VirtualBox network](https://www.virtualbox.org/manual/ch06.html)
1. [Easier reference for VB network](https://blogs.oracle.com/scoter/networking-in-virtualbox-v2)
1. Install Win10 in VB on Ubuntu, [mount ISO in IDE instead of SATA](https://forums.virtualbox.org/viewtopic.php?f=2&t=77173), and [disable Paravirtualization](https://superuser.com/questions/1208895/virtualbox-stuck-on-windows-logo?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa).

### Ubuntu
1. Synchronize local time:
  - Use ```$ timedatectl``` to check ```NTP synchronized: yes``` or ```NTP synchronized: no```
  - If ```no```, then ```$ sudo apt-get install ntp```, and ```$ sudo timedatectl set-ntp on``` ([reference](https://www.digitalocean.com/community/tutorials/how-to-set-up-time-synchronization-on-ubuntu-16-04))
  - Reboot if necessary
  - Wait several minutes until ```NTP synchronized: yes```, may check the state using ```$ watch -n 0.1 timedatectl```
