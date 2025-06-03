# Laptop Alert - Email Notification on Startup

## Project Description
This Python project automatically sends an email notification whenever the laptop boots up.  
It helps users to monitor if their laptop has been turned on and at what time.

---

## Features
- Automatically sends email on laptop startup
- Includes timestamp of the boot time in the email
- Uses Gmail SMTP with SSL for secure email sending
- Easy to configure with your email and app password
- When open the laptop automatic an alart email are send.

---

## ✅ Step-by-Step Installation for Linux

### 1. Make Sure Python Works

Check if Python 3 is installed:
which python3

---
### 2nd step: 

Create a new systemd service file:
sudo nano /etc/systemd/system/laptop-notify.service

write this content:
[Unit]
Description=Send email when laptop starts or wakes up
After=network-online.target
Wants=network-online.target
StartLimitIntervalSec=0

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 /home/hasan/Desktop/projects_of_python/open_notify/main.py

[Install]
WantedBy=multi-user.target


Then press ctrl+o, enter, ctrl+x

---

### 3rd step: 

Create a system sleep hook that triggers after waking from sleep:
sudo nano /lib/systemd/system-sleep/laptop-wake.sh

Write this content:
#!/bin/bash
if [ "$1" = "post" ]; then
    /usr/bin/systemctl start laptop-notify.service
fi

Then press ctrl+o, enter, ctrl+x

---

### 4th step:

Make the script executable:
sudo chmod +x /lib/systemd/system-sleep/laptop-wake.sh

---

### 5th step:

Reload systemd & Enable the Service:
sudo systemctl daemon-reload
sudo systemctl enable laptop-notify.service

---

### 6th step:

For Testing
Reboot your system:
sudo reboot

---

### How to Disable or Uninstall

Disable the Service:
sudo systemctl disable laptop-notify.service


Remove Service and Hook Script:
sudo rm /etc/systemd/system/laptop-notify.service
sudo rm /lib/systemd/system-sleep/laptop-wake.sh


Reload systemd:
sudo systemctl daemon-reload
