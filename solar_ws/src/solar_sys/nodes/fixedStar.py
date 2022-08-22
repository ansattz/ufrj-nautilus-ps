#!/usr/bin/env python3
import rospy
import tf2_ros  
import geometry_msgs.msg
import math

if __name__ == '__main__':
    rospy.init_node('fixedStar')
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()
    u = geometry_msgs.msg.TransformStamped()
    
    t.header.frame_id = "star"
    t.child_frame_id = "planet"

    u.header.frame_id = "planet"
    u.child_frame_id = "sat"

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        x = rospy.Time.now().to_sec() * math.pi
        y = rospy.Time.now().to_sec() * math.pi

        t.header.stamp = rospy.Time.now()
        t.transform.translation.x = 5.0 * math.cos(0.1*x)
        t.transform.translation.y = 5.0 * math.sin(0.1*y)
        t.transform.translation.z = 0.0
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        u.header.stamp = rospy.Time.now()
        u.transform.translation.x = 1.8 * math.cos(0.8*x)
        u.transform.translation.y = 1.8 * math.sin(0.8*y)
        u.transform.translation.z = 0.0
        u.transform.rotation.x = 0.0
        u.transform.rotation.y = 0.0
        u.transform.rotation.z = 0.0
        u.transform.rotation.w = 1.0

        br.sendTransform(u)
        br.sendTransform(t)
        rate.sleep()
