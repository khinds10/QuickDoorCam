# QuickDoorCam
Quick Security Cam for RPi

Download "RASPBIAN JESSIE LITE" https://www.raspberrypi.org/downloads/raspbian/

Create your new hard disk for DashboardPI

Insert the microSD to your computer via USB adapter and create the disk image using the dd command

Locate your inserted microSD card via the df -h command, unmount it and create the disk image with the disk copy dd command

$ df -h /dev/sdb1 7.4G 32K 7.4G 1% /media/XXX/1234-5678

$ umount /dev/sdb1

Caution: be sure the command is completely accurate, you can damage other disks with this command

if=location of RASPBIAN JESSIE LITE image file of=location of your microSD card

$ sudo dd bs=4M if=/path/to/raspbian-jessie-lite.img of=/dev/sdb (note: in this case, it's /dev/sdb, /dev/sdb1 was an existing factory partition on the microSD)

Setting up your RaspberriPi

Insert your new microSD card to the raspberrypi and power it on with a monitor connected to the HDMI port

Login

user: pi pass: raspberry

Change your account password for security

sudo passwd pi

Enable RaspberriPi Advanced Options

sudo raspi-config

Choose: 1 Expand File System

9 Advanced Options

A2 Hostname change it to "DOORCAM"

A4 SSH Enable SSH Server

A7 I2C Enable i2c interface

Enable the English/US Keyboard

sudo nano /etc/default/keyboard

Change the following line: XKBLAYOUT="us"

Reboot PI for Keyboard layout changes / file system resizing to take effect

$ sudo shutdown -r now

Auto-Connect to your WiFi

sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

Add the following lines to have your raspberrypi automatically connect to your home WiFi (if your wireless network is named "linksys" for example, in the following example)

network={
   ssid="linksys"
   psk="WIRELESS PASSWORD HERE"
}
Reboot PI to connect to WiFi network

$ sudo shutdown -r now

Now that your PI is finally on the local network, you can login remotely to it via SSH. But first you need to get the IP address it currently has.

$ ifconfig Look for "inet addr: 192.168.XXX.XXX" in the following command's output for your PI's IP Address

Go to another machine and login to your raspberrypi via ssh

$ ssh pi@192.168.XXX.XXX

Start Installing required packages

$ sudo apt-get update

$ sudo apt-get upgrade

$ sudo apt-get install vim git python-requests python-smbus i2c-tools python-imaging python-smbus build-essential python-dev rpi.gpio python3 python3-pip libi2c-dev

Update local timezone settings

$ sudo dpkg-reconfigure tzdata

select your timezone using the interface

Setup the simple directory l command [optional]

$ vi ~/.bashrc

add the following line:

$ alias l='ls -lh'

$ source ~/.bashrc

Fix VIM default syntax highlighting [optional]

$ sudo vi /etc/vim/vimrc

uncomment the following line:

syntax on

Install Motion Webcam Utility

$ sudo apt install motion

Edit config to output JPGs for upload

$ sudo vi /etc/motion/motion.conf
    output_pictures on
    ffmpeg_output_movies off

$ sudo service motion restart

Create a symlink in the home folder

$ cd ~

$ ln -s /var/lib/motion

Clone Webcam repository

$ cd ~

$ git clone https://github.com/khinds10/QuickDoorCam.git

$ pip3 install pysftp

Edit Crontab to upload each minute the latest motion image

# m h  dom mon dow   command
* * * * * python3 /home/pi/QuickDoorCam/upload.py

Supplies Needed

RaspberriPi Zero

Pi Zero

Build and wire the device

1) Print the Project Enclosure

    Using a 3D printer print the enclosure files included in the 'enclosure/' folder. .x3g files are MakerBot compatible. You can also use the .stl and .blend (Blender Program) files to edit and create your own improvements to the design.

3) TODO

4) TODO

Configure Application to run correctly in settings.py config file
Find the file settings.py and adjust to your current settings

Setup Startup Scripts
$ crontab -e

Verify the display starts working on reboot

$ sudo reboot

