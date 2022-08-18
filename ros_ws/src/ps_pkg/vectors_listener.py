#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Accel
from std_msgs.msg import Float64

class Vectors_listener():
    def __init__(self):
        rospy.init_node('vectors_listener', anonymous=True)
        rospy.Subscriber('auv_vectors', Accel ,self.callback)
        self.pub = rospy.Publisher('Norm', Float64, queue_size=10)

    def callback(self,msg):
        x=msg.linear.x
        y=msg.linear.y
        z=msg.linear.z

        x=msg.angular.x
        y=msg.angular.y
        z=msg.angular.z

        norm = (x**2 + y**2 + z**2)**0.5
        f = Float64()
        f.data = norm
        rospy.loginfo(f)
        self.pub.publish(f)

if __name__ == '__main__':
    l = Vectors_listener()
    rospy.spin()
