#!/bin/bash

set -e
set -x

pip install conan --upgrade
pip install conan_package_tools
conan profile new default --detect
conan config install https://github.com/grifcj/learning-conan-1-conanconfig.git
