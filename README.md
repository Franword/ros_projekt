<h1 align="center">Welcome to Teb Local Planner Tutorials - obstacles and viapoints 👋</h1>

## Description

This is demo for <a href="http://wiki.ros.org/teb_local_planner" >Teb local planner</a>. It's based on existing <a href="http://wiki.ros.org/teb_local_planner/Tutorials" >tutorials</a>. It's showing examples how to place obstacles and viapoints.

## Prerequisites
Enviorment with <a href="http://wiki.ros.org/" >ROS</a> installed.

<a href="http://wiki.ros.org/teb_local_planner" >Teb local planner</a> library installed.

ROS running.

Run example from <a href="http://wiki.ros.org/teb_local_planner/Tutorials" >tutorials</a>.
```sh
roslaunch teb_local_planner test_optim_node.launch
```
## Usage

### Publishing obstacles
```sh
rosrun teb_local_planner_tutorials my_publish_viapoints.py 
```
### Publishing viapoints.
```sh
rosrun teb_local_planner_tutorials my_publish_obstacle.py
```
More about vaipoints you can find <a href="http://wiki.ros.org/teb_local_planner/Tutorials/Following%20the%20Global%20Plan%20%28Via-Points%29" >here</a>.
### Publishing feedback.
You need to enable the publish feedback option first. Check <a href="http://wiki.ros.org/teb_local_planner/Tutorials/Inspect%20optimization%20feedback" >this</a> tutorial.

```sh
rosrun teb_local_planner_tutorials my_publish_feedback.py
```

