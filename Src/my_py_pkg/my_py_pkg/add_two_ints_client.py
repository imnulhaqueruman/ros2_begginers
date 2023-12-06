import rclpy 
from rclpy.node import Node ## import  node class
from functools import partial
from example_interfaces.srv import AddTwoInts

class AddTwoIntsClientNode(Node):

    def __init__(self):
        super().__init__("add_two_ints_client")
        self.call_add_two_ints_server(5,6)
        self.call_add_two_ints_server(7,8)
        
    
    def call_add_two_ints_server(self,a,b):
        # create client
        client_= self.create_client(AddTwoInts,"add_two_ints")

        # waiting for server 
        while not client_.wait_for_service(1):
            self.get_logger().warn("waiting for server")

        # create request
        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        # call async in server with request
        future = client_.call_async(request)
        future.add_done_callback(partial(self.callback_call_two_int, a=a), b=b) 

    def callback_call_two_int(self, future, a, b):
        try:
           response = future.result()
           self.get_logger().info(str(a) + " + " + str(b) + " = " + str(response.sum))
        except Exception as e:
           self.get_logger().error("service call failed %r" % (e,))

def main(args=None):
    rclpy.init(args=args) ## initialize ros to create ros communiation 
    node = AddTwoIntsClientNode()
    rclpy.spin(node) # spin allow to node
    rclpy.shutdown() # ros communication shutdown

if __name__== "__main__":
    main()