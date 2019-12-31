# Pomelo

We implemented physical code blocks that have icons that demonstrate the function of the block such as move forward, right, left or backward. Pomelo will be used in a classroom environment where the teacher creates puzzles for students. Students will arrange the block in order to complete the maze. These kinds of assignments will encourage collaboration between students as well as teach them essential skills like problem-solving and critical thinking. This programming method doesn’t bore students since it feels more like playing with a robot rather than coding. 

To create these aforementioned code blocks, we placed an ArUco marker on the top left corner of all sides of the blocks. When the student presses the button on top of the robot, the camera, in the form of the robot, will read these markers from top to bottom and perform the moves accordingly. 

To make the interaction between Pomelo and the students more natural, we observed elementary school classes and interviewed teachers. The most optimal design seemed to be a dog-shaped robot. Moreover, we added a display board that shows Pomelo’s eyes and emotions to make the interaction less mechanical and more organic. 

Our future goals include implementing a voice assistant to further help students during classes. Students have different paces while learning and it is very easy for a student to fall behind. Pomelo will be answering the students’ questions via visuals on the display board and the voice assistant. Another aspect we want to include is Pomelo being personalized to each student; via camera and microphone, Pomelo will keep track of the student and work on improving their weaker sides.

Code installation guide, 3D design, and electronic componenets can be found below. 

# The Code

Pomelo is ran from the shell script run.sh which is used to run main.py and modprobe bcm2835-v4l2, which is used to access  the picamera through pygame. Inside main.py two threads are created. One that runs the takeInput method, which is used to detect when an input is made and runs the code accordingly, in ArucoClass.py and the Loop method, which is used to make the pygame screen and display the many faces and emotions of pomelo, in MonitorClass.py. Both of these modules are located in the Main_Lib directory, which also contains the motorClass.py module. First of all the motorClass module is used to define the methods that configure the movements of the motors. To do this we use the pololu_drv_8835_rpi library. This module is than used by the ArucoClass module. The ArucoClass module is used to detect the ArucoBlocks that are stacked in front of Pomelo. To do this, the module waits until it recieves input from the button placed on top of the head. When it recieves the input, the camera placed on the front of Pomelo takes a picture of its surroundings and detects ArucoMarkers placed on the ArucoBlocks. To do this we use the OpenCV library and the Aruco library found in it. After detecting the Aruco block and assigning a value to it, Pomelo executes the given functions, whether it states the amount of time to do the action or the action itself. Finally if it actually saw the markers, than it assigns a value accordingly and puts it in the queue so that the MonitorClass's methods can access it while it's running as parallel thread. In the MonitorClass module, it defines the main window the animations and faces of pomelo in the setup. Then inside the loop it does an animation according to the value given inside the queue by the ArucoClass. To not mix up these parallel threads, the code inside these threads uses a lock to stop the consumer(MonitorClass) from using the value by the producer(ArucoClass) before it stops executing.

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
