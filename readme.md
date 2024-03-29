# Setup your ROS2 environment
```bash
source /opt/ros/humble/setup.bash

gedit ~/.bashrc
# Add the following line at the end of the file and save it
source /opt/ros/humble/setup.bash

# install ros2 dependencies 
sudo apt install python3-colcon-common-extensions

gedit ~/.bashrc
# Add the following line at the end of the file and save it
source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
```
# ROS2 python package 
```bash
# cd to your directory 
cd ros2_ws/src
# create pkg command 
ros2 pkg create my_py_pkg(pkg name) --build-type (argument) ament_python --dependencies rclpy

```
 
# before build to check 
```bash
 pip3 list 
 # if not found 
 sudo apt install python3-pip
 # then check again 
 pip3 list 

 pip3 list | grep setuptools 

 # check verison and upgrade 
 pip3 install setuptools==version no

```
# Compile to your package
```bash
colcon build 
# your package successfully build 

# if you want build specific  packages
colcon build --packages-select my_py_pkg 
# hurrah! your python package now ready to host any python node 
```
# Create C++ package 
```bash
ros2 pkg create my_cp_pkg --build-type ament_cmake --dependencies rclcpp
```
# Build c++ package 
```bash
  colcon build 
  colcon build --packages-select my_cp_pkg
```
# ROS2 -Nodes 
* subprograms in your application, responsible for only one thing as like class .
* Combined into a graph .
* Two nodes communicate with each other through ros topics , service and parameter .
![Alt text](image-1.png)

# Run any node in Python
```bash
# executeable command 
cd /directory/my_py_pkg
chmod +x my_first_node.py 
./my_first_node.py
```
## After creating node add this node in console scripts inside the setup.py folder and then run 
```bash
colcon build 
# after build the node it will store in install folder 
cd /install/my_py_pkg/my_py_pkg/lib 
and run ./py_node
```
# Basic Python node template you can use to create every node 
```python
import rclpy
import rclpy.node import Node 

class Mynode(Node):
    def __init__(self):
        super().__init__("py_test")
        self.get_logger().info("Hello ROS2")

def main(args=None):
    rclpy.init(args=args)
    node = Mynode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__"
    main()
```
#### After writing the node, you compile it, and you re-source your environment in order to use it. Nodes are compiled (only for Cpp), and installed (for both Python and Cpp), inside the install/ folder of your ROS2 workspace
```bash
# You can directly execute them from here, or by using the command line tool “ros2 run <package> <executable>”.
 ros2 run my_py_pkg py_node 
 # first build 
 colcon build 
 cd /ros2_bigginers 
 source install/setup.bash

 # then this command will execute any where 
```
# Minimal C++ node 
```c++

#include "rclcpp/rclcpp.hpp"

int main(int argc,char **argv)
{
    rclcpp::init(argc, argv); // initialize ros2 communication
    auto node = std::make_shared<rclcpp::Node>("cpp_test");
    RCLCPP_INFO(node->get_logger(), "Hello CPP Node");
    rclcpp::spin(node);
    rclcpp::shutdown(); // shutdown 
   return 0;
}
```
# Build Package 
```bash
 cd /ros2_begginers
 colcon build --packages-select my_cp_pkg

```
#### After c++ node build you have to changes your CMakeLists.txt file 
```bash
# add executabel (node_name src/filename)
add_executable(cpp_node src/my_first_node.cpp)
# add dependencies (node rclcpp)
ament_target_dependencies(cpp_node rclcpp)

# after build node it will store this folder 
install(TARGETS
  cpp_node 
  DESTINATION lib/${PROJECT_NAME}
)
# open terminal 
cd /ros2_beginners/install/my_cp_pkg/lib/my_cp_pkg ./cpp_node

# or you can run 
ros2 run my_cp_pkg cpp_node
```