# Quadcopter Build
<b>Schematic</b>
<br>
![YMFC-3D_scematic](https://user-images.githubusercontent.com/75802334/171931255-70936a6f-4132-4fc5-9cf5-89725974b614.jpg)
<br>

<b>Take off and Flight Video</b>



https://user-images.githubusercontent.com/75802334/171943030-e3c4fde3-ca75-489b-8f51-9f5a2d57a10e.mp4


<br><b>Landing Video</b><br>



https://user-images.githubusercontent.com/75802334/171943679-0fec2d1e-469c-4859-953c-a3a91209ac55.mp4


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



