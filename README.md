# Turtoise Bot

This is a gazebo repository containing a custom mobile robot called <i>Turtoise bot</i> including camera and lidar plugins

### Instructions

1. Create a ros workspace

```
mkdir robot_ws/src
cd robot_ws/src
catkin_init_workspace
cd ..
catkin_make
```

2. Clone the repository to the src folder

```
cd src
git clone https://github.com/Rajpal9/turtoise_bot.git
cd ..
catkin_make
```

3. source the setup.bash file and launch the simulation
```
source ./devel/setup.bash
roslaunch turtoise_bot turtoisebot.launch
```

4. Launching turtoise bot with camera simulation and viewing the images. For this step, close any gazebo simulation, if running.
```
roslaunch turtoise_bot turtoisebot_camera.launch
rosrun image_view image_view image:=/camera1/image_raw
```
