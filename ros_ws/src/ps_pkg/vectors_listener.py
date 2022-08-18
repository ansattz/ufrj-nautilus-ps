#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Accel
from std_msgs.msg import Float64

class Vectors_listener():
    def __init__(self):
        rospy.init_node('vectors_listener', anonymous=True)
        rospy.Subscriber('auv_vectors', Accel ,self.callback)
        self.pub1 = rospy.Publisher('Vlinear_norm', Float64, queue_size=10)
        self.pub2 = rospy.Publisher('Vangular_norm', Float64, queue_size=10)

    def callback(self,msg):
        x=msg.linear.x
        y=msg.linear.y
        z=msg.linear.z

        x=msg.angular.x
        y=msg.angular.y
        z=msg.angular.z
        
        Vlinear_norm = (x**2 + y**2 + z**2)**0.5
        Vangular_norm = (x**2 + y**2 + z**2)**0.5

        f1 = Float64()
        f2 = Float64()
        f2.data = Vangular_norm
        f1.data = Vlinear_norm
        rospy.loginfo(f1)
        self.pub1.publish(f1)
        self.pub2.publish(f2)

if __name__ == '__main__':
    l = Vectors_listener()
    rospy.spin()
