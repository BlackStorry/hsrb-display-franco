#!/usr/bin/env python

import rclpy
from rclpy.node import Node
import time
from pathlib import Path
import os
#import matplotlib.pyplot as plt

from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class ImagePublisher(Node):

    def __init__(self): # topic="/head_display/reveiver"
        super().__init__('image_publisher')
        self.bridge = CvBridge()

        # Create a publisher for the image
        self.publisher = self.create_publisher(Image,'topic',10)#rospy.Publisher(topic, Image, queue_size=10)
        print("publisher started!")

    def publish_image(self, path):
        image = cv2.imread(path)#image = plt.imread(path)#

        print(image)

        if image is not None:
            print("image is real")
            # Convert the OpenCV image to a ROS image message
            ros_image = self.bridge.cv2_to_imgmsg(image, "bgr8")

            # Publish the ROS image message
            #rospy.sleep(1)
            self.publisher.publish(ros_image)
            print("published image")
        else:
            print("image id none")
            self.get_logger().error(f"Failed to load image: {path}")

def main(args=None):
    rclpy.init(args=args)

    image_publisher = ImagePublisher()


    print("getting images")
    picture_directory = str(Path.home()) + '/workspace/ros/src/hsrb-display-franco/test_images/'
    default_picture = os.path.join(picture_directory, 'default_logo.png')
    doing_picture = os.path.join(picture_directory, 'detecting.png')
    print(default_picture)

    # Ensure subscriber started on hsrb
    # sub = ImageSubscriber()
    # time.sleep(3)

    pub = ImagePublisher()
    pub.publish_image(default_picture)

    time.sleep(3)

    pub.publish_image(doing_picture)

    time.sleep(3)

    pub.publish_image(default_picture)

    print("done")
    #rclpy.spin(image_publisher)
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    image_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()