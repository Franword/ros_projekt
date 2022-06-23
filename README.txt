Aby wykorzystać przygotowane pliki należy przede wszystkim odpalić poniższy plik .launch.
roslaunch teb_local_planner test_optim_node.launch

Następnie można przetestować program my_publish.obstacle oraz my_publish_viapoints.
Ja przykładowo wrzuciłem pliki do ~/catkin_ws/src/teb_local_planer_tutorials/scripts i odpalałem komendami:
rosrun teb_local_planner_tutorials my_publish_viapoints.py 
rosrun teb_local_planner_tutorials my_publish_obstacle.py

Tak samo należy odpalić my_publish_feedback. Trzeba jednak wcześniej włączyć opcję publikowania feedbacku. Jest to pokazane w poniższym tutorialu.
http://wiki.ros.org/teb_local_planner/Tutorials/Inspect%20optimization%20feedback

Więcej o viapoints w poniższym poradniku.
http://wiki.ros.org/teb_local_planner/Tutorials/Following%20the%20Global%20Plan%20%28Via-Points%29






