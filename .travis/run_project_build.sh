 #!/bin/bash

 rm -rf build && mkdir -p build && cd build
 conan install -if build . -pr ./travis.conan.yml --build missing
 conan build -bf build .
