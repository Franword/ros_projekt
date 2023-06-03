<h1 align="center">Welcome to Teb Local Planner Tutorials - obstacles and viapoints 👋</h1>

## Description

This is demo for <a href="http://wiki.ros.org/teb_local_planner" >Teb local planner</a>. It's based on existing <a href="http://wiki.ros.org/teb_local_planner/Tutorials" >tutorials</a>. It's showing examples how to place obstacles and viapoints.

## Prerequisites
Enviorment with <a href="http://wiki.ros.org/" >ROS</a> and <a href="https://www.python.org/" >python</a> installed.

<a href="http://wiki.ros.org/teb_local_planner" >Teb local planner</a> library installed.

ROS running.

Run example from <a href="http://wiki.ros.org/teb_local_planner/Tutorials" >tutorials</a>.
```sh
roslaunch teb_local_planner test_optim_node.launch
```
## Usage

### Publishing obstacles
```sh
python my_publish_viapoints.py 
```
![](readme%20content/viapoints.gif)
### Publishing viapoints.
```sh
python my_publish_obstacle.py
```
![](readme%20content/obstacles.png)

More about vaipoints you can find <a href="http://wiki.ros.org/teb_local_planner/Tutorials/Following%20the%20Global%20Plan%20%28Via-Points%29" >here</a>.
### Publishing feedback.
You need to enable the publish feedback option first. Check <a href="http://wiki.ros.org/teb_local_planner/Tutorials/Inspect%20optimization%20feedback" >this</a> tutorial.

```sh
python my_publish_feedback.py
```
![](readme%20content/feedback1.png)
![](readme%20content/feedback2.png)