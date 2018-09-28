cmake_minimum_required(VERSION 3.2)
project(boost_cpp_demo)

set(CMAKE_CXX_STANDARD 14)

include_directories(/usr/include/python2.7)
include_directories(/usr/lib/python2.7/config-x86_64-linux-gnu)

#link_directories(/usr/lib/x86_64-linux-gnu)

add_library(hello SHARED hello.cpp)
# set prefix otherwise the output will be libhello.so instead of hello.so
set_target_properties(hello PROPERTIES PREFIX "")

target_link_libraries(hello boost_python-py27)

# build
# g++ -fPIC hello.cpp -o hello.so -shared -I/usr/include/python2.7 -I/usr/lib/python2.7/config-x86_64-linux-gnu -lboost_python-py27
