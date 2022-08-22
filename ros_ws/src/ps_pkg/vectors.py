#!/usr/bin/env python3
import rospy
import random
from geometry_msgs.msg import Accel
from std_msgs.msg import Float64
class Vectors:
    def __init__(self):
        rospy.init_node('vectors', anonymous=True)
        self.pub = rospy.Publisher('auv_vectors', Accel, queue_size=10)
       
        self.list = list(range(1000))

    def start(self):
        rate = rospy.Rate(5)
        while not rospy.is_shutdown():

            v = Accel()
            v.linear.x = random.choice(self.list)
            v.linear.y = random.choice(self.list)
            v.linear.z = random.choice(self.list)

            v.angular.x = random.choice(self.list)
            v.angular.y = random.choice(self.list)
            v.angular.z = random.choice(self.list)

            rospy.loginfo(v)
            self.pub.publish(v)
            rate.sleep()

if __name__ == '__main__':
    try:
        t = Vectors()
        t.start()
    except rospy.ROSInterruptException:
        pass
