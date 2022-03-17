import os
import subprocess

cmd = 'sudo apt update'
os.system(cmd)
cmd = 'sudo apt-get install --assume-yes ./chrome-remote-desktop_current_amd64.deb'
os.system(cmd)
cmd = 'sudo apt install --assume-yes xfce4 desktop-base dbus-x11 xscreensaver'
os.system(cmd)
cmd = 'sudo apt install xfce4-terminal -y'
os.system(cmd)
cmd = 'sudo apt install firefox-esr -y'
os.system(cmd)
cmd = 'sudo apt-get install geany -y'
os.system(cmd)
cmd = 'sudo apt-get install vim-gtk3 -y'
os.system(cmd)
cmd = 'sudo apt install iputils-ping -y'
os.system(cmd)
cmd = 'sudo apt update'
os.sytem(cmd)
cmd = 'sudo apt install obs-studio'
os.sytem(cmd)
cmd = 'sudo add-apt-repository universe'
os.sytem(cmd)
cmd = 'sudo apt install wireshark'
os.sytem(cmd)
cmd = 'sudo add-apt-repository ppa:ubuntuhandbook1/apps'
os.sytem(cmd)
cmd = 'sudo apt install vokoscreen-ng'
print("link https://remotedesktop.google.com/access")
