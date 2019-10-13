import os

from conans import ConanFile, CMake, tools
from six import StringIO

class AppTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    def test(self):
        buf = StringIO()
        self.run('app', output=buf, run_environment=True)
        assert 'The Fibonacci series is a grand thing' in buf.getvalue()
