import platform
import os
import psutil
import socket

def main ():
    print(platform.node())
    print(platform.platform())
    print(platform.release())
    print(os.cpu_count())
    print(psutil.virtual_memory().total)
    print("testing functionality")

    hostname = socket.gethostname()
    print("Your Computer IP Address is:" + socket.gethostbyname(hostname))