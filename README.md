# EMG_simulation
This is a ROS practice. The task is to write a topic named "simulated_emg". In this topic, there is a publisher and a subscriber.

# Procedures to run the code
Prepare a catkin workspace. The workspace is created under the home directory below.
```bash
mkdir ~/catkin_ws
cd ~/catkin_ws
mkdir src
```
Prepare and build the workspace.
```bash
catkin_make
```
Clone the repository to the `src` directory.
```bash
cd src
git clone https://github.com/Dongx1aoYang/EMG_simulation.git
```
Go back the the workspace root directory and source the `setup.bash`.
```bash
cd ~/catkin_ws
source devel/setup.bash
```
Build the catkin workspace again.
```bash
cd ..
catkin_make
```
Run `roscore` to activate ROS.
```bash
roscore
```
Now the publisher and the subscriber should be ready for launch.
To run the publisher, open a new terminal:
```bash
rosrun emg_sim emg_publisher.py
```
To run the subscriber, open another new terminal:
```bash
rosrun emg_sim emg_publisher.py
```
