#!/usr/bin/python
import os
import subprocess

def build(cmd):
    print("Running {}: {}".format(os.getpid(), cmd))
    os.system(cmd)

if __name__ == "__main__":
    configs = [
            str("ninja -C build/d{}".format(d)) for d in range(0, 4)
    ]
    for c in configs:
        build(c)
