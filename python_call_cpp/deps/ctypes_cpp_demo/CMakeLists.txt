cmake_minimum_required(VERSION 3.12)
project(ctypes_cpp_demo)

set(CMAKE_CXX_STANDARD 14)
# add_executable(ctypes_cpp_demo main.cpp)

include_directories(/usr/include/python2.7)
include_directories(/usr/lib/python2.7/config)

add_library(ctypes_example wrapper.cpp)







