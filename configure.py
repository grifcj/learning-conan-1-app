#!/usr/bin/python
import os
import subprocess
from concurrent.futures import ProcessPoolExecutor

def configure(cmd, env=None):
    if env is None:
        env = os.environ.copy()

    print("Running {}: {}".format(os.getpid(), cmd))
    os.system(cmd)

if __name__ == "__main__":
    configs = [
            str("cmake -H. -Bbuild/d{} -GNinja".format(d)) for d in range(0, 4)
    ]
    for c in configs:
        configure(c)
