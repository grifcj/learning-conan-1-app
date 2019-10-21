import platform
from cpt.packager import ConanMultiPackager
from pprint import pprint

if __name__ == "__main__":
    builder = ConanMultiPackager(
            archs=["x86_64"],
            reference: "app/1.0.0-nightly"
            username: "grifcj"
            channel="dev",
            login_username: "grifcj"
            upload: "https://api.bintray.com/conan/grifcj/learning"
            upload_dependencies="all",
            build_policy="missing")

    # Expect CI to define compiler versions with environment variables to
    # constrain build variants
    builder.add_common_builds(shared_option_name=False)

    # Force c++11 stl, we get link errors with clang if not and supporting
    # c++11 with libc++ requires extra compiler and link options on linux
    if platform.system() == "Linux":
        builder.update_build_if(
                lambda build: True,
                new_settings={"compiler.libcxx": "libstdc++11"})

    builder.run("default-cmake-ninja")
