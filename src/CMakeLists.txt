find_package(logger REQUIRED)
find_package(math REQUIRED)

add_executable(app app.cpp)
target_link_libraries(app PUBLIC math::math logger::logger)

include(CMakeExtensions)
install_project_targets()
generate_cpp_info(app)
