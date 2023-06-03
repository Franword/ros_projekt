#!/usr/bin/env python

# This small script subscribes to the FeedbackMsg message of teb_local_planner
# and plots the current velocity.
# publish_feedback must be turned on such that the planner publishes this information.
# Author: christoph.roesmann@tu-dortmund.de

import rospy, math
from teb_local_planner.msg import FeedbackMsg, TrajectoryMsg, TrajectoryPointMsg
from geometry_msgs.msg import PolygonStamped, Point32
import numpy as np
import matplotlib.pyplot as plotter
from tf.transformations import euler_from_quaternion

def feedback_callback(data):
  global trajectory

  if not data.trajectories: # empty
    trajectory = []
    return
  trajectory = data.trajectories[data.selected_trajectory_idx].trajectory
  
def plot_velocity_profile(fig, ax, x,y,v,yaw):
  ax.cla()
  ax.grid()
  ax.set_ylabel('Posiotion y [m]')
  ax.set_xlabel('Posiotion x [m]')
  vx = v*np.cos(yaw)
  vy = v*np.sin(yaw)
  ax.quiver(x, y, vx, vy,headwidth=10,width=0.001)
  fig.canvas.draw()
  
def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.trajectories[data.selected_trajectory_idx].trajectory)
    
def velocity_plotter():
  global trajectory
  rospy.init_node("visualize_velocity_profile", anonymous=True)
  
  topic_name = "/test_optim_node/teb_feedback"
  rospy.Subscriber(topic_name, FeedbackMsg, feedback_callback, queue_size = 1) # define feedback topic here!

  rospy.loginfo("Visualizing velocity profile published on '%s'.",topic_name) 
  rospy.loginfo("Make sure to enable rosparam 'publish_feedback' in the teb_local_planner.")

  # two subplots sharing the same t axis
  fig, ax = plotter.subplots()
  #fig = plotter.figure()
  plotter.ion()
  plotter.show()
  
  r = rospy.Rate(1) # define rate here
  while not rospy.is_shutdown():
    
    t = []
    v= []
    a=[]
    x=[]
    y=[]
    yaw = []
    omega = []
    
    for point in trajectory:
      t.append(point.time_from_start.to_sec())
      x.append(point.pose.position.x)
      y.append(point.pose.position.y)
      v.append(point.velocity.linear.x)
      quaterion = [point.pose.orientation.x,point.pose.orientation.y,point.pose.orientation.z,point.pose.orientation.w]
      euler = euler_from_quaternion(quaterion)
      yaw.append(euler[2])
      
      omega.append(point.velocity.angular.z)
          
    plot_velocity_profile(fig, ax, np.asarray(x), np.asarray(y), np.asarray(v),np.asarray(yaw))
        
    r.sleep()

if __name__ == '__main__': 
  try:
    trajectory = []
    velocity_plotter()
  except rospy.ROSInterruptException:
    pass

