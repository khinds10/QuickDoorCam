# QuickDoorCam
Quick Security Cam for RPi

Download "RASPBIAN JESSIE LITE"
https://www.raspberrypi.org/downloads/raspbian/

**Create your new hard disk for DashboardPI**
>Insert the microSD to your computer via USB adapter and create the disk image using the `dd` command
>
> Locate your inserted microSD card via the `df -h` command, unmount it and create the disk image with the disk copy `dd` command
> 
> $ `df -h`
> */dev/sdb1       7.4G   32K  7.4G   1% /media/XXX/1234-5678*
> 
> $ `umount /dev/sdb1`
> 
> **Caution: be sure the command is completely accurate, you can damage other disks with this command**
> 
> *if=location of RASPBIAN JESSIE LITE image file*
> *of=location of your microSD card*
> 
> $ `sudo dd bs=4M if=/path/to/raspbian-jessie-lite.img of=/dev/sdb`
> *(note: in this case, it's /dev/sdb, /dev/sdb1 was an existing factory partition on the microSD)*

**Setting up your RaspberriPi**

*Insert your new microSD card to the raspberrypi and power it on with a monitor connected to the HDMI port*

Login
> user: **pi**
> pass: **raspberry**

Change your account password for security
>`sudo passwd pi`

Enable RaspberriPi Advanced Options
>`sudo raspi-config`

Choose:
`Expand File System`

`Advanced Options`
>`Hostname`
>*change it to "DOORCAM"*
>
>`SSH`
>*Enable SSH Server*
>
>`Enable Camera`
>*Enable camera interface*

**Enable the English/US Keyboard**

>`sudo nano /etc/default/keyboard`

> Change the following line:
>`XKBLAYOUT="us"`

**Reboot PI for Keyboard layout changes / file system resizing to take effect**
>$ `sudo shutdown -r now`

**Auto-Connect to your WiFi**

>`sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`

Add the following lines to have your raspberrypi automatically connect to your home WiFi
*(if your wireless network is named "linksys" for example, in the following example)*
>
>	network={
>	   ssid="linksys"
>	   psk="WIRELESS PASSWORD HERE"
>	}

**Reboot PI to connect to WiFi network**

>$ `sudo shutdown -r now`
>
>Now that your PI is finally on the local network, you can login remotely to it via SSH.
>But first you need to get the IP address it currently has.
>
>$ `ifconfig`
>*Look for "inet addr: 192.168.XXX.XXX" in the following command's output for your PI's IP Address*

**Go to another machine and login to your raspberrypi via ssh**

> $ `ssh pi@192.168.XXX.XXX`

**Start Installing required packages**

>$ `sudo apt-get update`
>
>$ `sudo apt-get upgrade`
>
>$ `sudo apt-get install sshpass vim rpi.gpio python-smbus python-requests python-picamera python-opencv python-imaging python-dev python3-pip python3 libi2c-dev i2c-tools git build-essential`

**Update local timezone settings**

>$ `sudo dpkg-reconfigure tzdata`

> select your timezone using the interface

**Setup the simple directory `l` command [optional]**

>$ `vi ~/.bashrc`
>
>*add the following line:*
>
>$ `alias l='ls -lh'`
>
>$ `source ~/.bashrc`

**Fix VIM default syntax highlighting [optional]**

>$ `sudo vi /etc/vim/vimrc`
>
>uncomment the following line:
>
>_syntax on_

>$ cd ~
>
>$ git clone https://github.com/khinds10/QuickDoorCam.git
>
>$ pip3 install pysftp

**Edit Crontab to upload each minute the latest motion image**
>
>`# m h  dom mon dow   command`
>
>`* * * * * python /home/pi/QuickDoorCam/webcam.py`

**Supplies Needed**

**RaspberriPi Zero (W Model w/ built in wireless)**
![PiZero W](https://raw.githubusercontent.com/khinds10/QuickDoorCam/master/construction/pizero.jpg "PiZero W")

**Webcam (fisheye FOV lens)**
![Fisheye](https://raw.githubusercontent.com/khinds10/QuickDoorCam/master/construction/fisheye.jpg "Fisheye")

**LED**
![LED](https://raw.githubusercontent.com/khinds10/QuickDoorCam/master/construction/led.jpg "LED")

**Build and wire the device**

1) Print the Project Enclosure

    Using a 3D printer print the enclosure files included in the 'enclosure/' folder. .x3g files are MakerBot compatible. You can also use the .stl and .blend (Blender Program) files to edit and create your own improvements to the design.

2) Solder an appropriate resister and LED to the +3v and GND leads of the PI

![LED](https://raw.githubusercontent.com/khinds10/QuickDoorCam/master/construction/led1.jpg "LED")

![LED2](https://raw.githubusercontent.com/khinds10/QuickDoorCam/master/construction/led2.jpg "LED2")

3) Get the webcam and the LED and the RPI ready to mount in the case

![Wiring](https://raw.githubusercontent.com/khinds10/QuickDoorCam/master/construction/wiring.jpg "Wiring")

4) Mount the Camera throught the front hole

![Mount](https://raw.githubusercontent.com/khinds10/QuickDoorCam/master/construction/mount-camera.jpg "Mount")


5) Install the LED through the small hole in the corner and place the RPI Zero and wiring inside the case

![Inside](https://raw.githubusercontent.com/khinds10/QuickDoorCam/master/construction/inside.jpg "Inside")

![Inside2](https://raw.githubusercontent.com/khinds10/QuickDoorCam/master/construction/inside2.jpg "Inside2")

6) Configure Application to run correctly in settings.py config file

Find the file settings.py-example and adjust to your current settings

Enter your SFTP server and api.forecast.io credentials to get the weather subtitles working and the images uploaded to be viewed on the web.

### FINISHED!

![Inside2](https://raw.githubusercontent.com/khinds10/QuickDoorCam/master/construction/finished.jpg "Finished")

>$ `crontab -e`
>`* * * * * python /home/pi/QuickDoorCam/webcam.py`
>`* * * * * find /home/pi/images -name "*.jpg" -type f -mtime +30 -delete`

![Camera Shot](https://raw.githubusercontent.com/khinds10/QuickDoorCam/master/construction/back-door.jpg "Camera Shot")
