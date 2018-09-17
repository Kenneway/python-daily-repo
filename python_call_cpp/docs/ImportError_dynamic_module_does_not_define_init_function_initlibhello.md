# issue

使用python通过boost_python调用c++时, c++动态库编译完毕,python导入动态库时报错如下:

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ImportError: dynamic module does not define init function (initlibhello)

# solution

## 原因:

1. Python 3.X扩展的入口函数签名如下：
// 其中xxxxxxx是module名，必须保持一致
PyMODINIT_FUNC PyInit_xxxxxxx(void);    
详见：http://docs.python.org/3/extending/

2. Python 2.X扩展的入口函数签名如下：
// 其中xxxxxxx是module名，必须保持一致
PyMODINIT_FUNC initxxxxxxx(void)    

当python代码使用中 "import abc" 导入abc.so时,
其实是调用了 PyMODINIT_FUNC initabc(void) 函数

以 hello 为例,如若其cmake文件如下,通过编译生成了libhello.so

    cmake_minimum_required(VERSION 3.12)
    project(boost_cpp_demo)
    
    set(CMAKE_CXX_STANDARD 14)
    
    include_directories(/usr/include/python2.7)
    include_directories(/usr/lib/python2.7/config-x86_64-linux-gnu)
    
    #link_directories(/usr/lib/x86_64-linux-gnu)
    add_library(hello SHARED hello.cpp)

    target_link_libraries(hello boost_python-py27)
    
在生成so库的时候, 入口函数签名会被映射为inithello()
在使用 "import libhello" 导入libhello.so时,程序会自动调用initlibhello()
故会报改错

## 解决

### 方法1

    mv libhello.so hello.so
    
### 方法2

cmake文件改为:

    cmake_minimum_required(VERSION 3.12)
    project(boost_cpp_demo)
    
    set(CMAKE_CXX_STANDARD 14)
    
    include_directories(/usr/include/python2.7)
    include_directories(/usr/lib/python2.7/config-x86_64-linux-gnu)
    
    #link_directories(/usr/lib/x86_64-linux-gnu)
    
    add_library(hello SHARED hello.cpp)
    # set prefix otherwise the output will be libhello.so instead of hello.so
    set_target_properties(hello PROPERTIES PREFIX "")
    
    target_link_libraries(hello boost_python-py27)

生成hello.so而不是libhello.so

