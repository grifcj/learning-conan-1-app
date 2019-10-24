cmake_minimum_required(VERSION 3.13)
project(app)

find_package(logger REQUIRED)
find_package(math REQUIRED)

add_executable(app app.cpp)
target_link_libraries(app PUBLIC math::math logger::logger)
add_executable(app::app ALIAS app)

include(CMakeExtensions)
install_project_targets()

