# Flight_Controller
 open source flight controller software for Multirotor using Arduino and C++, Implementing PID controller, Interrupts, RC communication Protocols.
 
Current version: 1.4 10 Feb, 2021

Content:

Flight_controller.ino

Revision update:
=====================================================================================================================================================

Version 1.3 April 30, 2020
The calibration sketch stops working when a character or number is send. When sending a character via the serial monitor of some Arduino IDE’s a line feed is also send. Because the ESC calibration program only expects one character the program stops working.

In the code the line:
data = Serial.read();                                                               //Read the incomming byte.

Is changed into:
data = Serial.read();                                                               //Read the incomming byte.
delay(100);                                                                         //Wait for any other bytes to come in
while(Serial.available() > 0)loop_counter = Serial.read();                          //Empty the Serial buffer.
=====================================================================================================================================================


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
=====================================================================================================================================================

Version 1.0 - Jan 3, 2020
Release
=====================================================================================================================================================
this software was is created with the help of brooking. 
