#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32MultiArray
import random


class EMGPublisher():
    '''
    A publisher that publishes an 8-dimensional integer array on a topic named 'simulated_emg'. 
    Each dimension can be randomly sampled between 0-500. 
    '''
    def __init__(self):
        self.pub = rospy.Publisher('simulated_emg', Int32MultiArray, queue_size=10)
        rospy.init_node('emg_publisher', anonymous=True)
        self.rate = rospy.Rate(10)

    def run(self):
        while not rospy.is_shutdown():
            emg_data = [random.randint(0, 500) for i in range(8)]
            # Convert to message
            emg_array = Int32MultiArray(data=emg_data)
            self.pub.publish(emg_array)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        emg_publisher = EMGPublisher()
        rospy.loginfo('Publishing simulated EMG signals ...')
        emg_publisher.run()
    except rospy.ROSInterruptException:
        pass