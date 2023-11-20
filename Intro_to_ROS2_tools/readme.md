# Introduction to ROS2 tools
###### In this section you will learn more about some of the most useful ROS2 tools. Those tools are an important part of the ROS2 ecosystem, they will allow you to debug your nodes and your whole ROS2 application

# ros2 run 
#### The command ros2 run launches an executable from a package.
```bash
ros2 run <package_name> <executable_name>
```
# ros2 node list 
#### ros2 node list will show you the names of all running nodes. This is especially useful when you want to interact with a node, or when you have a system running many nodes and need to keep track of them.
```bash
  ros2 node list 
  # The terminal return the node name 
  /py_node
```
# ros2 node info 
#### returns a list of subscribers, publishers, services, and actions. i.e. the ROS graph connections that interact with that node. 
```bash
  ros2 node info /py_node
```
#### The output should look like this 
```bash
/py_test
  Subscribers:

  Publishers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
  Service Servers:
    /py_test/describe_parameters: rcl_interfaces/srv/DescribeParameters
    /py_test/get_parameter_types: rcl_interfaces/srv/GetParameterTypes
    /py_test/get_parameters: rcl_interfaces/srv/GetParameters
    /py_test/list_parameters: rcl_interfaces/srv/ListParameters
    /py_test/set_parameters: rcl_interfaces/srv/SetParameters
    /py_test/set_parameters_atomically: rcl_interfaces/srv/SetParametersAtomically
  Service Clients:

  Action Servers:

  Action Clients:
```