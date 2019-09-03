#!/usr/bin/python
import os
import subprocess
import time

def runCmds(cmds):
    p = subprocess.Popen(
            '/bin/bash',
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    for c in cmds:
        yield c
        p.stdin.write(c + os.linesep)
    p.stdin.close()
    for line in iter(p.stdout.readline, ""):
        yield line
    p.stdout.close()
    rc = p.wait()
    if rc:
        raise subprocess.CalledProcessError(rc, cmds)

if __name__ == "__main__":
    externals = [
            {
                'name' : 'googletest',
                'checkout' : [
                    "mkdir -p externals/googletest",
                    "cd externals/googletest",
                    "git init",
                    "git remote add origin https://github.com/google/googletest.git",
                    "git fetch --depth=1 origin release-1.8.0",
                    "git reset --hard FETCH_HEAD"
                    ]
                },
            {
                'name' : 'logger',
                'checkout' : (
                    "mkdir -p externals/logger",
                    "cd externals/logger",
                    "git init",
                    "git remote add origin git@github.com:grifcj/cmake-logger",
                    "git fetch --depth=1 origin master",
                    "git reset --hard FETCH_HEAD"
                    )
                },
            {
                'name' : 'math',
                'checkout' : (
                    "mkdir -p externals/math",
                    "cd externals/math",
                    "git init",
                    "git remote add origin git@github.com:grifcj/cmake-math",
                    "git fetch --depth=1 origin master",
                    "git reset --hard FETCH_HEAD"
                    )
                }
            ]

    for e in externals:
        path = 'externals/%s' % e['name']
        if not os.path.exists(path):
            for line in runCmds(e['checkout']):
                print(line)

