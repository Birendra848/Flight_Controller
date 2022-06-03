# Quadcopter Build
<b>Schematic</b>
<br>
![YMFC-3D_scematic](https://user-images.githubusercontent.com/75802334/171931255-70936a6f-4132-4fc5-9cf5-89725974b614.jpg)
<br>
<b>Build image</b>
<br>
![20200225_162116](https://user-images.githubusercontent.com/75802334/171933988-e43b156c-e09e-49eb-bfbf-9338c0bec638.jpg)
![20200225_162311](https://user-images.githubusercontent.com/75802334/171941092-c0281f23-66fe-4293-a000-7832406f0772.jpg)


https://user-images.githubusercontent.com/75802334/171941173-60b2e9ef-f506-4996-898f-9fe8aeb58238.mp4



# Flight_Controller
Open source flight controller software for Quadcopter using Arduino and C++, Implementing PID controller, Interrupts, RC communication Protocols.
 
Current version: 1.2 10 Feb, 2021

Content:

Flight_controller.ino


Version 1.1 - 12 Feb, 2016
There was a NaN (not a number) problem in the code. When flying more aggressive the quadcopter could become uncontrolable. The NaN problem is caused by the following:
When the absolute value of acc_y or acc_x becomes larger that the acc_total_vector the values provided to the asin function is larger than 1 and the asin function produces a NaN.
It recovers when the acc_total_vector becomes larger that the acc_x or acc_y values. But due to the complimentary filter the NaN error persists.
This problem will only occur when flying aggressive / fast descents. 

I changed the code as followed:
from:
angle_pitch_acc = asin((float)acc_y/acc_total_vector)* 57.296;            //Calculate the pitch angle.
angle_roll_acc = asin((float)acc_x/acc_total_vector)* -57.296;            //Calculate the roll angle.

to:
if(acc_y > acc_total_vector){
  angle_pitch_acc = asin((float)acc_y/acc_total_vector)* 57.296;            //Calculate the pitch angle.
}
if(acc_x > acc_total_vector){
  angle_roll_acc = asin((float)acc_x/acc_total_vector)* -57.296;            //Calculate the roll angle.
}

This software is created with the help of brooking.net



