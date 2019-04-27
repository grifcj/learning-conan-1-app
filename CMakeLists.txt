cmake_minimum_required(VERSION 3.13)
project(app)

enable_testing()

include(externals.cmake)
AddExternals(googletest logger math)

set(exeName ${PROJECT_NAME})
add_executable(${exeName} main.cpp)
target_link_libraries(${exeName} PUBLIC math logger)

set(testName ${PROJECT_NAME}_unittest)
add_test(NAME ${testName} COMMAND $<TARGET_FILE:${exeName}>)
set_tests_properties(
   ${testName}
   PROPERTIES
   PASS_REGULAR_EXPRESSION "Fibonacci.*grand")
