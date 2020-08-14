#!/usr/bin/python
import rospy
import time
from mavros_msgs.msg import State

class mavros_cmd():
    def __init__(self):
        rospy.loginfo("Setting Up the Node...")  
        rospy.init_node('mavros_publisher')

        self._state_msg = State()
        self.state_cmd_pub = rospy.Publisher("mavros/state", State, queue_size=10)
        if(self.state_cmd_pub == False):
            return False
        rospy.loginfo("> State Publisher corrrectly initialized")
        self.current_time = rospy.Time.now()

    def send_state(self):
    	# next, we'll publish the state message over ROS
    	self._state_msg.header.stamp 	= self.current_time
    	self._state_msg.connected 		= True
    	self._state_msg.armed 			= True
    	self._state_msg.guided 			= False
    	self._state_msg.manual_input 	= True
    	self._state_msg.mode 			= "MANUAL"
    	self._state_msg.system_status 	= 3

    	self.state_cmd_pub.publish(self._state_msg)

    @property
    def run(self):
        #--- Set the control rate
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.current_time = rospy.Time.now()
            self.send_state()
            rate.sleep()

if __name__ == "__main__":
    mavros_publisher     	= mavros_cmd()
    mavros_publisher.run()
