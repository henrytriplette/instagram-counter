### 1.44inch LCD HAT from Waveshare

Download Raspbian from
https://www.raspberrypi.org/downloads/raspbian/

Burn with Etcher

On the SD card /boot/ add
- SSH Empty file
- wpa_supplicant.conf file [look in file]

```
sudo apt-get update
sudo apt-get upgrade
```

```
sudo raspi-config
```
enable ‘SPI’ inside ‘Advanced Options’ and then ‘SPI’.
enable ‘SSH’ inside ‘Advanced Options’ and then ‘SSH’.
enable ‘camera’ inside ‘Advanced Options’ and then ‘camera’.

sudo nano /etc/modules
- content of modules file

sudo nano /etc/modprobe.d/fbtft.conf
- content of modules file

sudo apt-get install cmake git
```
cd ~
git clone https://github.com/tasanakorn/rpi-fbcp
cd rpi-fbcp/
mkdir build
cd build/
cmake ..
make
sudo install fbcp /usr/local/bin/fbcp
```

```
cd ~
git clone https://github.com/adafruit/Adafruit-Retrogame
cd Adafruit-Retrogame/
sudo make install
```

sudo nano /etc/udev/rules.d/10-retrogame.rules
- content of 10-retrogame.rules file

sudo nano /etc/rc.local
- content of rc.local file

Remove the SD card.
Place this SD card into the computer and open the ‘boot’ folder
Open config.txt
- At the bottom of the file add:
```
dtoverlay=pwm-2chan,pin=18,func=2,pin2=13,func2=4
hdmi_force_hotplug=1
hdmi_cvt=128 128 60 1 0 0 0
hdmi_group=2
hdmi_mode=1
hdmi_mode=87

display_rotate=2
```

Add file named retrogame.cfg
- content of retrogame.cfg file

More: https://www.sudomod.com/forum/viewtopic.php?f=11&t=5371&start=10
