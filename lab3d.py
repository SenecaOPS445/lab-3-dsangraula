#!/usr/bin/env python3

import subprocess

def free_space():
   
    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'", shell=True, text=True, capture_output=True)
    return result.stdout.strip()  

if __name__ == '__main__':
    print(free_space())  
