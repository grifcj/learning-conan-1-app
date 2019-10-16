from conans import ConanFile, CMake, python_requires

base = python_requires("conanbase/1.0.0-nightly@grifcj/dev")

class AppConan(base.get_conanfile()):
    name = "app"
    version = "1.0.0-nightly"
    scm = {
        "type": "git",
        "url": "https://github.com/grifcj/cmake-app",
        "revision": "auto"
    }
    requires = (
            "logger/1.0.0-nightly@grifcj/dev",
            "math/1.0.0-nightly@grifcj/dev")
    build_requires = (
            "cmake_extensions/1.0.0-nightly@grifcj/dev")
    generators = (
            "cmake_paths",
            "virtualrunenv")


