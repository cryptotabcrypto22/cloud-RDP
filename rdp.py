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
os.sytem(cmd)
cmd = 'sudo apt install --assume-yes task-xfce-desktop'
os.sytem(cmd)
cmd = 'sudo apt install obs-studio'
os.sytem(cmd)
print("link https://remotedesktop.google.com/access")
