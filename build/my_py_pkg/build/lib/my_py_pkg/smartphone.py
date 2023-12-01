#!/usr/bin/env python3
# import ros 
import rclpy 
from rclpy.node import Node ## import  node class
from example_interfaces.msg import String
class SmartphoneNode(Node):

    def __init__(self):
        super().__init__("smartphone")
        self.subscriber_ = self.create_subscription(String, "robot_news",self.callback_robot_news, 10)
        self.get_logger().info("smartphonenode has been started")

    def callback_robot_news(self,msg):
        self.get_logger().info(msg.data)
def main(args=None):
    rclpy.init(args=args) ## initialize ros to create ros communiation 
    node = SmartphoneNode()
    rclpy.spin(node) # spin allow to node
    rclpy.shutdown() # ros communication shutdown

if __name__== "__main__":
    main()