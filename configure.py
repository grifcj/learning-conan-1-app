#!/usr/bin/python
import os
import subprocess

def runCmd(cmd):
    print("Running {}: {}".format(os.getpid(), cmd))
    os.system(cmd)

if __name__ == "__main__":
    externals = [
            {
                'name' : 'googletest',
                'checkout' :
                    "git clone https://github.com/google/googletest.git externals/googletest && "
                    "cd externals/googletest && "
                    "git checkout release-1.8.0"
                },
            {
                'name' : 'logger',
                'checkout' : "git clone git@github.com:grifcj/cmake-logger externals/logger"

                },
            {
                'name' : 'math',
                'checkout' : "git clone git@github.com:grifcj/cmake-math externals/math"
                }
            ]

    for e in externals:
        path = 'externals/%s' % e['name']
        if not os.path.exists(path):
            runCmd(e['checkout'])

    configs = [
            "cmake -H. -Bbuild -GNinja"
            ]

    for c in configs:
        runCmd(c)

