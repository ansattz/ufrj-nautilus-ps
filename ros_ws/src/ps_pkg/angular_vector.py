#!/usr/bin/env python3
import rospy
import random
from geometry_msgs.msg import Accel
class Angular_vector:
    def __init__(self):
        rospy.init_node('angular_vector', anonymous=True)
        self.pub = rospy.Publisher('auv_angular_vector', Accel, queue_size=10)
       
        self.list = list(range(1000))

    def start(self):
        rate = rospy.Rate(5)
        while not rospy.is_shutdown():
            v = Accel()
            v.angular.x = random.choice(self.list)
            v.angular.y = random.choice(self.list)
            v.angular.z = random.choice(self.list)

            rospy.loginfo(v)
            self.pub.publish(v)
            rate.sleep()

if __name__ == '__main__':
    try:
        t = Angular_vector()
        t.start()
    except rospy.ROSInterruptException:
        pass
