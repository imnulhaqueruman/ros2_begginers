import rclpy
from rclpy.node import Node 
from example_interfaces.msg import Int64

class NumberCounterNode(Node):
    def __init__(self):
        super().__init__("py_test")
        self.get_logger().info("Hello ROS2")

def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
    main()