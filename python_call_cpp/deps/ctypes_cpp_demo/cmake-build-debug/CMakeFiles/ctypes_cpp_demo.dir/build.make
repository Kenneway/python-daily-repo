# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.12

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /opt/clion-2018.2.1/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /opt/clion-2018.2.1/bin/cmake/linux/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/czj/develop/python-daily-repo/python_call_cpp/deps/ctypes_cpp_demo

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/czj/develop/python-daily-repo/python_call_cpp/deps/ctypes_cpp_demo/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/ctypes_cpp_demo.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/ctypes_cpp_demo.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/ctypes_cpp_demo.dir/flags.make

CMakeFiles/ctypes_cpp_demo.dir/main.cpp.o: CMakeFiles/ctypes_cpp_demo.dir/flags.make
CMakeFiles/ctypes_cpp_demo.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/czj/develop/python-daily-repo/python_call_cpp/deps/ctypes_cpp_demo/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/ctypes_cpp_demo.dir/main.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/ctypes_cpp_demo.dir/main.cpp.o -c /home/czj/develop/python-daily-repo/python_call_cpp/deps/ctypes_cpp_demo/main.cpp

CMakeFiles/ctypes_cpp_demo.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/ctypes_cpp_demo.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/czj/develop/python-daily-repo/python_call_cpp/deps/ctypes_cpp_demo/main.cpp > CMakeFiles/ctypes_cpp_demo.dir/main.cpp.i

CMakeFiles/ctypes_cpp_demo.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/ctypes_cpp_demo.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/czj/develop/python-daily-repo/python_call_cpp/deps/ctypes_cpp_demo/main.cpp -o CMakeFiles/ctypes_cpp_demo.dir/main.cpp.s

# Object files for target ctypes_cpp_demo
ctypes_cpp_demo_OBJECTS = \
"CMakeFiles/ctypes_cpp_demo.dir/main.cpp.o"

# External object files for target ctypes_cpp_demo
ctypes_cpp_demo_EXTERNAL_OBJECTS =

ctypes_cpp_demo: CMakeFiles/ctypes_cpp_demo.dir/main.cpp.o
ctypes_cpp_demo: CMakeFiles/ctypes_cpp_demo.dir/build.make
ctypes_cpp_demo: CMakeFiles/ctypes_cpp_demo.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/czj/develop/python-daily-repo/python_call_cpp/deps/ctypes_cpp_demo/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ctypes_cpp_demo"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/ctypes_cpp_demo.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/ctypes_cpp_demo.dir/build: ctypes_cpp_demo

.PHONY : CMakeFiles/ctypes_cpp_demo.dir/build

CMakeFiles/ctypes_cpp_demo.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/ctypes_cpp_demo.dir/cmake_clean.cmake
.PHONY : CMakeFiles/ctypes_cpp_demo.dir/clean

CMakeFiles/ctypes_cpp_demo.dir/depend:
	cd /home/czj/develop/python-daily-repo/python_call_cpp/deps/ctypes_cpp_demo/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/czj/develop/python-daily-repo/python_call_cpp/deps/ctypes_cpp_demo /home/czj/develop/python-daily-repo/python_call_cpp/deps/ctypes_cpp_demo /home/czj/develop/python-daily-repo/python_call_cpp/deps/ctypes_cpp_demo/cmake-build-debug /home/czj/develop/python-daily-repo/python_call_cpp/deps/ctypes_cpp_demo/cmake-build-debug /home/czj/develop/python-daily-repo/python_call_cpp/deps/ctypes_cpp_demo/cmake-build-debug/CMakeFiles/ctypes_cpp_demo.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/ctypes_cpp_demo.dir/depend

