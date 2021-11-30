#RemoteTimer
A light remote timer application that allows a timer set on one network device to be displayed on another one. 
Uses ZMQ for communication. Intend to be used e.g. to display the remaining time of a talk to a speaker on stage. 

`model.py` and `view.py` have to be running on the device displaying the Timer.

`control.py` has to run on the device controlling the timer. Current time is output via the console.
Both devices have to be connected through any means supporting tcp.

Quickstart Control: 
1. set correct time in corresponding input
2. click `Send Time` to send the time to the view node. 
3. Use `Start`, `Pause`, `Reset`, `Continue` to control the timer.
4. Use lower input and `add time` to add time to the countdown.


![Control Display](control.png)
![Timer Display](view.png)

# Contributors
- Initial Work: Julian M. Dlugosch