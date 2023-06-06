#!/usr/bin/env python3
# import ros 
import rclpy 
from rclpy.node import Node ## import class node 
def main(args=None):
    rclpy.init(args=args) ## initialize ros to create ros communiation 
    node = Node("py_test")
    node.get_logger().info("hello ROS 2")
    rclpy.spin(node)
    rclpy.shutdown()
if __name__== "__main__":
    main()