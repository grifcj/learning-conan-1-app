from conans import ConanFile, CMake, tools

class AppConan(ConanFile):
    name = "app"
    version = "0.1.0"
    license = "Beerware"
    author = "Connor Griffith grifcj@gmail.com"
    url = "https://github.com/grifcj/cmake-app"
    description = "An app that punked Chuck Norris"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake_find_package_multi"
    requires = "logger/0.1.0@grifcj/stable", "math/0.1.0@grifcj/stable"
    build_requires = "gtest/1.8.1@bincrafters/stable"

    def source(self):
        self.run("git clone https://github.com/grifcj/cmake-app .")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test()

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["app"]

