


# update the system
```
apt update
apt upgrade
```
# install a few useful packages and setup swap
```
apt install git dphys-swapfile
```

# set CONF_SWAPSIZE to 1024
```
nano /etc/dphys-swapfile
systemctl enable dphys-swapfile
```

# set the correct timezone
```
dpkg-reconfigure tzdata
```

# Install python3
```
sudo apt-get install python3-pip
```

# Fix Pygame: ImportError: libSDL_ttf-2.0.so.0: cannot open shared object file: No such file or directory
```
sudo apt-get install libsdl-ttf2.0-0
```
