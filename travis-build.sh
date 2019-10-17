conan remote add learning https://api.bintray.com/conan/grifcj/learning
conan install -if build . -s compiler.libcxx=libstdc++11 --build missing
conan build -bf build .
