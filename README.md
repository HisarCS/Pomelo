# pomelo
kore

## Step 1 - Install OpenCV
You can install OpenCV on your Raspberry Pi by following this guide: https://www.pyimagesearch.com/2018/09/19/pip-install-opencv/

## Step 2 - Install pomelo
Run these commands:  
```
cd ~  
git clone https://github.com/HisarCS/pomelo  
```
## Step 3 - pololu_drv8835_rpi library
You can install pololu_drv8835_rpi on your Raspberry Pi by following this guide:https://github.com/pololu/drv8835-motor-driver-rpi

## Step 4 - Gasist library
You can install Gasist on your Raspberry Pi by following this guide:https://github.com/shivasiddharth/GassistPi

## Step 5 - Make the script executable  
Run these commands:  
```
cd ~/pomelo  
chmod +x run.sh  
```
  
## Step 6 - Run it!  
Now you can execute the script by this command:
```
~/pomelo/run.sh  
```

## Optional - Run Pomelo always when Raspberry Pi boots
Run this command:  
```
crontab -e  
```
Select nano editor  
Add the following line to end of the crontab file:  
```
@reboot ~/pomelo/run.sh
```
