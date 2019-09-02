cmake_minimum_required(VERSION 3.13)
project(math)

enable_testing()

include(externals.cmake)
AddExternals(googletest logger)

set(libName ${PROJECT_NAME})
add_library(${libName} math.cpp)
target_include_directories(${libName} PUBLIC ${CMAKE_CURRENT_LIST_DIR})
target_link_libraries(${libName} PUBLIC logger)

set(testName ${PROJECT_NAME}_unittest)
add_executable(${testName} math-test.cpp)
target_link_libraries(${testName} PUBLIC ${libName} gmock gmock_main)
add_test(${testName} ${testName})
