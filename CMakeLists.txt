cmake_minimum_required(VERSION 3.13)
project(app)

enable_testing()

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(app main.cpp)
target_link_libraries(app PUBLIC CONAN_PKG::math CONAN_PKG::logger)

add_test(NAME app-test COMMAND $<TARGET_FILE:app>)
set_tests_properties(
   app-test
   PROPERTIES
   PASS_REGULAR_EXPRESSION "Fibonacci.*grand")
