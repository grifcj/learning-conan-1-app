from conans import ConanFile, CMake, tools

def get_version():
    git = tools.Git()
    try:
        return git.run("describe --tags --dirty --always").replace('/', '-')
    except:
        return None

class AppConan(ConanFile):
    name = "app"
    version = get_version()
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

    scm = {
            "type": "git",
            "url": "https://github.com/grifcj/cmake-app",
            "revision": "auto"
            }

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test()

    def package(self):
        self.copy("app")

