#!/usr/bin/env python3
import rospy
import random
from geometry_msgs.msg import Accel, Point, Vector3
from std_msgs.msg import Float64
class Vector_l:
    def __init__(self):
        rospy.init_node('vector_l', anonymous=True)
        self.pub = rospy.Publisher('auv_linear_vector', Accel, queue_size=10)
       
        self.list = list(range(1000))

    def start(self):
        rate = rospy.Rate(5)
        while not rospy.is_shutdown():

            v = Accel()
            v.linear.x = random.choice(self.list)
            v.linear.y = random.choice(self.list)
            v.linear.z = random.choice(self.list)
            rospy.loginfo(v)
            self.pub.publish(v)
            rate.sleep()

if __name__ == '__main__':
    try:
        t = Vector_l()
        t.start()
    except rospy.ROSInterruptException:
        pass
