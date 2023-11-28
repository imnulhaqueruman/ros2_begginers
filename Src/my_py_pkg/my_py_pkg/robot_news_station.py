#!/usr/bin/env python3
# import ros 
import rclpy 
from rclpy.node import Node ## import  node class
from example_interfaces.msg import String # dependencies

class RobotNewsStationNode(Node):

    def __init__(self):
        super().__init__("robot_news_station")

        self.publisher_ = self.create_publisher(String,"robot_news", 10) # create publisher with string data type and with a topic namde in this node , here 10 is a que size as like data buffer. We got publisher_ object 
        self.timer_= self.create_timer(0.5, self.publish_news)
        self.get_logger().info("Robot news Station Has been started")

    def publish_news(self):
        msg = String()
        msg.data = "hello"
        self.publisher_.publish(msg)
        
def main(args=None):
    rclpy.init(args=args) ## initialize ros to create ros communiation 
    node = RobotNewsStationNode()
    rclpy.spin(node) # spin allow to node
    rclpy.shutdown() # ros communication shutdown

if __name__== "__main__":
    main()