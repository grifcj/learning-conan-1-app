cmake_minimum_required(VERSION 3.13)
project(app)

enable_testing()

include(externals.cmake)

set(exeName ${PROJECT_NAME})
add_executable(${exeName} main.cpp)
target_link_libraries(${exeName} PUBLIC math)

