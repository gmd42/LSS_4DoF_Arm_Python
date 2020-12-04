# LSS_4DoF_Arm_Python
## Senior Design Group 8B

This project utilizes the [Official Lynxmotion Smart Servo (LSS) libraries for Python](https://github.com/Lynxmotion/LSS_Library_Python).

### Install these packages with a package installer like pip:
- RPi
- tkinter
- pyserial

Important files:
- main.py: This has the arm start its cyclic motion in the work cell
- motion.py: The main program uses this class to define the specific inputs to the servos for all of the arm's motion
- contact_sensor.py: The main program uses this to define the expected states of the contact sensor at every step of the arm's motion. Reading an unexpected signal from the GPIO pim will raise an AssertError
- positionGUI.py: This is an unfinished GUI for setting the positon of the servos. The hold and limp buttons are functional.
- The remaining files have been forked from another LSS library repository and have not beem changed.

### How to set up the LSS Lynxmotion arm for the work cell:

 1. Connect the two contact sensor wires to a ground pin and a digital GPIO pin (and remember this pin number).
 2. In approximately line 58 of main.py, change the value to the GPIO input number.
 3. Install the dependencies of the code listed above.
 4. Connect the microcontroller to the controller in the arm, if not already connected.
 5. Power the arm and the microcontroller.
 6. Run main.py
 7. If the COM port causes an error, refer to the error description below.

### Common errors:
- The COM port is not available or not reading anything.
  - The COM ports are set differently when running the program on a Linux computer and a Windows computer. Check the devices connected to the computer to see find the corrected COM port. Also, check that all components are receiving power, including the arm and microcontroller.
- AssertionError is raised unexpectedly.
  - This error only happens when the stent is not correctly picked up and released at every step. Otherwise, check that the correct GPIO pins are connected to the contact sensor and that the list of correct states reflects the actual expected states of the contact sensor.
