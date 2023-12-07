import rclpy
from rclpy.node import Node 
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class NumberCounterNode(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.counter = 0
        self.server_= self.create_service(SetBool, "reset_counter", self.reset_Counter )
        self.publisher_= self.create_publisher(Int64, "number_counter", 10)
        self.subscriber_= self.create_subscription(Int64, "number",self.publish, 10)
        self.get_logger().info("Number counter node has been started with a server")

    def reset_Counter(self, request,response):
        if request.data:
            self.counter=0
            response.success =True
            response.message="Counter has been reset"
        else:
            response.success = False
            response.message="counter has not been reset"
            # self.get_logger().info(response.message)
        return response

    def publish(self, msg):
        self.counter += msg.data 
        new_msg = Int64()
        new_msg.data = self.counter
        self.publisher_.publish(new_msg)

def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
    main()