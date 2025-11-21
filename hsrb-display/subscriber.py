#!/usr/bin/env python

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class ImageSubscriber(Node):
    def __init__(self, topic="/head_display/reveiver"):
        super().__init__('image_subscriber')
        self.image = None

        self.subscription = self.create_subscription(Image,'topic', self.image_callback,10)#rospy.Subscriber(topic, Image, self.image_callback)

        self.bridge = CvBridge()

        print("subscriber started")

    def image_callback(self, msg):

        try:
            image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            print("try showing image")
            if image is not None:
                self._display_image(image)

        except Exception as e:
            self.get_logger().info("Error processing image: %s", e)#rospy.logerr("Error processing image: %s", e)

    def _display_image(self, image):
        # cv2.CAP_IMAGES: Fixed frame. Rescale images to frame
        # cv2.WINDOW_GUI_NORMAL: Fixed frame. Fixed image
        cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

        desired_width = 800  # Example width
        desired_height = 600  # Example height
        cv2.resizeWindow("Image", desired_width, desired_height)

        cv2.imshow("Image", image)
        cv2.waitKey(5)  # Display image for 5 second
        print("changed image")

def main(args=None):
    rclpy.init(args=args)

    image_subscriber = ImageSubscriber()

    rclpy.spin(image_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    image_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

