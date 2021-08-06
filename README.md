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
>$ `sudo apt-get install vim git python-requests python-smbus i2c-tools python-imaging python-smbus build-essential python-dev rpi.gpio python3 python3-pip libi2c-dev`

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

**Install Motion Webcam Utility**

>$ sudo apt install motion

**Edit config to output JPGs for upload**

>$ sudo vi /etc/motion/motion.conf
>    output_pictures on
>    ffmpeg_output_movies off

>$ sudo service motion restart

**Create a symlink in the home folder**
>
>$ cd ~
>
>$ ln -s /var/lib/motion
>

**Clone Webcam repository**

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

**RaspberriPi Zero**

**Pi Zero**

**Build and wire the device**

1) Print the Project Enclosure

    Using a 3D printer print the enclosure files included in the 'enclosure/' folder. .x3g files are MakerBot compatible. You can also use the .stl and .blend (Blender Program) files to edit and create your own improvements to the design.

2) TODO

3) TODO

Configure Application to run correctly in settings.py config file
Find the file settings.py and adjust to your current settings






SORT BELOW:

sudo apt install sshpass


#### Flashing RaspberriPi Hard Disk / Install Required Software (Using Ubuntu Linux)

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
`1 Expand File System`

`6 Enable Camera`

`9 Advanced Options`
>`A2 Hostname`
>*change it to "SunRise"*
>
>`A4 SSH`
>*Enable SSH Server*
>
>`A7 I2C`
>*Enable i2c interface*

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

	network={
	   ssid="linksys"
	   psk="WIRELESS PASSWORD HERE"
	}

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
>$ `sudo apt-get install vim git python-smbus i2c-tools python-pil python-smbus build-essential python-dev rpi.gpio python3 python3-pip libi2c-dev python-picamera python-opencv`

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

**Clone SunRise repository**

`$ cd ~`

`$ https://github.com/khinds10/WakeUpMirror.git`

**Install the SSMTP mail program to gmail your sunrise pictures**

>$ `sudo apt-get update && apt-get install ssmtp`

>$ `sudo apt-get install sharutils`

**Edit the SSMTP config**

>$ `sudo vi /etc/ssmtp/ssmtp.conf`

>comment out: `mailhub=mail`
>comment out: `FromLineOverride=YES`

>Add the following lines to the end of the file
>
>`AuthUser=your-gmail-address@gmail.com`
>`AuthPass=YOUR GMAIL PASSWORD`
>`FromLineOverride=YES`
>`mailhub=smtp.gmail.com:587`
>`UseSTARTTLS=YES`

**Test emailing to yourself using the installed command**
>$ `echo "This is a test" | mail -s "Test" your-gmail-address@gmail.com`

## Supplies Needed

**RaspberriPi Zero (W Model w/ built in wireless)**
![PiZero W](https://raw.githubusercontent.com/khinds10/SunRiseCatcher/master/construction/pizero.jpg "PiZero W")

PI Camera w/picture here

## Print the Project Enclosure

Using a 3D printer print the enclosure files included in the 'enclosure/' folder. .x3g files are MakerBot compatible. You can also use the .stl and .blend (Blender Program) files to edit and create your own improvements to the design.

## Assembly

**Change your settings.py to match your personal preferences**

`settings.py`

> emailAddress = 'your-email@gmail.com'
>
> weatherAPIURL = 'https://api.forecast.io/forecast/'
> weatherAPIKey = 'YOUR FORECAST.IO KEY HERE'
>
> numberOfSunriseCaptures = 15
> timeToCaptureMinutes = 30

> latitude = 42.4152778
> longitude = -71.1569444

**Run Daily at 4am (via crontab)**

Add the following line to your PI crontab to run the capture program starting at 4am

>$ `crontab -e`
>`* * * * * python /home/pi/QuickDoorCam/webcam.py`

### FINISHED!
