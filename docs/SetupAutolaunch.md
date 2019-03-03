# How to setup script autolaunch

Start from home base directory
```
nano launcher.sh
```

Then type
```
#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/instagramcounter
sudo python3 main.py
cd /
```

Cntl-X, Return to save.

# Make It Executable

We need to make the launcher script an executable, which we do with this command
```
chmod 755 launcher.sh
```
Now test it, by typing in:
```
sh launcher.sh
```
This should run your Python code.

# Add Logs Directory

Navigate back to your home directory:
```
cd
```
Create a logs directory:
```
mkdir logs
```

# 4: Add to Your Crontab

Type in:
```
sudo crontab -e
```
This will brings up a crontab window.

Now, enter the line:
```
@reboot sh /home/pi/instagramcounter/launcher.sh >/home/pi/logs/cronlog 2>&1
```

# 5: Reboot and See If It Works

Unplug the power or just type in:
```
sudo reboot
```
Wait for startup and see if your script automatically launches.

If it doesn't work, check out the log file:
```
cd logs
cat cronlog
```
This will show you any errors that you might have.
