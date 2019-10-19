from cpt.packager import ConanMultiPackager
from pprint import pprint

if __name__ == "__main__":
    builder = ConanMultiPackager(
            archs=["x86_64"],
            username="grifcj",
            channel="dev",
            upload_dependencies="all",
            build_policy="missing",
            remotes= "https://api.bintray.com/conan/grifcj/learning")

    # Expect CI to define compiler versions with environment variables to
    # constrain build variants
    builder.add_common_builds()

    # Force c++11 stl, we get link errors with clang if not and supporting
    # c++11 with libc++ requires extra compiler and link options on linux
    builder.update_build_if(
            lambda build: True,
            new_settings={"compiler.libcxx": "libstdc++11"})

    builder.run()
