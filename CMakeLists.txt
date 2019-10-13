cmake_minimum_required(VERSION 3.13)
project(app)

find_package(logger REQUIRED)
find_package(math REQUIRED)

add_executable(app main.cpp)
target_link_libraries(app PUBLIC math::math logger::logger)

include(CMakeExtensions)
install_project_targets()

enable_testing()
add_test(NAME app::unittest COMMAND $<TARGET_FILE:app>)
set_tests_properties(
   app::unittest
   PROPERTIES
   PASS_REGULAR_EXPRESSION "Fibonacci.*grand")
