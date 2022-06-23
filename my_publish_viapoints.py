#!/usr/bin/env python

import rospy, math
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path
from math import sin


def publish_via_points_msg():
  pub = rospy.Publisher('/test_optim_node/via_points', Path, queue_size=1)
  rospy.init_node("test_via_points_msg")


  via_points_msg = Path() 
  via_points_msg.header.stamp = rospy.Time.now()
  via_points_msg.header.frame_id = "odom" # CHANGE HERE: odom/map
  
  r = rospy.Rate(5) # 10hz
  t = 0.0
  points = []
  while not rospy.is_shutdown():
    t = t + 0.1
    points.clear()
    for x in range(-40,40,1):
      point = PoseStamped()
      point.pose.position.x = x/10
      point.pose.position.y = sin(t)*sin((x+40)*0.2)
      points.append(point)
    
    
    via_points_msg.poses = points

    pub.publish(via_points_msg)
    
    r.sleep()



if __name__ == '__main__': 
  try:
    publish_via_points_msg()
  except rospy.ROSInterruptException:
    pass

