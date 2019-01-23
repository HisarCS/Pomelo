# pomelo
kore

## Step 1 - Install OpenCV
You can install OpenCV on your Raspberry Pi by following this guide: https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/

## Step 2 - Install pomelo
Run these commands:  
cd ~  
git clone https://github.com/HisarCS/pomelo  
  
## Step 3 - Make the script executable  
Run these commands:  
cd ~/pomelo  
chmod +x run.sh  
  
## Step 4 - Run it!  
Now you can execute the script by this command:  
~/pomelo/run.sh  

## Optional - Run Pomelo always when Raspberry Pi boots
Run this command:  
crontab -e  
Select nano editor  
Add the following line to end of the crontab file:  
@reboot ~/pomelo/run.sh
