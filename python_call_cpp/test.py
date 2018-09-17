import ctypes


if __name__ == '__main__':
    pdll = ctypes.CDLL('deps/ctypes_cpp_demo/libctypes_example.a')
    print pdll.fact(14)