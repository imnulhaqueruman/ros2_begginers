#!/usr/bin/env python3
# import ros 
import rclpy 
from rclpy.node import Node ## import  node class

class MyNode(Node):

    def __init__(self):
        super().__init__("py_test")
        self.counter_= 0
        self.get_logger().info("Hello ROS2")
        self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info("Hello" + str(self.counter_))
def main(args=None):
    rclpy.init(args=args) ## initialize ros to create ros communiation 
    node = MyNode()
    rclpy.spin(node) # spin allow to node
    rclpy.shutdown() # ros communication shutdown
    
if __name__== "__main__":
    main()