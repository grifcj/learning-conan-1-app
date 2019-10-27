import os
from conans import ConanFile, CMake, python_requires

base = python_requires("conanbase/1.0.0-nightly@grifcj/dev")

class AppConan(base.get_conanfile()):
    name = "app"
    version = "1.0.0-nightly"
    url = "https://github.com/grifcj/cmake-app"
    license = "MIT"
    description = "An app for learning"
    scm = {
        "type": "git",
        "url": "https://github.com/grifcj/cmake-app",
        "revision": "auto"
    }
    requires = (
            "math/1.0.0-nightly@grifcj/dev")
    build_requires = (
            "cmake_extensions/1.0.0-nightly@grifcj/dev")
    generators = "cmake_paths"

    def _make_cmake(self):
        cmake = super()._make_cmake()
        cmake.definitions["logger_DIR"] = ""
        cmake.definitions["math_DIR"] = ""
        return cmake
