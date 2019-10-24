cmake_minimum_required(VERSION 3.13)
project(app-test)

find_package(app REQUIRED)

enable_testing()
add_test(NAME app::unittest COMMAND $<TARGET_FILE:app::app>)
set_tests_properties(
   app::unittest
   PROPERTIES
   PASS_REGULAR_EXPRESSION "Fibonacci.*grand")
