cmake_minimum_required(VERSION 3.13)
project(app VERSION ${PACKAGE_VERSION})

add_subdirectory(src)

include(CTest)
if (BUILD_TESTING)
	add_subdirectory(test)
endif()
