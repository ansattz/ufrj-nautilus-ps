#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Accel
from std_msgs.msg import Float64

class Linear_listener():
    def __init__(self):
        rospy.init_node('linear_listener', anonymous=True)
        rospy.Subscriber('auv_linear_vector', Accel ,self.callback)
        self.pub = rospy.Publisher('Norm', Float64, queue_size=10)

    def callback(self,msg):
        x=msg.linear.x
        y=msg.linear.y
        z=msg.linear.z

        norm = (x**2 + y**2 + z**2)**0.5
        f = Float64()
        f.data = norm
        rospy.loginfo(f)
        self.pub.publish(f)

if __name__ == '__main__':
    l = Linear_listener()
    rospy.spin()
