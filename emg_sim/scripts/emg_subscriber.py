#!/usr/bin/env python

import rospy
import numpy as np
from collections import deque
from std_msgs.msg import Int32MultiArray


class EMGSubscriber:
    '''
    A subscriber that subscribes to 'simulated_emg' topic,
    with a sliding window of size 20 that stores the most recent 20 arrays from this topic.
    It also computes and prints continuously in the terminal the 8-dimensional average of 
    the 8-dimensional integer array over the sliding window. 
    '''
    def __init__(self, window_size):
        rospy.init_node('emg_subscriber', anonymous=True)
        self.window_size = window_size
        self.window = deque(maxlen=self.window_size)
        self.subscriber = rospy.Subscriber('simulated_emg', Int32MultiArray, self.emg_callback)

    def emg_callback(self, msg):
        emg_array = msg.data
        self.window.append(emg_array)
        avg_emg = np.mean(self.window, axis=0)
        rospy.loginfo('Average EMG: %s', avg_emg)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    emg_subscriber = EMGSubscriber(window_size=20)
    emg_subscriber.run()