cmake_minimum_required(VERSION 3.13)
project(app)

include(CMakeExtensions)
declare_source_package(app)

add_subdirectory(src)

include(CTest)
if (BUILD_TESTING)
	add_subdirectory(test)
endif()
