# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

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
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/dirrgang/exercism/cpp/hamming

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/dirrgang/exercism/cpp/hamming/build

# Utility rule file for test_hamming.

# Include the progress variables for this target.
include CMakeFiles/test_hamming.dir/progress.make

CMakeFiles/test_hamming: hamming
	./hamming

test_hamming: CMakeFiles/test_hamming
test_hamming: CMakeFiles/test_hamming.dir/build.make

.PHONY : test_hamming

# Rule to build all files generated by this target.
CMakeFiles/test_hamming.dir/build: test_hamming

.PHONY : CMakeFiles/test_hamming.dir/build

CMakeFiles/test_hamming.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/test_hamming.dir/cmake_clean.cmake
.PHONY : CMakeFiles/test_hamming.dir/clean

CMakeFiles/test_hamming.dir/depend:
	cd /home/dirrgang/exercism/cpp/hamming/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/dirrgang/exercism/cpp/hamming /home/dirrgang/exercism/cpp/hamming /home/dirrgang/exercism/cpp/hamming/build /home/dirrgang/exercism/cpp/hamming/build /home/dirrgang/exercism/cpp/hamming/build/CMakeFiles/test_hamming.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/test_hamming.dir/depend
