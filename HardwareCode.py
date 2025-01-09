#Hardware Code for the Servo Table, Rotary Actuator and Q-Arm

ip_address =  "localhost"
project_identifier = 'P3A'
#--------------------------------------------------------------------------------
import sys
import time
sys.path.append('../')
from Common.hardware_project_library import *
from Common.barcode_checker import *
from Common.standalone_actuator_lib import *
bot = qbot()
hardware = True
arm = qarm(project_identifier,ip_address,hardware)
table = servo_table(ip_address,None,hardware)
scanner = barcode_checker()

#--------------------------------------------------------------------------------
# STUDENT CODE BEGINS
#---------------------------------------------------------------------------------

for x in range(4):
    ##The arm rotates to pick up the bag, after 5 sec so we can scan the luggage
    print("5 seconds to scan the baggage")
    time.sleep(5)
    manualBagDecision = scanner.barcode_check
    arm.home()##Home the arm to make sure all movements are constant
    arm.rotate_base(-86)
    time.sleep(1)
    arm.rotate_elbow(12)
    arm.rotate_shoulder(13)

    arm.rotate_elbow(12)
    time.sleep(1)
    arm.control_gripper(45)
    print("That was supposed to be grab")
    ##Theoretically grabbed it

    arm.rotate_elbow(-15) #Pull bag up and away from the rotater
    time.sleep(1)
    arm.rotate_shoulder(-30)
    time.sleep(1)
    arm.rotate_base(90) ## arm facing straight forwards now
    time.sleep(1)

    

    if manualBagDecision == "Platform": 
            ##Start going to drop on platform
            arm.rotate_base(-20.6)
            time.sleep(1)
            arm.rotate_elbow(-15)
            time.sleep(1)
            arm.rotate_shoulder(30)
            time.sleep(1)
            arm.control_gripper(-45) #Suposed to drop bag on the platform
            time.sleep(1)
            print("That was supposed to be drop on platform")
    else:
            ##Drop the bag in the reject bin
            arm.rotate_base(90)
            time.sleep(1)
            arm.rotate_elbow(-20)
            time.sleep(1)
            arm.rotate_shoulder(30)
            time.sleep(1)
            arm.control_gripper(-45)
            print("That was supposed to drop into the bucket")


    print(arm.effector_position) ## Checks the coordinates

    ##Activates rotary actuator
    bot.activate_stepper_motor()
    bot.rotate_stepper_ccw(4) ## Extend
    time.sleep(5)## Allow time to take bag out
    bot.rotate_stepper_cw(2.25)## bring back to proper spot

    table.rotate_table_angle(90)


#---------------------------------------------------------------------------------
# STUDENT CODE ENDS
#---------------------------------------------------------------------------------


    

    

