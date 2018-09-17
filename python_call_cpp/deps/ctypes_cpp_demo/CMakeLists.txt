cmake_minimum_required(VERSION 3.12)
project(ctypes_cpp_demo)

set(CMAKE_CXX_STANDARD 14)

include_directories(/usr/include/python2.7)
include_directories(/usr/lib/python2.7/config)

add_library(ctypes_demo SHARED wrapper.cpp)

# build
# g++ -fPIC wrapper.cpp -o example.so -shared -I/usr/include/python2.6 -I/usr/lib/python2.6/config
