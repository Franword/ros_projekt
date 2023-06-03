#!/usr/bin/env python

# Author: christoph.roesmann@tu-dortmund.de

import rospy, math
from costmap_converter.msg import ObstacleArrayMsg, ObstacleMsg
from geometry_msgs.msg import PolygonStamped, Point32

def publish_obstacle_msg():
  pub = rospy.Publisher('/test_optim_node/obstacles', ObstacleArrayMsg, queue_size=1)
  #pub = rospy.Publisher('/p3dx/move_base/TebLocalPlannerROS/obstacles', ObstacleArrayMsg, queue_size=1)
  rospy.init_node("test_obstacle_msg")


  obstacle_msg = ObstacleArrayMsg() 
  obstacle_msg.header.stamp = rospy.Time.now()
  obstacle_msg.header.frame_id = "odom" # CHANGE HERE: odom/map
  
  obstacles = [[-3,0],[-2,-0.5],[0,0],[2,0.3],[2,-1],[4,0]]
  for id, obstacle in enumerate(obstacles):
    obstacle_msg.obstacles.append(ObstacleMsg())
    obstacle_msg.obstacles[id].id = id
    obstacle_msg.obstacles[id].polygon.points = [Point32()]
    obstacle_msg.obstacles[id].polygon.points[0].x = obstacle[0]
    obstacle_msg.obstacles[id].polygon.points[0].y = obstacle[1]
    obstacle_msg.obstacles[id].polygon.points[0].z = 0

  r = rospy.Rate(10) # 10hz
  # t = 0.0
  while not rospy.is_shutdown():
    
    # Vary y component of the point obstacle
    # obstacle_msg.obstacles[0].polygon.points[0].y = 1*math.sin(t)
    # t = t + 0.1
    
    pub.publish(obstacle_msg)
    
    r.sleep()



if __name__ == '__main__': 
  try:
    publish_obstacle_msg()
  except rospy.ROSInterruptException:
    pass

