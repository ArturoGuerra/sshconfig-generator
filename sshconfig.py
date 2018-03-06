#!/usr/bin/python3.6
import subprocess
import re

from pathlib import Path

configFile = str(Path.home()) + '/.ssh/config'
blacklist = ['auttaja', 'osu', 'mandalore']
sshconfig = open(configFile, 'r')

def ssh_genlist():
    l = list()
    lines = sshconfig.readlines()
    for line in lines:
        regex = re.match("Host ((?!\*)\w+)", line)
        if (regex) and regex.group(1) not in blacklist:
            l.append(regex.group(1))
    return l

for s in ssh_genlist():
    print(f"Server Name: {s}")
    subprocess.call(['scp', configFile, f'{s}:.ssh/config'])
    print('--------------------------------------------------')
