#!/bin/bash

set -e
set -x

conan profile new default --detect
conan config install https://github.com/grifcj/learning-conan-1-conanconfig.git
python build.py
