import ctypes


if __name__ == '__main__':

    # test ctypes
    pdll = ctypes.CDLL('deps/ctypes_cpp_demo/cmake-build-debug/libctypes_demo.so')
    print pdll.fact(14)
